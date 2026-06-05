#!/usr/bin/env python3
"""Lint an inline-email-builder fragment against the hard rules.

Dependency-free (stdlib only) so it runs on any machine / inside Codex.

Usage:
    python3 validate_email.py path/to/fragment.html
    cat fragment.html | python3 validate_email.py -

Exit code: 0 if no ERRORs, 1 if any ERROR. WARN/INFO never fail the build.
"""
import re
import sys

# Tags that must never appear (document wrapper / non-inline styling).
FORBIDDEN_TAGS = ["html", "head", "title", "body", "style", "link", "script"]


def read_source(arg: str) -> str:
    if arg == "-":
        return sys.stdin.read()
    with open(arg, encoding="utf-8") as fh:
        return fh.read()


def check(html: str):
    """Return (errors, warns, infos) as lists of strings."""
    errors, warns, infos = [], [], []

    # Strip HTML comments before structural checks — a comment that merely mentions
    # <style>/<head>/@media (e.g. a doc header) must not be flagged as a real tag.
    scan = re.sub(r"<!--.*?-->", "", html, flags=re.S)

    # 1. Forbidden document-wrapper / style tags.
    for tag in FORBIDDEN_TAGS:
        if re.search(rf"<\s*{tag}[\s>/]", scan, re.IGNORECASE):
            errors.append(f"forbidden <{tag}> tag present (fragment must be inline-only)")

    # 2. Media queries can't work without <style>.
    if "@media" in scan:
        errors.append("@media query present — not supported in inline-only fragments")

    # 3. Images: src must be absolute https, and need alt.
    imgs = re.findall(r"<img\b[^>]*>", scan, re.IGNORECASE)
    if not imgs:
        infos.append("no <img> tags found")
    for img in imgs:
        src_m = re.search(r"\bsrc\s*=\s*['\"]([^'\"]*)['\"]", img, re.IGNORECASE)
        src = src_m.group(1).strip() if src_m else ""
        if not src:
            errors.append(f"<img> missing src: {img[:70]}")
        elif src.startswith("[") and src.endswith("]"):
            infos.append(f"image token left to fill: {src}")
        elif src.startswith("http://"):
            warns.append(f"image uses insecure http:// (prefer https): {src}")
        elif not src.startswith("https://"):
            errors.append(f"image src not an absolute https URL: {src}")
        if not re.search(r"\balt\s*=", img, re.IGNORECASE):
            warns.append(f"<img> missing alt attribute: {img[:70]}")

    # 4. Styling must be inline — flag class/id used for styling.
    if re.search(r"\bclass\s*=", scan, re.IGNORECASE):
        warns.append("class= attribute present — inline styling only, classes won't apply in email")

    # 5. Unfilled THEME tokens must not remain (these are the skill's job to fill).
    theme_tokens = ["[bg_page]", "[bg_card]", "[color_heading]",
                    "[color_text]", "[color_accent]", "[year]"]
    for tok in theme_tokens:
        if tok in scan:
            errors.append(f"unfilled theme token {tok} — skill must replace with a real value")

    # 6. Deliverability nicety.
    if "[unsubscribe]" not in scan and "unsubscribe" not in scan.lower():
        warns.append("no unsubscribe link found (required for marketing email)")

    # 7. Size hint.
    kb = len(html.encode("utf-8")) / 1024
    if kb > 100:
        warns.append(f"fragment is {kb:.0f} KB — Gmail clips >102 KB; trim if close")

    return errors, warns, infos


def main():
    if len(sys.argv) != 2:
        print("usage: validate_email.py <file|-> ", file=sys.stderr)
        return 2
    html = read_source(sys.argv[1])
    errors, warns, infos = check(html)

    for e in errors:
        print(f"ERROR: {e}")
    for w in warns:
        print(f"WARN:  {w}")
    for i in infos:
        print(f"INFO:  {i}")

    print(f"\n{len(errors)} error(s), {len(warns)} warning(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
