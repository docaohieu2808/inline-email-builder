# Email HTML rules (why each constraint exists)

These constraints come from the existing pipeline + how email clients render. Follow them
exactly; the validator enforces the mechanical ones.

## 1. Fragment only — no document wrapper
No `<html>`, `<head>`, `<title>`, `<body>`, `<style>`, `<link>`. The backend/ESP injects the
fragment into its own wrapper. A nested `<html>`/`<style>` would be stripped or break the host
page. → Output starts at the outermost `<div>`.

## 2. Inline CSS only
Gmail strips `<style>` blocks in many contexts and ALL clients honor inline `style=`. Every
visual rule lives in a `style='...'` attribute. Do not rely on `class`/`id` for styling.

## 3. Responsive WITHOUT media queries
Media queries need `<style>`, which the inline-only pipeline bans. Use the **fluid** technique:
- Containers: `width:100%; max-width:Npx; margin:0 auto;`
- Images: `width:100%; max-width:Npx; height:auto; display:block;`
- Avoid fixed pixel widths on containers.
Degrades gracefully: on phones the container fills the screen up to `max-width`.

### Multi-column that auto-stacks (NO Bootstrap, NO media query)
"Image left + text right on desktop → image on top + text below on mobile" is fully doable
inline. Use the **fluid inline-block wrap** ("media object") — concrete blocks in `templates/blocks/`
(`image-2-across`, `image-4-grid`, `image-pair-side-text`):
- Parent `font-size:0; text-align:center;` (kills inline-block whitespace gap).
- Each column `display:inline-block; width:100%; max-width:280px; vertical-align:top;` and
  resets its own `font-size`. The two column divs MUST be adjacent (no whitespace between them).
- **Sizing must leave slack.** 2 columns' total footprint (each `max-width` **plus its own padding**)
  must be **comfortably under** the container's inner width — e.g. for a ~600px-inner card, 2-up
  columns ≤ ~280px each. **Never rely on `box-sizing:border-box`** to squeeze them — Outlook ignores
  it, so a `max-width:290px; padding:8px` column is really **306px** wide → 2×306 > 600 → wraps to
  one column in the inbox. Put padding on an INNER div, keep the column itself padding-free.
- Wide container → both columns sit side by side. Narrow (mobile) → each is 100% → they wrap to
  stacked, in source order (put the image column first for image-on-top).
Verified: renders side-by-side at 700px and stacked at 380px with zero media queries.

> Do NOT use Bootstrap (or any external CSS framework) in email — clients strip the stylesheet
> and ignore its grid/flex. The fluid inline-block pattern above replaces it.

## 4. Images
- **Absolute `https://` URLs only.** No local, relative, or `file://` paths.
- Every `<img>` needs a meaningful `alt`. Decorative-only images may use `alt=''` deliberately.
- Don't put critical text inside images (clients block images by default → blank email).
- The images themselves are the user's — see "Images are entirely the user's" below.

## 4b. Background images (optional — her real templates use them)
A decorative card/section background via CSS is supported in modern clients (Gmail, Apple Mail, iOS).

- **A CSS background image is a DECORATIVE backdrop behind real content — NEVER a region's only
  content.** If a column/section is meant to *show* a picture (product, hero, lookbook), use a
  **foreground `<img>`** — it always renders, carries `alt`, and the region is never blank. A
  bg-image box whose only content is a small label over a huge top `padding` becomes an **empty
  column** whenever the image is absent (Outlook, image-blocked, or an unfilled token). **Rule of
  thumb: image IS the content → `<img>`; image sits BEHIND text → CSS background (+ fallback).**

**Write the background so the fallback colour SURVIVES — this is the part that's easy to get wrong:**
- **Longhand (safest):** `background-color:#FALLBACK; background-image:url('[bg_image]');
  background-position:top center; background-repeat:no-repeat; background-size:cover;`
- **Or shorthand WITH the colour inside it:** `background:#FALLBACK url('[bg_image]') top center no-repeat;`
- **TRAP — NEVER write `background-color:#X;` then `background:url(...) ...;`** on the same element.
  The `background` shorthand **resets `background-color` to `transparent`**, wiping your fallback. The
  colour must live *inside* the shorthand, or use the longhand `background-image` (which leaves
  `background-color` alone).
- **ALWAYS keep that fallback colour.** Outlook desktop (Word engine) ignores CSS background images,
  and Gmail blocks images until the user loads them — the fallback colour is what shows there, and any
  overlaid text must stay readable on it.
