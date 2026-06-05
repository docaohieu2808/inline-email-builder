# Recommendation engine — auto-suggest Layout + Style

The agent is a **consultant, not a menu**. Don't make her pick by name. Read the brief, then
**proactively recommend a Layout + Style** with a one-line reason, and let her accept or tweak.

## Two kinds of input
- **GIVEN (a property of the brand — already known, never "chosen" per email):** industry, brand
  colors / vibe. Use them as context; do NOT ask her to pick a style "by color" or "by industry".
  Brand colors are hers (filled in code) — harmonize the design with them, don't invent a palette.
- **VARIABLE (changes each email — this is what you actually decide around):** occasion, campaign.

So: `(given industry + brand colors) + (this email's occasion/campaign) → recommend Layout + Style`.

Layout codes L1–L7 and Style codes S1–S8 are defined in `picker-layout-style.md`.

## A. Occasion → Layout + Style  (primary driver)
| Dịp | Layout | Style |
|---|---|---|
| Khai trương | L1 Hero / L3 Voucher | S4 Rực rỡ / S3 Luxe |
| Sinh nhật khách | L1 Hero | S1 Tối giản / S6 Duotone pastel |
| Sale / giảm giá | L3 Voucher | S4 Rực rỡ / S2 Dark |
| Bản tin định kỳ | L5 Bản tin | S1 Tối giản / S5 Tạp chí |
| Ra mắt SP / BST | L1 Hero / L4 Lưới | S5 Tạp chí / S2 Dark |
| Tri ân / cảm ơn | L2 Một cột | S3 Luxe / S1 Tối giản |
| Mời sự kiện | L2 Một cột | S5 Tạp chí / S2 Dark |
| Xác nhận đặt lịch / đơn | L6 Receipt | S1 Tối giản / S8 Cổ điển |
| Mời quay lại (re-engage) | L7 Thư đơn / L1 Hero | S1 Tối giản |

## B. Campaign → Layout + Style  (primary driver)
| Chiến dịch | Layout | Style |
|---|---|---|
| Khuyến mãi (acquisition) | L3 Voucher | S4 Rực rỡ / S2 Dark |
| Nuôi dưỡng / bản tin (nurture) | L5 Bản tin | S1 Tối giản / S5 Tạp chí |
| Ra mắt (launch) | L1 Hero | S2 Dark / S5 Tạp chí |
| Tri ân / giữ chân (retention) | L2 Một cột | S3 Luxe / S1 Tối giản |
| Mời sự kiện (event) | L2 Một cột / L1 Hero | S5 Tạp chí / S2 Dark |
| Giao dịch (transactional) | L6 Receipt | S1 Tối giản / S8 Cổ điển |

## C. Industry → style/palette LEAN  (context, not a choice — already given)
Use to refine the style picked from A/B so it fits the trade. (Palettes per industry live in
`theming-guide.md`; but the brand's own colour is given — harmonize with that first.)
| Ngành | Style lean |
|---|---|
| Nail / Spa / Beauty | Luxe · Tối giản |
| Nhà hàng / F&B | Rực rỡ · Tạp chí |
| Thời trang / Retail | Tạp chí · Dark · Duotone |
| Fitness / Gym | Dark · Rực rỡ |
| Mỹ phẩm | Luxe · Duotone |
| Tech / SaaS | Tối giản · Dark |
| Giáo dục | Tối giản · Rực rỡ |
| BĐS / Cao cấp | Luxe · Tạp chí |

## Vary even within the SAME occasion (avoid sameness — CRITICAL)
Two emails of the same occasion (e.g. two promos) must NOT come out with the same structure. Each
occasion has SEVERAL valid compositions — rotate them; don't reuse one component recipe. For a
**promo**, pick a *different* one each time:
- **Hero + benefit list + offer box** (service-led).
- **Product grid / catalog** — 2×N products, each image + name + price/discount (when the brand sells products).
- **Single giant offer** — minimal: logo + huge "30% OFF" + one line + CTA.
- **Featured product / bundle** — one hero product + a couple of specs + offer.
- **Voucher-code centric** — big dashed code box.

> **ANTI-PATTERN (the trap):** do NOT default to *eyebrow → headline → 3 `✓` → tinted offer box →
> CTA* for every promo. That recipe is ONE option, not THE template. Change the composition each
> time — vary section count, benefit-list vs product-grid vs testimonial, hero vs no-hero, where the
> offer sits, centred vs left. Colour + copy changing is NOT enough; the **structure** must differ.

### Vary the HEADER & FOOTER too — not just the body
Don't let *logo top-left + a separate social-link footer* harden into a fixed shell. The body is
not the only place to differ:
- **Logo placement** — left, **centred**, with a tagline under it, or inside a coloured header band.
- **Header treatment** — plain logo · logo + a thin "view online" link on the right · a coloured
  brand band · logo + a one-line value strip.
- **Social** — a row of icons · text links · **placed in the header** instead of the footer · omitted
  on minimal/transactional emails.
- **Footer richness** — minimal (just contact + unsubscribe) vs fuller (tagline + social + address).
Keep the *required* footer content (**unsubscribe + contact**) every time — only its treatment and
placement vary. (E.g. a luxe email might centre the logo with a tagline + a hairline footer; a
promo might left-align the logo with a bold header band and an icon-row footer.)

## How to recommend (agent behavior)
1. From the brief get: industry + brand colors (GIVEN) and occasion + campaign (VARIABLE).
2. Pick Layout + Style from A/B, then nudge the style with C and harmonize with the brand colors.
   Deliberately pick a composition you have NOT just used (see "Vary even within the same occasion").
3. Say it in Vietnamese, short, with the reason + an out:
   > "Mình đề xuất **Hero + Luxe**, tông hồng–gold (hợp nail + khai trương sang). OK không, hay đổi?"
4. She accepts, tweaks ("tối giản hơn đi"), or names her own — then build. If she gave nothing to
   go on, ask only the occasion.
