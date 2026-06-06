# Quality checklist — self-review before returning

Run AFTER `validate_email.py` passes. The validator catches mechanical errors; this catches judgment.

## Frame & tokens (must-have)
- [ ] Text left as tokens: **`[title]` (heading) + `[content]` (body)** — NO written copy. Images go
  in **`[image_N]`** slots (the chosen arrangement block), not invented.
- [ ] Logo / header present (`[logo]`); footer present with `[contact]` + **`[unsubscribe]`** +
  view-in-browser.
- [ ] All client bits are `[tokens]` (logo, images, links) — none invented.
- [ ] Fixed chrome ("Hủy đăng ký", "Xem trên trình duyệt", labels) in **full Vietnamese diacritics**, NFC.

## Design (per Email Template Design Guidelines)
- [ ] **Not a bare flat box** — card has radius + shadow; design applied (gradient/band/badge/divider).
- [ ] **Every image is FRAMED** (border + mat + radius + shadow + caption) — no bare `<img>` in the body.
- [ ] Components designed where they fit (offer box, tick list, badge) — text in them = TOKENS.
- [ ] **Dashed border ONLY on a coupon-code box**; plain % offer = SOLID tinted box.
- [ ] **No CTA button** unless she explicitly asked (code.txt has none; offer/coupon is the action).

## Visual / technical
- [ ] `[title]`/`[content]` containers styled (font-family, size, line-height) so her pasted text
  inherits a good look.
- [ ] Body contrast ≥ 4.5:1; ≤ ~3 hues; dark mode avoids pure-black-on-transparent.
- [ ] Every `<img>` has a meaningful `alt`.
- [ ] Reads fine narrow (≤ 400px) — single column / rows stack.
- [ ] Multi-column / image blocks fit cleanly (no 2+1 orphan); **no `box-sizing` reliance**; columns
  stack on mobile; image sizes equal; each `[image_N]` has a meaningful `[image_N_alt]`.
- [ ] `font-family` set on every text element (not only the wrapper) — else Outlook → Times.
- [ ] No region uses a CSS background image as its ONLY content (image-as-content → `<img>`).

If anything is off, fix and re-check — then return the layout + the "fill these" list.