- **Keep the image a `[token]`** (e.g. `[bg_image]`) — it's the user's asset, `https://` only.
- **Don't rely on a bg image for text legibility.** If contrast over the image is risky, put the text
  on a solid inner box (as her sample does: artwork on the outer card, white inner box for `[content]`).
- A bg image with a **decorative top zone** needs the content pushed below it — use top padding or a
  spacer (her legacy template uses a large `margin-bottom` on the logo block to clear the artwork).
  That offset is **intentional and tied to the specific image** — adjust it to the image, don't treat
  it as a stray hack.
- Pixel-perfect bg images in Outlook desktop need VML (`<v:rect>`/`<v:fill>`) — out of scope for
  inline-only; the fallback colour is the accepted Outlook behaviour.

## 5. Markup hygiene
- Single-quote attributes (`style='...'`) to match the existing templates.
- Use entities: `&copy;`, `&amp;`, `&nbsp;`.
- Add a hidden preheader div for inbox preview text (see `templates/examples/`).
- Use web-safe **sans** stacks (`"Helvetica Neue", Helvetica, Arial`, or Tahoma/Verdana). Custom web
  fonts need `<style>`/`@font-face` → not allowed; pick a web-safe stack. (Georgia/Times serif only
  for English-only copy — they break Vietnamese diacritics; see hard rule 8d.)
- **Set `font-family` inline on EVERY text element** (`<h1>`, `<p>`, `<a>`, text `<div>`) — do NOT
  rely on inheritance from a parent wrapper. Outlook and several clients RESET font-family on
  `<h1>`/`<p>`/`<td>` to **Times New Roman**, breaking the look (it renders fine in a browser, but
  wrong in the inbox). Repeat the same stack on each text node. Styled `<div>`s inherit a bit more
  reliably than `<h1>`/`<p>`, but still set the family explicitly to be safe.

## 6. Accessibility & deliverability
- Contrast ≥ 4.5:1 for body text.
- Real `alt` text, logical reading order.
- Always include an `[unsubscribe]` link (legal requirement for marketing email).

## Where it goes & who sees it (don't conflate the two)
The fragment is **pasted into an email platform / builder** (the ESP) — that's WHY it must be
inline-only + fragment + no `<style>`. The platform then **sends it to recipients who open it across
ALL clients & devices** (Gmail, Apple Mail, mobile, Outlook web AND desktop). So **both layers
matter**: the platform dictates inline/fragment; the clients dictate rendering. The audience is
everything → **stay conservative**: fluid widths (no `box-sizing` reliance), bg-image fallbacks, sans
fonts, NFC, no broken tags. Don't optimise for one modern client and don't assume "the builder
handles it" — the builder just sends; the inbox decides.

**Client support target:** modern clients render the div-based fluid approach cleanly. **Outlook
desktop (Word engine)** is the strict one — it ignores `max-width`, `box-shadow`, CSS bg-images and
`box-sizing`; design so it **degrades gracefully** (a full-width stack is fine), never relying on
those. Pixel-perfect Outlook needs table layout + VML (out of scope; raise before adding).

## Images are entirely the user's — do NOT automate or spec
The skill never auto-fetches, generates, hot-links, optimizes, sizes, specs, or invents an image
URL. For every image just leave its `[token]` (with correct responsive `<img>` styling). The user
sources, optimizes, and fills the real image herself. Only use an image URL she explicitly provides.

## Social links: text or icon
Both are valid — pick to match the style:
- **Text** (e.g. `Facebook · Instagram`) — lightest (0 images), always renders, never breaks.
  Default for **luxe / minimal / editorial** styles.
- **Icon images** — Suit **vibrant / playful** styles. Must be **PNG/GIF, never SVG** (Outlook
  won't render SVG). In her real pipeline (see her `code.txt`) the icon **image src is a FIXED
  self-hosted URL** reused across every email, and only the social **LINK href is a per-send
  token**. So: tokenize the link (`[facebook]`), and for the image leave `[icon_facebook]` (she
  swaps in her fixed icon URL) — or bake in her icon-set URL if she provides it. The icon set is
  generic infrastructure she already hosts, not per-client data.
- **Icon fonts / CDNs are OFF-LIMITS.** Font Awesome, W3.CSS, Google Material, etc. are icon
  *fonts* needing `<link>`/`<style>` (banned) — they render as empty boxes in email. "Use icons"
  means emitting `[icon_*]` **tokens only**; the agent never hotlinks an icon CDN or fetches an
  icon. She fills the tokens from her own hosted PNG set.
Default to ICON images (`[icon_*]` tokens — her convention; see SKILL rule 7). Use plain text links only for luxe/minimal styles or when she asks.
