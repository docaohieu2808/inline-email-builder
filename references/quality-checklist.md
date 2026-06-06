# Quality checklist — self-review before returning

Run AFTER `validate_email.py` passes. The validator catches mechanical errors; this catches judgment.

## Frame & tokens (must-have)
- [ ] Editorial text left as tokens: **`[title]` (heading) + `[content]` (body)** — NO invented copy,
  extra sections, or CTA buttons she didn't ask for.
- [ ] Logo / header present (`[logo]`); footer present with `[contact]` + **`[unsubscribe]`** +
  view-in-browser.
- [ ] All client bits are `[tokens]` (logo, images, links) — none invented.
- [ ] Fixed chrome ("Hủy đăng ký", "Xem trên trình duyệt", labels) in **full Vietnamese diacritics**, NFC.

## Visual / technical
- [ ] `[title]`/`[content]` containers styled (font-family, size, line-height) so her pasted text
  inherits a good look.
- [ ] Body contrast ≥ 4.5:1; ≤ ~3 hues; dark mode avoids pure-black-on-transparent.
- [ ] Every `<img>` has a meaningful `alt`.
- [ ] Reads fine narrow (≤ 400px) — single column / rows stack.
- [ ] Multi-column rows fit cleanly (no 2+1 orphan); **no `box-sizing` reliance**.
- [ ] `font-family` set on every text element (not only the wrapper) — else Outlook → Times.
- [ ] No region uses a CSS background image as its ONLY content (image-as-content → `<img>`).

If anything is off, fix and re-check — then return the frame + the "fill these" list.
