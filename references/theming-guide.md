# Theming guide

Pick a small, tasteful palette + web-safe font that fits the industry, then fill the theme
tokens. Keep it restrained — 2–3 colors. Verify contrast ≥ 4.5:1 for text.

## Palette per industry (starting points — adapt to brand if given)

| Industry | heading/accent | accent (CTA) | text | page bg |
|---|---|---|---|---|
| Nails / salon / spa | `#66d0d0` teal or `#ff6f91` pink | `#ff6f91` | `#333333` | `#fef6f8` |
| Beauty / cosmetics | `#c98bb9` mauve | `#b5179e` | `#2b2b2b` | `#faf5f9` |
| Restaurant / food | `#e07a5f` terracotta | `#c1440e` | `#3d2b1f` | `#fdf6ec` |
| Fitness / gym | `#2a9d8f` | `#e76f51` | `#22333b` | `#f1faee` |
| Tech / SaaS | `#3a86ff` | `#2563eb` | `#1f2937` | `#f5f7fb` |
| Retail / fashion | `#222222` | `#d4af37` gold | `#333333` | `#ffffff` |

If the brand provides colors, use those; the table is only a fallback.

## Fonts (web-safe stacks — no web fonts, they need `<style>`)
- Clean/modern: `"Helvetica Neue", Helvetica, Arial, sans-serif`
- Extra-safe Vietnamese / friendly: `Tahoma, Verdana, sans-serif`
- Editorial/luxe feel: stay sans but lean on **letter-spacing + weight + whitespace** (a serif is NOT
  worth it for Vietnamese — see below).
Set the stack inline on **every** text element (not just the wrapper — see `email-html-rules.md`).

**Vietnamese-safe typography = SKILL hard rule 8** (sans only — no Georgia/Times serif; NFC;
`font-weight` ≤ 700; heading `line-height ≥ 1.3`). Obey it when theming; not restated here.

Keep `[content]` HTML inline-styled too (e.g. `<p style='margin:0 0 12px 0;'>...</p>`).

> Copy / messaging rules → `copywriting-rules.md`. Pre-output contrast & quality review →
> `quality-checklist.md`.
