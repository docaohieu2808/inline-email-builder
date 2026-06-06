# Email design guidelines (how it should LOOK & READ — not just be code-correct)

`layout-patterns.md` = structure · `theming-guide.md` = colour/font · **THIS** = the visual,
typographic, content-formatting and component conventions that make output look professional and
consistent. Apply on top of whatever layout/style is chosen. Conventions, not a fixed look —
adapt to the style (luxe = hairline dividers + whitespace; bright = bolder boxes).

## A. Style directions (the overall look)
Minimal · Dark · Luxe · Editorial · Duotone · Bento · Bright · Classic. What makes it modern:
- **Whitespace** — generous section padding (24–40px); crowded = dated.
- **Big tight headlines** — 28–42px, bold, slight negative letter-spacing. Keep `line-height ≥ 1.3`
  (Vietnamese stacked diacritics need room; never < 1.2 or they clip/overlap).
- **Restraint** — ONE accent colour, the rest neutral; avoid rainbow + heavy shadows.
- **Rounded** — `border-radius` on cards/images/buttons (pill `999px`) for modern; sharper for classic/editorial.
- **Narrow column** — `max-width:520–600px` reads more premium than 640.
- **Flat / high-contrast** — clean light bg (`#fbfaf8`) or dark (`#0d0d10` + light text + accent).
- **Honest font limit** — no custom web fonts (need `<style>`); use a web-safe sans stack
  (`"Helvetica Neue",Helvetica,Arial`). Size + weight + spacing carry it.

## B. Typography rules
- **Headline** — short, **NO full stop** at the end.
- **Body paragraphs** — complete sentences **with** full stops; 15–16px, **line-height 1.45–1.5**
  (tight & compact — NOT 1.6+, that reads loose/airy; but keep ≥1.45 so VN diacritics don't clip).
  Heading line-height 1.3 (VN-safe min).
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
| Offer box (no code) | a **plain % / amount** offer ("Giảm 20%") with NO code → **SOLID tinted box** (pastel of accent), label + big offer, centred. **Do NOT use a dashed border here.** |
| Coupon-code box | **dashed / cut-out border is ONLY for an actual code** (`DCD1007`) — the "clip this coupon" metaphor. No code → not dashed. |
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
- **Tight, consistent vertical rhythm.** Keep section gaps EQUAL and **compact (~18–20px**, not 28+).
  Don't pile a big top padding on one block AND a big bottom padding on the next — they compound into
  an uneven, airy gap. Cleanest pattern: each section gets a consistent top padding and
  `padding-bottom:0`, so the next section's top padding alone sets the gap. Body line-height 1.45–1.5.
  Headline→intro margin ~10px (not 14+). Prefer compact spacing — loose/airy reads cheap.
- **Keep it TIGHT.** A typical email = logo → hero/headline → 1–3 sections → offer → CTA → footer.
  Don't cram every possible block (header-row + intro + banner + grid + cards + …). Restraint reads
  premium; a long busy email reads cheap. If a section doesn't earn its place, cut it.
- **Multi-column must FIT — no 2+1 orphan** (stat rows, cards, grids). Size columns so N of them +
  their padding sit under the container with slack; **don't rely on `box-sizing`** (sizing math + the
  box-sizing trap live in `email-html-rules.md` → "Multi-column"). If 3 won't fit, go 2-up or stack.
- **Side-by-side cards must look equal-height.** You write the copy → author both to a similar line
  count (a `✓` list = 1 line/item; a paragraph ≈ chars ÷ 30). `min-height` only floors *small*
  differences — it can't shorten a longer card; if they can't match, **stack** instead. (Email has no
  reliable auto equal-height — flexbox/table-cell break.)

## Reminder
Adapt to the chosen style, but still obey the hard rules + run `validate_email.py`.
