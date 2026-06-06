# Layout catalog — assemble a varied layout from these parts

The skill is a **layout assembler**: combine the parts below into a different layout each time (like
an app where one click changes the layout). **Text = `[title]` + `[content]` tokens (never written).
Images = `[image_N]` tokens.** Concrete block HTML lives in `templates/blocks/`.

## 0. Card shell (her convention)
- Card `max-width: 600–640px`, centred. Font **`Arial, Helvetica, sans-serif`**.
- **box-shadow** `0 0 6px #cccccc` (subtle depth — Outlook ignores it, fine).
- **Card background = a layout dial:** a solid **colour**, plain **white/none**, or a **`[bg_image]`**
  (always with a `background-color` fallback — see email-html-rules). Vary it per email.

## 1. Logo position (header)
- **Left** — logo left, optional "view online" link right (2-col header).
- **Centred** — logo centred, optional tagline under it; or on a coloured brand band.
- **Right** — logo right (less common, good for variety).

## 2. Banner (optional)
- Include a foreground `<img src='[banner]'>` (full-width fluid) for launch / promo / showcase.
- Skip it for plain / transactional. She can add/remove.

## 3. Image-arrangement block (pick one, vary per email)
**Each image = a FRAMED CARD** (border + white mat + radius + shadow + caption — like a PowerPoint
picture placeholder), NEVER a bare `<img>` (Design Guidelines §1). Build multi-image blocks with the
**fluid inline-block** technique (no `box-sizing`; columns FIT with slack; equal sizes; column `<div>`s
adjacent — see "Multi-column" in `email-html-rules.md`). Concrete blocks in `templates/blocks/`:

| Block | Looks like | File |
|---|---|---|
| 1 framed card | one image in a card | `image-card-frame.html` |
| 2 across | two framed cards side by side → stack on mobile | `image-2-across.html` |
| 2×2 grid | four framed cards, 2 top + 2 bottom | `image-4-grid.html` |
| 2 stacked + text | a vertical image pair on one side + `[content]` on the other (mirror to swap side) | `image-pair-side-text.html` |

(Compose new ones freely — 3-across, image+text row… — same fluid technique, same framed cards.)

## 3b. Content components (design per the occasion — see `design-guidelines.md` §4)
`offer-box.html` (SOLID % / DASHED code) · `cta-button.html` (big accent button) ·
`benefit-tick-list.html` (`✓` + `[benefit_N]`) · badge/pill · testimonial box. Text = tokens.

## 4. Footer (always — chrome, NOT copy) — her convention
- **Social = ICON row by default** — a "Theo dõi chúng tôi" label + `<a href='[facebook]'><img
  src='[icon_facebook]'></a>` (icon src = `[icon_*]` token = her self-hosted PNG set; link href =
  `[facebook]` token). Text links only if the style asks.
- **`[contact]`** · **`Copyright © [name]`** · **`[unsubscribe]`** ("Hủy đăng ký") · view-in-browser
  (`[domain]`, "Xem trên trình duyệt").
- Footer usually sits **below the card** (outside the shell), like her `code.txt`.

## Assembling
`logo(position) → [banner?] → [title] → [content] → image-block → footer` — but the **order is yours
to vary** (e.g. image block above `[title]`, or `[content]` beside a 2-stacked block). Pick a fresh
combo each time (see `recommendations.md`). Style every part per the brand colour + chosen Style
(`design-guidelines.md` / `theming-guide.md`), tight spacing, sans + NFC (SKILL rule 8).
