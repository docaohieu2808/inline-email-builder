# Token contract

Two kinds of `[token]`. Keep the bracket syntax — it matches the team's existing merge pipeline.

## A. Theme tokens — the SKILL fills these with real values before returning
Replace with concrete hex/text during generation. They must NOT remain in final output.

| Token | Meaning | Example value |
|---|---|---|
| `[bg_page]` | page background behind the card | `#f4f4f4` |
| `[bg_card]` | card background | `#ffffff` |
| `[color_heading]` | heading / accent text color | `#66d0d0` |
| `[color_text]` | body text color | `#333333` |
| `[color_accent]` | CTA button background | `#ff6f91` |
| `[year]` | current year | `2026` |

## B. Merge tokens — LEAVE as-is unless the brief gives a concrete value
The backend (or the user) fills these per send. Fill them only when the brief supplies the value.

| Token | Meaning |
|---|---|
| `[preheader]` | hidden inbox preview text |
| `[logo]` | logo image URL (absolute) |
| `[domain]` | website / "view in browser" URL |
| `[name]` | business name |
| `[title]` | email headline |
| `[content]` | body HTML (paragraphs, lists — still inline-styled) |
| `[banner]` / `[banner_url]` / `[banner_alt]` | banner image src / link / alt |
| `[cta_text]` / `[cta_url]` | call-to-action label / link |
| `[facebook]` `[instagram]` `[youtube]` | social profile URLs |
| `[icon_website]` `[icon_facebook]` `[icon_instagram]` `[icon_youtube]` | social icon image URLs |
| `[contact]` | footer contact line (address/phone) |
| `[unsubscribe]` | unsubscribe URL |

## Rule of thumb
- Brief says "salon name is Bloom Nails, pink theme" → fill `[name]`, theme tokens, write copy.
- Brief does NOT give the Facebook URL → leave `[facebook]` for the pipeline.
- Always end the output with a short list: **tokens left to fill** + **images needed**.
