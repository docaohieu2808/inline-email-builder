---
name: inline-email-builder
description: Build email HTML templates as inline-CSS fragments (no <style>/<head>/<html>, fluid responsive without media queries). Use when asked to create a marketing/transactional email template from a natural-language brief — title, logo, body content, social links, optional banner — for any industry (nails/salon, retail, etc.). Output is a paste-ready fragment compatible with merge-token pipelines.
license: MIT
metadata:
  author: hieudc
  version: "0.3.1"
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
4. **Images = absolute URLs** (`https://...`). Never local paths, never `<style>`-based bg for
   critical content. Keep file size low; prefer the user's licensed-stock host.
5. **Every `<img>` has meaningful `alt`.** Single-quote attributes (matches existing pipeline).
6. **Keep merge tokens in `[...]` form** for fields the backend fills (see `references/tokens.md`).

## Token convention (compatible with existing pipeline)

Reuse the bracket tokens the team already uses; fill concrete values when the brief gives
them, otherwise LEAVE the token for their merge system:
`[logo] [title] [content] [domain] [banner] [facebook] [twitter] [youtube] [instagram]
[cta_text] [cta_url] [contact] [name] [unsubscribe]`

## Workflow

1. **Parse brief** → the user fills the form in `references/brief-input-template.md`
   (industry, occasion, brand, style, layout, content, images, links, tone/language).
   **Any field left blank → auto-generate a value that fits the rest of the brief**; never
   block on optional fields. Images/links not provided stay as `[tokens]` and go into the
   final "still needed" list. Only ask the user if the brief is essentially empty.
2. **Theme + visual style** → pick a 2–3 color palette + web-safe font fitting the industry
   (contrast ≥ 4.5:1, see `references/theming-guide.md`) AND a look — modern minimal, bold
   dark, editorial, duotone, bento… see `references/modern-style.md`. Style is a separate dial
   from layout; vary it per brief.
3. **Choose a fresh layout for THIS brief** — pick an archetype from
   `references/layout-patterns.md` (or compose a new one) that fits the occasion; do not
   default to the same structure every time. Build it from the blocks in
   `templates/blocks/`; `templates/base-skeleton.html` and `templates/examples/*` are
   reference starting points to remix, not a required skeleton. For "image + text" sections
   that sit side-by-side on desktop and stack on mobile, use `templates/blocks/media-row.html`
   (fluid inline-block, no media query, no Bootstrap — see "Multi-column" in
   `references/email-html-rules.md`).
4. **Write copy** for `[title]` + `[content]` in the requested tone/language.
5. **Fill** inline styles with the theme. Only insert image URLs the user **explicitly
   provided**; otherwise leave the image `[token]` (images are bought manually — see step 7).
6. **Validate** — run the linter and fix every ERROR before returning. Run it from THIS
   skill's own directory (works wherever the skill is installed — `.codex/skills/`,
   `.claude/skills/`, etc.):
   ```bash
   cd <this-skill-directory> && python3 scripts/validate_email.py <output.html>
   ```
7. **Return** the final fragment in a fenced ```html block, then:
   - **Image spec sheet** — images are PURCHASED per-image by the user, so NEVER auto-fetch,
     auto-generate, or invent image URLs. Instead, for every image slot leave its `[token]`
     and output a buying spec so she purchases the right asset once: `token · where it's used
     · recommended size (px) + aspect ratio · suggested subject/keywords`. Example:
     `[banner] · top hero · 1280×440 (≈3:1), display 640 wide · "spring pastel nails, soft light"`.
   - **Tokens left to fill** — the remaining `[link]`/text tokens she must paste real values into.

## Quality upgrades over legacy templates

- Real `alt` text on every image (legacy templates often had none / mislabeled icons).
- Name social tokens by the actual network (`[facebook]`, `[instagram]` — not a generic
  `[twitter]` pointing at a Yelp icon).
- Avoid fragile spacing hacks (e.g. hard-coded `margin-bottom:230px`); use padding inside
  blocks instead.
- Bulletproof CTA = padded `<a>` with inline background (no image-only buttons).

## Image sourcing — manual, never automated

Images are **bought per-image** (each has its own price) from the user's licensed-stock site.
So the skill **never** auto-fetches, auto-generates, hot-links, or invents an image URL — that
would cost money and/or break licensing. Always leave the image `[token]` and emit the buying
spec (see workflow step 7) so she purchases the right asset and pastes its hosted https URL.
The only images the skill may use directly are ones the user explicitly provides in the brief.

## Scaling later (not yet — YAGNI)

This is a per-email **skill** (human picks + reviews). If briefs ever arrive as a batch
(a sheet of N clients × brand data), wrap this in a workflow that loops `fill_tokens.py`.
Do not build the batch path until there is real batch input.
