---
name: inline-email-builder
description: Build email HTML templates as inline-CSS fragments (no <style>/<head>/<html>, fluid responsive without media queries). Use when asked to create a marketing/transactional email template from a natural-language brief — title, logo, body content, social links, optional banner — for any industry (nails/salon, retail, etc.). Output is a paste-ready fragment compatible with merge-token pipelines.
license: MIT
metadata:
  author: hieudc
  version: "0.19.3"
---

# Inline Email Builder

Turn a specific brief into a **production-ready email HTML fragment** that survives real
inboxes. This skill is the **framework** — it encodes the hard parts (client quirks,
inline-only CSS, fluid responsiveness, token contract) so they stay consistent. The
**design itself is fresh every time**.

> **Assemble a fresh LAYOUT for each request — like an app, a different layout every time.** Vary:
> **logo position** (left / centred / right), **banner** (yes / no), the **image-arrangement block**
> (1 image · 2 across · 2 stacked + text · 2×2 grid · …), and the **footer/social** style. The **text
> stays `[title]` + `[content]` tokens** (you NEVER write copy); images are `[image_N]` tokens in the
> chosen arrangement. What's identical every time = the rules + token contract below; the layout changes.

## Who you're talking to (CRITICAL — read first)

The end user is a **Vietnamese-speaking front-end coder**. She wants ONE thing fast: **beautiful,
correct email code**. She fills the client-specific bits (logo, links, images) herself in her
editor — that's trivial for her, and it keeps client data OFF the agent.

- **Reply in Vietnamese**, concise.
- **Your job = the DESIGN, NOT the words.** **DEFAULT structure = her `code.txt`:** logo + `[title]`
  + `[content]` + **icon-social** + footer (`[contact]` + `Copyright © [name]` + unsubscribe/view).
  **Two separate axes — keep them straight:**
  - **STRUCTURE = code.txt** (title + content + social + footer). Extra **content blocks** — image
    grid / offer / coupon box / badge / banner / tick list / CTA — are **on-demand: add ONLY when the
    brief or content calls for them, NEVER auto-inject** onto a plain email.
  - **VISUAL DESIGN = ALWAYS rich** — decorative header (coloured band / gradient + fallback /
    `[bg_image]`), a **wave / decorative divider**, rounded corners + soft shadow, styled (circular)
    social icons, tasteful colour. **A plain white rectangle is WRONG** — even a bare title+content
    email MUST look designed. Decoration is always on; only the content blocks above are optional. When you DO use a component, design it per the **Email Template Design Guidelines**
  (`references/design-guidelines.md`): frame images, dashed = code / solid = %, etc. **All TEXT is a
  TOKEN** (`[title] [content] [offer] [image_N_caption]…`) — you design the boxes, never write the words.
- **Recommend Layout + Style — don't make her choose blind.** Brand industry + colors are GIVEN
  context (never ask her to pick "by color/industry"). From this email's **occasion + campaign**,
  proactively suggest a fitting Layout + Style with a one-line reason (see
  `references/recommendations.md`), harmonized with the brand's colors. She accepts or tweaks.
  Show the full numbered menu (`references/picker-layout-style.md`) only if she wants to browse.
- **Do NOT ask for, store, or insert real client data** (logo URLs, client links, real images).
  Leave them as `[tokens]`. Privacy: client info should never need to reach the agent. (If she
  volunteers a URL, you may use it — but never request it, and never persist client data.)
- After the code, give a short **"fill these" list** of the `[token]` placeholders she'll replace
  (images, logo, links). Don't spec, size, optimize, or suggest images — that's all hers.
- Run `scripts/validate_email.py` yourself; fix errors silently; surface issues only in plain
  Vietnamese.
