# Email design guidelines (how it should LOOK & READ — not just be code-correct)

`layout-patterns.md` = structure · `theming-guide.md` = colour/font · **THIS** = the visual,
typographic, content-formatting and component conventions that make output look professional and
consistent. Apply on top of whatever layout/style is chosen. Conventions, not a fixed look —
adapt to the style (luxe = hairline dividers + serif; bright = bolder boxes).

## A. Style directions (the overall look)
Minimal · Dark · Luxe · Editorial · Duotone · Bento · Bright · Classic. What makes it modern:
- **Whitespace** — generous section padding (24–40px); crowded = dated.
- **Big tight headlines** — 28–42px, bold, slight negative letter-spacing. Keep `line-height ≥ 1.3`
  (Vietnamese stacked diacritics need room; never < 1.2 or they clip/overlap).
- **Restraint** — ONE accent colour, the rest neutral; avoid rainbow + heavy shadows.
- **Rounded** — `border-radius` on cards/images/buttons (pill `999px`) for modern; sharper for classic/editorial.
- **Narrow column** — `max-width:520–600px` reads more premium than 640.
- **Flat / high-contrast** — clean light bg (`#fbfaf8`) or dark (`#0d0d10` + light text + accent).
- **Honest font limit** — no custom web fonts (need `<style>`); use a web-safe stack
  (`"Helvetica Neue",Helvetica,Arial` / `Georgia,serif`). Size + weight + spacing carry it.

## B. Typography rules
- **Headline** — short, **NO full stop** at the end.
- **Body paragraphs** — complete sentences **with** full stops; 15–16px, line-height 1.6–1.8.
- **Bullets** — short, **< ~12 words** each, usually no full stop.
- **CTA label** — an action phrase, **no full stop** ("Book now", "Nhận ưu đãi 20%").
- **Eyebrow/label** — UPPERCASE, letter-spacing 2–3px, small (11–13px), accent colour, above the headline.
- **UPPERCASE is ONLY for small eyebrows/labels.** Headlines, body, descriptions, card text are
  **sentence case** — NEVER `text-transform:uppercase` on a paragraph/description (it reads as shouting).
- One typeface family per email; hierarchy comes from size + weight, not many fonts.

## C. Content formatting rules
- **Benefits / features** → tick list (`✓` in accent colour) or short bullets.
- **Step-by-step / process** → numbered list (1. 2. 3.).
- **Promotion / coupon / code** → a highlighted **box** (tinted bg or bordered); offer big + bold.
- **Important aside** → a tinted note box, not buried mid-paragraph.
- Never a wall of text — break into short paragraphs + lists.

## D. Component conventions
| Block | Convention |
|---|---|
| Logo / header | top of email — **vary the placement** per design: left, centred, with a tagline, or inside a coloured brand band. Don't always default to top-left. |
| Eyebrow | small UPPERCASE, letter-spaced, accent colour, above headline |
| Hero image | full-width fluid (`width:100%; max-width; height:auto`), rounded if modern |
| Offer / voucher box | tinted bg (pastel of accent) OR thin/dashed border; label + big offer; centred |
| CTA button | ONE primary, padded `<a>` with solid accent bg + white text, rounded; never an image |
| Benefit list | `✓` in accent + short text |
| Service card / row | image + bold title + 1-line description (use `media-row` for 2-col → stacks on mobile) |
| Divider | thin 1px hairline in a muted tone, OR generous spacing (luxe favours both) |
| Footer | small (11–13px), muted grey, generous spacing; contact + unsubscribe + view-in-browser |

## E. Visual micro-rules
- **Emphasise the offer** with a *pastel-of-accent* background or a neat border — not a loud
  full-width banner (unless the style is "bright").
- One accent colour does the heavy lifting; keep everything else neutral.
- Let it breathe — spacing over borders; only add a border/shadow when it earns its place.
- **Keep it TIGHT.** A typical email = logo → hero/headline → 1–3 sections → offer → CTA → footer.
  Don't cram every possible block (header-row + intro + banner + grid + cards + …). Restraint reads
  premium; a long busy email reads cheap. If a section doesn't earn its place, cut it.
- **Multi-column must actually FIT** (stat rows, feature cards, product grids). Each column's
  `max-width` must be ≤ `(container_width − side_padding) ÷ N`, or the row wraps to an ugly **2+1
  orphan**. For a ~600px card: **3-up → col ≤ ~165px**, **2-up → col ≤ ~270px** (incl. padding). If
  3 won't fit cleanly, use 2-up or stack — never ship a 3-up that breaks to 2+1.
- **Side-by-side cards: balance the HEIGHT — and YOU control it because you write the copy.**
  Rendered height can't be read off the HTML (it depends on wrapping + font), so don't try to
  *detect* imbalance after the fact — **author both cards to a similar line count from the start.**
  Estimate lines per card from the code: a `✓`/bullet list = **one line per item**; a paragraph ≈
  **`characters ÷ ~30`** lines (for a ~270px card). Keep the two within ~1 line of each other (mixed
  list + paragraph is fine if the line counts match).
  - **`min-height` is only a FLOOR** — it equalises *only when BOTH cards fit inside it*. A paragraph
    taller than the `min-height` still overflows, so the boxes stay uneven. min-height fixes *small*
    differences; it can NOT shorten a genuinely longer card. (This is why a long paragraph still looks
    lopsided despite a min-height.)
  - If the two contents can't be made similar length, **stack them full-width** (one column) — then
    there's no side-by-side height problem at all.
  - (No auto equal-height in email: flexbox `align-items:stretch` / `display:table-cell` break in
    Outlook or don't stack on mobile.)

## Reminder
Adapt to the chosen style, but still obey the hard rules + run `validate_email.py`.
