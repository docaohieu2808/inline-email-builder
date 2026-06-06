---
name: inline-email-builder
description: Build email HTML templates as inline-CSS fragments (no <style>/<head>/<html>, fluid responsive without media queries). Use when asked to create a marketing/transactional email template from a natural-language brief — title, logo, body content, social links, optional banner — for any industry (nails/salon, retail, etc.). Output is a paste-ready fragment compatible with merge-token pipelines.
license: MIT
metadata:
  author: hieudc
  version: "0.17.0"
---

# Inline Email Builder

Turn a specific brief into a **production-ready email HTML fragment** that survives real
inboxes. This skill is the **framework** — it encodes the hard parts (client quirks,
inline-only CSS, fluid responsiveness, token contract) so they stay consistent. The
**design itself is fresh every time**.

> **Design a NEW layout for each request — do not reuse one fixed template.** Every brief
> is a different industry/occasion/style, so vary the structure (hero, media-rows, grid,
> promo/voucher, single-column editorial…) and the theme to fit *this* job. The files in
> `templates/` and the examples in `templates/examples/` are a **palette to remix**, never a
> mandatory skeleton. What must stay identical across every email is the rules + token
> contract below — not the look.

## Who you're talking to (CRITICAL — read first)

The end user is a **Vietnamese-speaking front-end coder**. She wants ONE thing fast: **beautiful,
correct email code**. She fills the client-specific bits (logo, links, images) herself in her
editor — that's trivial for her, and it keeps client data OFF the agent.

- **Reply in Vietnamese**, concise.
- **Your job = the FRAME, NOT the words.** Design a beautiful, rules-compliant, responsive inline-CSS
  **frame** (header/footer/colours/layout per brand + occasion) and leave the **editorial text as
  tokens** — `[title]` (heading) + `[content]` (body) — for her to fill, exactly like her merge
  pipeline (see her `code.txt`: just `[title]` + `[content]` inside a designed shell). **Do NOT write
  marketing copy, and do NOT add sections/buttons she didn't ask for.** She builds the body (paragraphs,
  offer, CTA, lists…) inside `[content]` herself. You style the slots; she fills the words.
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
7. **Always end with a footer** — `[contact]` + an `[unsubscribe]` link + a "view in browser" link.
   Marketing email legally requires unsubscribe; never omit it.
8. **Vietnamese-safe typography (CRITICAL).**
   (a) Copy uses full diacritics (`Cảm ơn`, `Giảm 20%`) — NEVER tiếng Việt không dấu — and in **NFC
   (precomposed)** form, never decomposed/NFD (else accents render detached: `mềm` → base + a
   floating mark). The validator flags NFD; normalize with `unicodedata.normalize('NFC', …)`.
   (b) **`font-weight` ≤ 700 (bold) — NEVER 800/900.** Heavy weights **squash the base letter** of
   stacked-diacritic chars (`ộ ệ ề ự ễ`): the `o`/`e` shrinks to fit the two stacked marks inside the
   thick glyph (very visible at heading sizes). Use `font-weight:bold` (700), never `800`/`900`.
   (c) Heading `line-height ≥ 1.3` (room for the double diacritics).
   (d) Web-safe **SANS** stack set inline on every text element: `"Helvetica Neue", Helvetica, Arial,
   sans-serif` (or `Tahoma` — best Vietnamese). **NEVER `Georgia` / `Times New Roman` (serif) for
   Vietnamese** — they lack/mis-render the stacked-diacritic glyphs (`ề ộ ậ ữ`) on Windows, so the
   tone mark detaches (`mềm` → "Mề f m"). For a luxe/editorial feel, get it from layout + spacing +
   weight, NOT a serif. (Serif is fine only for English-only copy.)

## Token convention (compatible with existing pipeline)

Reuse the bracket tokens the team already uses; fill concrete values when the brief gives
them, otherwise LEAVE the token for their merge system:
`[logo] [title] [content] [domain] [banner] [bg_image] [facebook] [instagram] [tiktok] [youtube]
[cta_text] [cta_url] [contact] [name] [unsubscribe]`
(`[bg_image]` = optional CSS background image on a card/section — always with a `background-color`
fallback; see "Background images" in `references/email-html-rules.md`.)

## Workflow

1. **Parse brief** → her 8-field prompt (see `references/brief-input-template.md`). **Any STYLE /
   LAYOUT field she leaves blank → auto-pick a fitting one.** The **message text is NEVER generated** —
   heading stays `[title]`, body stays `[content]` for her to fill. All client data (logo, links,
   images) stays as `[tokens]` too. Only ask if the brief is essentially empty.
2. **Theme + visual style** → harmonize a 2–3 colour palette with the **brand's stated colour**
   (it's given — don't invent one) + a web-safe font fitting the industry (contrast ≥ 4.5:1, see
   `references/theming-guide.md`), and pick a look — modern minimal, dark, editorial, duotone,
   bento… see `references/design-guidelines.md`. Style is a separate dial from layout; vary per brief.
3. **Choose a fresh layout for THIS brief** — pick an archetype from
   `references/layout-patterns.md` (or compose a new one) that fits the occasion; don't default
   to the same structure every time. **Two emails of the same occasion must differ STRUCTURALLY in
   the FRAME — not just recolour the same shell** (see "Vary even within the same occasion" in
   `references/recommendations.md`). Remix the concrete designs in `templates/examples/*` —
   reference starting points, not a required skeleton. For "image + text" sections that sit
   side-by-side on desktop and stack on mobile, use `templates/blocks/media-row.html` (fluid
   inline-block, no media query, no Bootstrap — see "Multi-column" in `references/email-html-rules.md`).
   **Also pick a header + footer/social treatment that fits THIS style — don't auto-default to
   logo-top-left + a plain text-link footer every time.** Choose per style: logo left / centred /
   in a coloured band; social as a text row / **icon row** (`[icon_*]` tokens) / a "Theo dõi:" label /
   placed in the header. (See "Vary the HEADER & FOOTER too" in `references/recommendations.md`.)
4. **Leave the text as TOKENS — do NOT write copy.** Heading → `[title]`; body → `[content]` (a
   single slot she fills with her own HTML: paragraphs, offer, CTA, lists…). Don't invent benefit
   lists / offer boxes / CTA buttons she didn't ask for — keep the frame clean (like her `code.txt`).
   Just **style the `[title]` + `[content]` containers** (font-family, size, colour, line-height per
   `design-guidelines.md`) so her pasted text inherits a good look.
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

