# Layout patterns (a palette to remix — pick/vary per brief)

Every email is a **different design**. Don't reuse one structure. Use this as a menu: pick an
archetype that fits the occasion, then re-theme and rearrange. Mixing archetypes is encouraged.
All patterns obey the hard rules (inline CSS, no `<style>`, fluid responsive). Concrete worked
examples live in `templates/examples/` (they are nails-themed — copy the STRUCTURE, not the copy).

## Archetypes

| # | Archetype | Best for | Structure sketch |
|---|---|---|---|
| A | **Hero + media-rows** | product/service highlights, "what's new" | logo → banner → intro → alternating image+text rows → CTA → social → footer |
| B | **Editorial single-column** | luxury/premium, storytelling, announcements | centered logo → full-width hero → centered headline + prose → divider → outline CTA → text links |
| C | **Promo / voucher** | sales, discounts, coupon codes | small logo → big SALE banner → 1-line offer → dashed voucher block (code) → big rounded CTA → social |
| D | **Grid / catalog** | menus, collections, multiple SKUs | logo → slim banner → intro → 2×N tile grid (image + label + price) → CTA → social |
| E | **Newsletter / digest** | recurring updates, multi-topic | logo → section blocks (heading + blurb + read-more), repeated → footer |
| F | **Transactional / receipt** | confirmations, bookings, orders | logo → status headline → detail table (label/value rows) → support links → footer |
| G | **Plain personal** | founder notes, re-engagement | logo (or none) → left-aligned text only, minimal styling, one inline link CTA |

## How to vary (so two emails never look the same)

- **Layout:** swap archetype; change logo placement (left vs centered); banner vs no banner;
  1-col vs 2-col rows vs grid; CTA shape (rounded pill / square / outline / text link).
- **Theme:** new palette + web-safe font per industry (see `theming-guide.md`); light vs dark;
  generous vs tight spacing.
- **Tone:** match the occasion/language; headline style (playful, elegant, urgent).

## Responsive building blocks (no media query)

- **Fluid container:** `width:100%; max-width:Npx; margin:0 auto`.
- **Fluid image:** `width:100%; max-width:Npx; height:auto; display:block`.
- **Auto-stacking columns** (2-col → 1-col, or grid): the `font-size:0` parent + `inline-block`
  `max-width` children trick — see `templates/blocks/media-row.html` and "Multi-column" in
  `email-html-rules.md`. Reuse it for 2-up rows, 3-up features, or N×2 grids.

## Reminder
The constant is the **rules + token contract**, not the look. Always finish by running
`scripts/validate_email.py` and fixing every ERROR.
