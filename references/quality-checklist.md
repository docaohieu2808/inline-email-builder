# Quality checklist — self-review before returning

Run AFTER `validate_email.py` passes. The validator catches mechanical errors; this catches what
judgment must — is it complete, clear, and good? Fix anything that fails, then return.

## Structure (must-have)
- [ ] Hidden **preview text** (preheader) present, and it's a real teaser — not empty/lorem.
- [ ] Logo / header present (`[logo]`).
- [ ] Exactly **one primary CTA** button with a clear action label.
- [ ] **Unsubscribe** link present (legal for marketing email).
- [ ] Client bits left as `[tokens]` (logo, images, links) — none invented.

## Content
- [ ] Headline states the main benefit; no full stop.
- [ ] Not too long — headline + short intro + benefits + offer + CTA, not a wall of text.
- [ ] Benefits short & scannable (`✓` list).
- [ ] ONE offer/ask only; not crammed with extras.
- [ ] Tone matches the industry + the brief's language.
- [ ] **If Vietnamese: full diacritics everywhere** (no tiếng Việt không dấu).
- [ ] **No ALL-CAPS body/descriptions** (uppercase only for small eyebrows/labels).
- [ ] No section repeats another's point; cut any block that doesn't earn its place.

## Visual
- [ ] CTA colour clearly stands out against its background.
- [ ] Heading readable on its bg; body contrast ≥ 4.5:1; ≤ ~3 hues; dark mode avoids pure-black-on-transparent.
- [ ] Every `<img>` has a meaningful `alt`.
- [ ] Reads fine narrow (≤ 400px) — single column / rows stack.
- [ ] Multi-column rows (stats / cards / grid) fit cleanly 3-up or 2-up on desktop — **no 2+1 orphan**.
- [ ] Side-by-side cards look **balanced (~equal height)** — match content length and/or `min-height`. Mixed list + paragraph is OK if heights are comparable; only a tall-vs-short pair is the problem.
- [ ] **`font-family` is set on every text element** (h1/p/a/div), not only the wrapper — else Outlook falls back to Times.

If anything is off, fix and re-check — then return the fragment + the "fill these" list.
