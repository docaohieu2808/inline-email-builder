# Design guidelines — how the assembled LAYOUT should LOOK

`layout-patterns.md` = the blocks to assemble · `theming-guide.md` = colour/font · **THIS** = the
visual + typographic conventions for styling the layout (frame + image blocks + the `[title]`/
`[content]` slots). The body text is `[content]` (she fills) — you style the shell + image blocks, not
her words.

## A. Style directions (the look)
Minimal · Dark · Luxe · Editorial · Duotone · Bento · Bright · Classic. What makes it modern:
- **Whitespace** — generous padding; crowded = dated.
- **Big headline slot** — `[title]` 28–34px, bold (≤700), `line-height ≥ 1.3` (VN diacritics need room).
- **Restraint** — ONE accent colour, the rest neutral; no rainbow / heavy shadows.
- **Rounded** — `border-radius` on images/cards for modern; sharper for classic/editorial.
- **Narrow column** — `max-width:520–600px` reads premium.
- **Flat / high-contrast** — clean light bg or dark (+ light text + accent).
- **Web-safe sans only** — size + weight + spacing carry it (no serif for Vietnamese — SKILL rule 8).

## B. Typography (styling the slots + chrome)
- **`[title]`** — 28–34px, bold, accent/heading colour, `line-height ≥ 1.3`, centred or left per style.
- **`[content]`** — 15–16px, **`line-height 1.45–1.5`**, neutral colour. Set `font-family` on the
  container so her pasted text inherits it. Don't put words in it — it's her slot.
- **Eyebrow/label** (if the frame uses one) — small UPPERCASE, letter-spaced, accent, above `[title]`.
  UPPERCASE is ONLY for tiny eyebrows — never on body/headings.
- One typeface family; `font-family` on EVERY text element (Outlook resets `<h1>`/`<p>` to Times else).

## C. Component conventions
| Block | Convention |
|---|---|
| Logo / header | top — **vary placement**: left / centred / + tagline / right / inside a coloured band |
| Banner | optional foreground `<img [banner]>`, full-width fluid, rounded if modern |
| Image block | 2-across / 2×2 grid / 2-stacked+text — fluid inline-block (`templates/blocks/`), stacks on mobile, **equal sizes** |
| Divider | thin 1px hairline in a muted tone, OR generous spacing |
| Footer | small (11–13px), muted; social + `[contact]` + `[unsubscribe]` + view-in-browser |

## D. Spacing & micro-rules
- **Tight, even vertical rhythm** — section gaps ~18–20px; each section a consistent top padding +
  `padding-bottom:0` (next section's top sets the gap). `[title]`→`[content]` gap ~8–10px. Compact
  reads premium; loose/airy reads cheap.
- **One accent** does the heavy lifting; let it breathe (spacing over borders).
- **Image blocks must FIT — no 2+1 orphan**: size columns so N of them + padding sit under the
  container with slack; **never rely on `box-sizing`** (math in `email-html-rules.md` → "Multi-column").
  Equal image sizes; if they won't fit, fewer-up or stack.

## Reminder
Style the layout, obey the hard rules, run `validate_email.py`. **Don't write copy** — text stays
`[title]` + `[content]`.
