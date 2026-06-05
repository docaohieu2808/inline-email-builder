# Modern style (the "look" layer — independent of the 7 layout archetypes)

Layout (`layout-patterns.md`) = how blocks are arranged. **Style = how it feels.** They are two
separate dials. Any archetype can be rendered dated OR modern; this file is the modern dial.

## What makes inline email look modern (2024–2026)

1. **Whitespace, lots of it** — generous padding (32–44px), big gaps between sections. Crowded = dated.
2. **Big, tight headlines** — 34–46px, `font-weight:bold`, `line-height:1.1`, slight negative
   `letter-spacing:-0.5px`. Let the type carry the design.
3. **Restraint** — one accent color, mostly neutrals. Avoid rainbow gradients + heavy drop shadows
   (a single bold gradient hero or a dark theme is fine when intentional).
4. **Rounded everything** — `border-radius:14–20px` on images/cards, **pill buttons**
   `border-radius:999px`.
5. **Narrow column** — `max-width:520–600px` reads more premium than 640.
6. **Flat, high-contrast** — clean backgrounds (`#fbfaf8` warm-white) or **dark mode**
   (`#0d0d10` bg, light text, neon accent). Dark + a vivid gradient hero looks very current.
7. **Real or abstract imagery, rounded** — soft "blob"/duotone abstracts or product photos; never
   text baked into a banner image (that's the dated tell — keep headline as live HTML text).

## The honest constraint
True brand-custom fonts need `<style>`/`@font-face`, which the inline-only pipeline bans. So use a
clean web-safe stack and let **size + weight + spacing** do the work:
`font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;` (or `Georgia,serif` for editorial).
This still looks modern; it just won't be a bespoke typeface.

## Style directions to offer
- **Minimal / editorial** — white space, one big headline, one image, pill CTA. (example: `templates/examples/`… build fresh)
- **Bold dark** — dark card, vivid gradient hero, neon pill, big type.
- **Duotone** — two-color treatment across imagery + accents.
- **Bento** — rounded cards in an asymmetric grid (reuse the auto-stacking column trick).
- **Magazine** — large hero, serif headline, multi-column body that stacks on mobile.

## Reminder
Style is free to change every send. The hard rules + token contract + `validate_email.py` do NOT
change. Pick a style that fits the brand/occasion, then validate.
