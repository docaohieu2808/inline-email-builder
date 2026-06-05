#!/usr/bin/env python3
"""Merge a JSON map of token values into a template fragment.

Replaces [key] occurrences with values from a JSON file. Useful now for filling theme
tokens, and later as the per-row step if briefs ever arrive as a batch (a list of JSON
rows). Dependency-free.

Usage:
    python3 fill_tokens.py template.html values.json [> out.html]

values.json example:
    {"name": "Bloom Nails", "color_heading": "#66d0d0", "year": "2026"}
Keys are matched as [key]. Unlisted [tokens] are left untouched (so backend merge can
still fill them).
"""
import json
import re
import sys


def main():
    if len(sys.argv) != 3:
        print("usage: fill_tokens.py <template.html> <values.json>", file=sys.stderr)
        return 2
    template_path, values_path = sys.argv[1], sys.argv[2]

    with open(template_path, encoding="utf-8") as fh:
        html = fh.read()
    with open(values_path, encoding="utf-8") as fh:
        values = json.load(fh)

    def replace(match):
        key = match.group(1)
        return str(values[key]) if key in values else match.group(0)

    # Match [token] where token is word-ish (letters, digits, underscore).
    out = re.sub(r"\[([A-Za-z0-9_]+)\]", replace, html)
    sys.stdout.write(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
