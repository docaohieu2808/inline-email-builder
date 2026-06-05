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
inline. Use the **fluid inline-block wrap** ("media object") in `templates/blocks/media-row.html`:
- Parent `font-size:0; text-align:center;` (kills inline-block whitespace gap).
- Each column `display:inline-block; width:100%; max-width:300px; vertical-align:top;` and
  resets its own `font-size`. The two column divs MUST be adjacent (no whitespace between them).
- Wide container (≥ ~600px) → both 300px columns sit side by side. Narrow (mobile) → each is
  100% → they wrap to stacked, in source order (put the image column first for image-on-top).
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
**Write it so the fallback colour SURVIVES — this is the part that's easy to get wrong:**
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
- Use web-safe font stacks (Arial/Helvetica, Georgia, Tahoma, Verdana). Custom web fonts need
  `<style>`/`@font-face` → not allowed here; pick a web-safe stack instead.
- **Set `font-family` inline on EVERY text element** (`<h1>`, `<p>`, `<a>`, text `<div>`) — do NOT
  rely on inheritance from a parent wrapper. Outlook and several clients RESET font-family on
  `<h1>`/`<p>`/`<td>` to **Times New Roman**, breaking the look (it renders fine in a browser, but
  wrong in the inbox). Repeat the same stack on each text node. Styled `<div>`s inherit a bit more
  reliably than `<h1>`/`<p>`, but still set the family explicitly to be safe.

## 6. Accessibility & deliverability
- Contrast ≥ 4.5:1 for body text.
- Real `alt` text, logical reading order.
- Always include an `[unsubscribe]` link (legal requirement for marketing email).

## Client support target
Modern clients first (Gmail web/app, Apple Mail, Outlook.com, iOS/Android mail). The div-based
fluid approach is intentional. NOTE: legacy **Outlook desktop (Word engine)** ignores `max-width`
and `box-shadow` and may render full-width — acceptable per the existing template's choices. If
strict Outlook-desktop parity is ever required, that needs table-based layout + VML (out of scope;
raise it before adding).

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
Default to text; use icons (as tokens) when the style calls for it or the user asks.
