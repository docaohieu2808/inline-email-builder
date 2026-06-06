# Layout catalog — assemble a varied layout from these parts

The skill is a **layout assembler**: combine the parts below into a different layout each time (like
an app where one click changes the layout). **Text = `[title]` + `[content]` tokens (never written).
Images = `[image_N]` tokens.** Concrete block HTML lives in `templates/blocks/`.

## 1. Logo position (header)
- **Left** — logo left, optional "view online" link right (2-col header).
- **Centred** — logo centred, optional tagline under it; or on a coloured brand band.
- **Right** — logo right (less common, good for variety).

## 2. Banner (optional)
- Include a foreground `<img src='[banner]'>` (full-width fluid) for launch / promo / showcase.
- Skip it for plain / transactional. She can add/remove.

## 3. Image-arrangement block (pick one, vary per email)
Build every multi-image block with the **fluid inline-block** technique (no `box-sizing`; columns
sized to FIT with slack; equal image sizes; the two column `<div>`s adjacent). See "Multi-column" in
`email-html-rules.md`. Concrete blocks in `templates/blocks/`:

| Block | Looks like | File |
|---|---|---|
| 1 image | one full-width image | (just an `<img [image_1]>`) |
| 2 across | `[img][img]` side by side → stack on mobile | `image-2-across.html` |
| 2×2 grid | 4 images, 2 top + 2 bottom | `image-4-grid.html` |
| 2 stacked + text | a vertical image pair on one side + `[content]` on the other (mirror to swap side) | `image-pair-side-text.html` |

(Compose new ones freely — 3-across, image+text row, etc. — same fluid technique.)

## 4. Footer (always — chrome, NOT copy)
Social links (`[facebook] [instagram] [youtube]` — text row / icon row / "Theo dõi:" label) +
**`[contact]`** + **`[unsubscribe]`** + a "view in browser" (`[domain]`). Style per the look; the
content here is fixed boilerplate, not marketing copy.

## Assembling
`logo(position) → [banner?] → [title] → [content] → image-block → footer` — but the **order is yours
to vary** (e.g. image block above `[title]`, or `[content]` beside a 2-stacked block). Pick a fresh
combo each time (see `recommendations.md`). Style every part per the brand colour + chosen Style
(`design-guidelines.md` / `theming-guide.md`), tight spacing, sans + NFC (SKILL rule 8).
