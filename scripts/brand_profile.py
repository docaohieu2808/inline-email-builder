#!/usr/bin/env python3
"""Manage per-client brand profiles (reuse logo/colors/social/contact across emails).

A profile is a JSON file holding the constants for one brand. Real profiles live next to this
skill in `brand-profiles/<slug>.json` and are gitignored (never committed); only EXAMPLE.json
ships. Override the directory with env EMAIL_BRAND_PROFILES_DIR.

Commands:
    list                 → list saved profiles
    new <slug>           → scaffold brand-profiles/<slug>.json from EXAMPLE.json
    show <slug>          → print the profile flattened to token values (JSON)
    apply <slug> <file>  → fill [tokens] in <file> from the profile, print result

Token mapping: name→[name] logo→[logo] domain→[domain] facebook/instagram/youtube→[..]
contact→[contact] unsubscribe→[unsubscribe]; colors.accent→[color_accent],
colors.heading→[color_heading], colors.text→[color_text], colors.bg_page→[bg_page],
colors.bg_card→[bg_card].
"""
import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_ROOT = os.path.dirname(HERE)
PROFILE_DIR = os.environ.get("EMAIL_BRAND_PROFILES_DIR",
                             os.path.join(SKILL_ROOT, "brand-profiles"))

COLOR_KEYS = {"accent": "color_accent", "heading": "color_heading", "text": "color_text",
              "bg_page": "bg_page", "bg_card": "bg_card"}
FLAT_KEYS = ["name", "logo", "domain", "facebook", "instagram", "youtube",
             "contact", "unsubscribe"]


def profile_path(slug):
    return os.path.join(PROFILE_DIR, f"{slug}.json")


def flatten(profile):
    """Map a profile dict to {token_name: value} (token names without brackets)."""
    out = {k: profile[k] for k in FLAT_KEYS if k in profile}
    for ck, tok in COLOR_KEYS.items():
        if ck in profile.get("colors", {}):
            out[tok] = profile["colors"][ck]
    return out


def cmd_list():
    if not os.path.isdir(PROFILE_DIR):
        print("(no profiles dir yet)")
        return
    slugs = sorted(f[:-5] for f in os.listdir(PROFILE_DIR)
                   if f.endswith(".json") and f != "EXAMPLE.json")
    print("\n".join(slugs) if slugs else "(no profiles yet — create one with: new <slug>)")


def cmd_new(slug):
    dst = profile_path(slug)
    if os.path.exists(dst):
        sys.exit(f"already exists: {dst}")
    shutil.copy(os.path.join(PROFILE_DIR, "EXAMPLE.json"), dst)
    print(f"created {dst} — edit it with the brand's real logo URL, colors, links.")


def load(slug):
    p = profile_path(slug)
    if not os.path.exists(p):
        sys.exit(f"no profile '{slug}' in {PROFILE_DIR} (try: list)")
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def cmd_show(slug):
    print(json.dumps(flatten(load(slug)), ensure_ascii=False, indent=2))


def cmd_apply(slug, fragment):
    values = flatten(load(slug))
    with open(fragment, encoding="utf-8") as fh:
        html = fh.read()
    html = re.sub(r"\[([A-Za-z0-9_]+)\]",
                  lambda m: str(values[m.group(1)]) if m.group(1) in values else m.group(0),
                  html)
    sys.stdout.write(html)


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    cmd, rest = args[0], args[1:]
    if cmd == "list":
        cmd_list()
    elif cmd == "new" and rest:
        cmd_new(rest[0])
    elif cmd == "show" and rest:
        cmd_show(rest[0])
    elif cmd == "apply" and len(rest) == 2:
        cmd_apply(rest[0], rest[1])
    else:
        print(__doc__)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
