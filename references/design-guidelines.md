# Email Template Design Guidelines

How the email should **LOOK and READ** — the aesthetic + content-formatting system, not just
code-correctness. **The skill DESIGNS the components; the TEXT inside is always a TOKEN** (`[title]
[content] [offer] [cta_text] [benefit_N] [image_N_caption] [testimonial] [author]…`) — you never write
the words. Apply on top of the chosen layout (`layout-patterns.md`) + palette (`theming-guide.md`).
Conventions, not a fixed look — adapt to the Style. **Never ship bare flat boxes — design it.**

> **DEFAULT structure = her `code.txt`: logo + `[title]` + `[content]` + icon-social + footer**
> (`[contact]` + `Copyright © [name]` + unsubscribe/view). The components below (framed image cards,
> offer/coupon box, badge, banner, tick list, CTA…) are a **toolkit — used ONLY when the brief/content
> calls for them, never auto-injected.** A plain email is just title + content + social + footer.
>
> **But two axes, kept separate:** *content blocks* = on-demand · ***visual design = ALWAYS on*.** Even
> that plain title+content email MUST be richly designed — decorative header (band / gradient + fallback
> / `[bg_image]`), a **wave / decorative divider**, rounded + soft shadow, styled circular social icons,
> tasteful colour. **§1 visual rules apply to EVERY email; a flat white rectangle is WRONG.** §4
> components are the on-demand toolkit — §1 decoration is not optional.

## 1. Visual design rules (what the eye sees)
- **Card shell** — white / colour / `[bg_image]`; `border-radius:12–16px`; soft `box-shadow`; Arial.
- **Frame every image** — an image sits in a CARD: `border:1px solid #eee` + `padding:8–10px` (white
  mat) + `border-radius` + `box-shadow` (+ optional caption) — like a **PowerPoint picture placeholder**.
  NEVER a bare `<img>` floating in the body. (block: `image-card-frame.html`)
- **One accent colour** + neutrals; ≤ 3 hues. Restraint reads premium.
- **Highlight box** — pastel-of-accent bg or a tinted bordered box to emphasise an offer/aside.
- **Dashed border = ONLY a coupon-code box.** A plain % offer with no code = **SOLID tinted box**.
- **Dividers** — a thin 1px hairline, a row of dots, or generous spacing. A **curved / wave / cut**
  divider must be a designed **IMAGE** (`[divider_*]`) — email CSS can't draw waves/clip-path.
- **Badges / pills** — small `border-radius:999px` tinted label for eyebrows / tags / prices.
- **Gradients** — OK, but put a solid `background:#fallback;` FIRST (Outlook ignores the gradient).
  Diagonal "cut" = `linear-gradient(120deg,#A 50%,#B 50%)`.
- **Rounded** for modern; sharper for classic. **Circle** image = `border-radius:50%` (square source).
- **Spacing** — generous, even; tight rhythm (~18–20px gaps); crowded = dated.

## 2. Typography rules
- **Heading `[title]`** — 26–34px, bold (≤700), `line-height ≥ 1.3`, **no full stop**, centred/left per style.
- **Body `[content]`** — 15–16px, `line-height 1.5–1.6`, full stops OK (complete sentences).
- **Bullets** — short (< ~12 words), usually no full stop.
- **CTA `[cta_text]`** — action phrase, **no full stop**.
- **Eyebrow** — UPPERCASE, letter-spacing 2–3px, 11–13px, accent. UPPERCASE **only** for tiny eyebrows.
- One typeface (**Arial**); hierarchy from size + weight. `font-family` on EVERY text element. Sans, NFC (rule 8).

## 3. Content-formatting rules (how content is presented — text still tokens)
- **Benefits / features** → tick list (`✓` accent icon) + `[benefit_N]` tokens.
- **Step-by-step / process** → numbered list (1. 2. 3.) + tokens.
- **Promotion / coupon** → highlighted BOX (tinted bg; dashed only for a real code); offer big + bold (`[offer]`).
- **Quote / testimonial** → tinted box, larger text, `[testimonial]` + `[author]`.
- **Important aside** → a tinted note box, not buried mid-paragraph.
- Never a wall of text — short paragraphs + lists / cards.

## 4. Component rules (each block's convention)
| Component | Convention | Token text |
|---|---|---|
| Header / logo | top; vary placement (left / centred / right / in a coloured band) | — |
| Banner / hero | full-width fluid `<img>`, rounded if modern | `[banner]` |
| **Framed image card** | border + mat + radius + shadow + caption (PPT placeholder) | `[image_N] [image_N_caption]` |
| Service / product card | framed image card + bold title + 1-line desc (+ price badge) | `[image_N] [image_N_caption]` |
| Offer box (no code) | **SOLID** pastel-of-accent box, label + big offer, centred | `[offer]` |
| Coupon-code box | **DASHED** / cut-out border (only for a real code) | `[coupon]` |
| CTA button | **OFF by default** — code.txt has none; the offer/coupon is the action. Add ONLY if she asks (then: big padded `<a>`, solid accent bg, rounded) | `[cta_text]`→`[cta_url]` (if asked) |
| Benefit list | `✓` accent icons + short lines | `[benefit_N]` |
| Testimonial | tinted quote box | `[testimonial] [author]` |
| Badge / pill | small rounded tinted label | `[badge]` |
| Divider | 1px hairline / dots / spacing / **wave-image** | `[divider_*]` (if image) |
| Footer | small muted; **ICON** social + `[contact]` + `Copyright © [name]` + unsubscribe/view | — |

## 5. Overall (the style guide)
- Pick ONE **Style** (`picker-layout-style.md`) + the brand colour; apply consistently.
- **Restraint > clutter** — one accent, tight even rhythm, frame images, design components — but don't
  cram every block. A long busy email reads cheap.
- **Vary the layout** each email (`recommendations.md`). Obey the hard rules; run `validate_email.py`.
- The skill **DESIGNS**; she fills the **TOKENS**. Never write the words.