- **Deliver via a `.html` FILE, not a terminal paste.** Copying long inline-HTML out of a terminal
  (Codex CLI) can corrupt it — line-wrap newlines split tags (`</`↵`div>` breaks the tag, so the next
  block inherits the previous one's bold), and accents may decompose to NFD. **Save the fragment to a
  `.html` file and tell her to open/copy THAT.** (If she insists on terminal copy, warn her to re-check
  for split tags + run NFC normalize.)

## When to use

Asked to "make an email template" / "design an email" for a campaign or transactional
message, where output must be an **HTML fragment** (no document wrapper), inline CSS,
mobile-friendly. Example brief:

> Template email ngành nails: tiêu đề, logo, nội dung, link social (có thể đổi),
> có/không banner. Ảnh nhẹ, CSS inline, không `<style>`/`<head>`/`<html>`, responsive.

## Hard rules (NON-NEGOTIABLE — see `references/email-html-rules.md`)

1. **Fragment only** — no `<html>`, `<head>`, `<title>`, `<body>`, `<style>`, no `<link>`.
2. **Inline CSS only** — every style lives in a `style='...'` attribute. No classes for styling.
3. **Responsive WITHOUT media queries** — fluid technique: `width:100%` + `max-width:Npx` +
   `margin:0 auto`; images `width:100%; max-width:Npx; height:auto; display:block`.
4. **Images = absolute `https://` URLs** (never local/relative). Sourcing, sizing & hosting are
   the user's — see "Logo, images, links" below.
5. **Every `<img>` has meaningful `alt`.** Single-quote attributes (matches existing pipeline).
6. **Keep merge tokens in `[...]` form** for fields the backend fills (see `references/tokens.md`).
7. **Always end with a footer** — `[contact]` + `Copyright © [name]` + an `[unsubscribe]` link + a
   "view in browser" link. **Social = icon images (`[icon_*]` tokens) by default** (her convention —
   a "Theo dõi chúng tôi" label + an icon row; text links only if the style asks). Marketing email
   legally requires unsubscribe; never omit it.
8. **Vietnamese-safe typography (CRITICAL).**
   (a) Copy uses full diacritics (`Cảm ơn`, `Giảm 20%`) — NEVER tiếng Việt không dấu — and in **NFC
   (precomposed)** form, never decomposed/NFD (else accents render detached: `mềm` → base + a
   floating mark). The validator flags NFD; normalize with `unicodedata.normalize('NFC', …)`.
   (b) **`font-weight` ≤ 700 (bold) — NEVER 800/900.** Heavy weights **squash the base letter** of
   stacked-diacritic chars (`ộ ệ ề ự ễ`): the `o`/`e` shrinks to fit the two stacked marks inside the
   thick glyph (very visible at heading sizes). Use `font-weight:bold` (700), never `800`/`900`.
   (c) Heading `line-height ≥ 1.3` (room for the double diacritics).
   (d) Web-safe **SANS** stack on every text element — default **`Arial, Helvetica, sans-serif`** (her
   pipeline; or `Tahoma`). **NEVER `Georgia` / `Times New Roman` (serif) for Vietnamese** — they
   mis-render the stacked-diacritic glyphs (`ề ộ ậ ữ`) on Windows (`mềm` → "Mề f m"); a luxe feel
   comes from layout + spacing + weight, NOT a serif. (Serif OK only for English-only copy.)

## Token convention (compatible with existing pipeline)

Reuse the bracket tokens the team already uses; fill concrete values when the brief gives
them, otherwise LEAVE the token for their merge system:
`[logo] [title] [content] [domain] [banner] [image_1..4] [image_N_alt] [image_N_caption] [bg_image]
[eyebrow] [offer] [offer_label] [coupon] [benefit_1..n] [testimonial] [author]
[badge] [divider_*] [icon_*] [facebook] [instagram] [youtube] [tiktok] [contact] [name] [unsubscribe]`
(No CTA-button tokens by default — code.txt has no button; add `[cta_text]`/`[cta_url]` only if she asks.
Component tokens — `[offer]`, `[coupon]`, `[benefit_N]`, `[image_N_caption]`, `[testimonial]`… —
are the **text slots inside the designed components** (see `design-guidelines.md` §4). The skill
designs the box; she fills the token. `[icon_*]` = social icon images; `[divider_*]` = a designed
wave/curve divider image; `[bg_image]` = CSS background — always with a `background-color` fallback.)

## Workflow

1. **Parse brief** → her 8-field prompt (see `references/brief-input-template.md`). **Any STYLE /
   LAYOUT field she leaves blank → auto-pick a fitting one.** The **message text is NEVER generated** —
   heading stays `[title]`, body stays `[content]` for her to fill. All client data (logo, links,
   images) stays as `[tokens]` too. Only ask if the brief is essentially empty.
2. **Theme + visual style** → harmonize a 2–3 colour palette with the **brand's stated colour**
   (it's given — don't invent one) + a web-safe font fitting the industry (contrast ≥ 4.5:1, see
   `references/theming-guide.md`), and pick a look — modern minimal, dark, editorial, duotone,
   bento… see `references/design-guidelines.md`. Style is a separate dial from layout; vary per brief.
3. **Assemble a fresh LAYOUT for THIS brief** from the catalog in `references/layout-patterns.md`:
   pick a **logo position** (left/centred/right), **banner** (yes/no), an **image block**
   (`templates/blocks/*` — 2-across, 2×2 grid, 2-stacked+text…), and a **footer/social** style. Place
   the `[title]` + `[content]` text slots + the image block in a sensible order. **Vary the combo each
   time** — don't reuse the same one (see "Vary the LAYOUT each time" in `recommendations.md`).
   Build image blocks with the **fluid inline-block** technique (no `box-sizing`, columns fit with
   slack, equal sizes) — see "Multi-column" in `references/email-html-rules.md`.
4. **Build the DEFAULT structure** (logo + `[title]` + `[content]` + icon-social + footer), styled
   per the **Email Template Design Guidelines** (`design-guidelines.md`) — clean card + shadow, accent
   heading, Arial. **Add components ONLY if the brief/content calls for them** (product showcase →
   framed image cards; promo with a code → DASHED coupon box; plain % → SOLID offer box; etc.) — do
   NOT auto-inject a coupon / CTA / image grid onto a plain email. Any image you DO add must be a
   **framed card** (never bare). **All component TEXT is a TOKEN** (`[title] [content] [offer]
   [image_N_caption]…`) — design the box, never write the words.
5. **Fill** inline styles with concrete theme colours (real hex, harmonized with the brand
   colour). Leave every image as its `[token]` unless the user explicitly provided a URL.
6. **Validate & self-review** — run the linter (fix every ERROR), then self-review against
   `references/quality-checklist.md` (the `[title]`/`[content]` slots present, **unsubscribe/footer**,
   token slots not invented copy, full diacritics on the fixed chrome, contrast, responsive). Run the linter from THIS skill's own directory (works wherever installed —
   `.codex/skills/`, `.claude/skills/`, etc.):
   ```bash
   cd <this-skill-directory> && python3 scripts/validate_email.py <output.html>
   ```
7. **Return** the final frame in a fenced ```html block, then a short **"fill these" list** — the
   `[token]` placeholders she replaces: **`[title]` + `[content]`** (the text) plus logo, images, links.

## Quality upgrades over legacy templates

- Real `alt` text on every image (legacy templates often had none / mislabeled icons).
- Name social tokens by the actual network (`[facebook]`, `[instagram]` — not a generic
  `[twitter]` pointing at a Yelp icon).
- Prefer padding inside blocks over arbitrary hard-coded margins for spacing — **except** a
  deliberate large offset to clear a **background image's** decorative zone (that's intentional and
  tied to the image, not a stray hack; see "Background images" in `email-html-rules.md`).
- Bulletproof CTA = padded `<a>` with inline background (no image-only buttons).

## Logo, images, links = the coder's job (not ours)

The skill's deliverable is **the template** — design + code with `[token]` placeholders. Logo,
images, and URLs are 100% hers: she sources them, optimizes/sizes the files, and fills them in her
editor. The agent never receives, fetches, generates, optimizes, specs, or invents them — just
leaves clean tokens. (Bonus: client data stays off the agent.)

