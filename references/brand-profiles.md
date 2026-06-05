# Brand profiles (reuse per-client constants)

A brand profile saves the things that **never change for a client** — logo, colors, social
links, contact, website, unsubscribe URL — so they aren't re-typed every email. Built to hold
**many profiles** (one per client); a single-brand user just keeps one.

## Where they live (privacy)
`brand-profiles/<slug>.json` next to this skill. **Real profiles are gitignored** — they hold a
client's URLs, never committed/pushed. Only `brand-profiles/EXAMPLE.json` ships as a template.
Override the location with env `EMAIL_BRAND_PROFILES_DIR` if you keep them elsewhere.

## Profile format (`brand-profiles/bloom-nails.json`)
```json
{
  "name": "Bloom Nails",
  "logo": "https://cdn.../bloom-logo.png",
  "domain": "https://bloomnails.com",
  "colors": { "accent": "#ff6f91", "heading": "#66d0d0", "text": "#333333",
              "bg_page": "#fef6f8", "bg_card": "#ffffff" },
  "facebook": "https://facebook.com/bloomnails",
  "instagram": "https://instagram.com/bloomnails",
  "youtube": "https://youtube.com/@bloomnails",
  "contact": "123 Blossom Ave · (555) 012-3456",
  "unsubscribe": "https://bloomnails.com/unsubscribe"
}
```
Any field may be omitted → it stays a `[token]`. Token mapping: `name→[name]`, `logo→[logo]`,
`domain→[domain]`, `facebook/instagram/youtube→[..]`, `contact→[contact]`,
`unsubscribe→[unsubscribe]`, and `colors.accent→[color_accent]`, `colors.heading→[color_heading]`,
`colors.text→[color_text]`, `colors.bg_page→[bg_page]`, `colors.bg_card→[bg_card]`.

## How the skill uses it
Nothing is hardcoded — profiles are discovered at runtime, any slug works.
1. The brief names a brand. Run `scripts/brand_profile.py list` to see the actual saved profiles
   and pick the one matching that brand (slug = brand name lowercased, spaces → hyphens; e.g.
   "Bloom Nails" → `bloom-nails`, "Tiệm Nail ABC" → `tiem-nail-abc`).
2. If a match exists, load it (`show <slug>`) and **pre-fill** those tokens; the brand's colors
   seed the theme. Only the per-email parts (occasion, copy, purchased image) are new.
3. If no match, proceed normally (auto-gen / leave tokens) and offer to save a profile for next time.

## Managing profiles (helper script)
```bash
cd <this-skill-directory>
python3 scripts/brand_profile.py list                 # list saved brands
python3 scripts/brand_profile.py new bloom-nails      # scaffold from EXAMPLE, then edit it
python3 scripts/brand_profile.py show bloom-nails     # see flattened token values
python3 scripts/brand_profile.py apply bloom-nails out.html   # fill [tokens] in a fragment
```

## Still manual (never in a profile)
Purchased images (per-email, priced individually) and the per-email copy/occasion. Profiles hold
only the stable brand constants.
