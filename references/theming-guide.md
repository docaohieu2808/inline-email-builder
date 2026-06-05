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

**⚠ Do NOT use `Georgia` / `Times New Roman` (serif) for Vietnamese.** On Windows they lack/mis-render
the double-diacritic glyphs (`ề ộ ậ ữ`) → the tone mark **detaches** ("mềm" → "Mề f m"). Sans (Arial /
Tahoma / Helvetica Neue) renders Vietnamese correctly. Serif is OK only for English-only copy.

**Vietnamese diacritics — IMPORTANT:** the base letter of stacked-diacritic chars (`ộ ệ ề ự ễ`)
gets **squashed by heavy font-weights** — cap at `font-weight:bold` (700), **NEVER 800/900** (the
heavy glyph shrinks the `o`/`e` to fit the two stacked marks; very visible at heading sizes). Give headings
`line-height ≥ 1.3` for vertical room. Any web-safe stack works; `"Helvetica Neue", Helvetica,
Arial, sans-serif` is a clean default.

Keep `[content]` HTML inline-styled too (e.g. `<p style='margin:0 0 12px 0;'>...</p>`).

> Copy / messaging rules → `copywriting-rules.md`. Pre-output contrast & quality review →
> `quality-checklist.md`.
