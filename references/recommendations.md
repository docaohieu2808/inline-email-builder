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
Use to refine the style picked from A/B so it fits the trade.
| Ngành | Style lean | Tông màu hay gặp |
|---|---|---|
| Nail / Spa / Beauty | Luxe · Tối giản | hồng pastel, teal, gold |
| Nhà hàng / F&B | Rực rỡ · Tạp chí | terracotta, đỏ, kem |
| Thời trang / Retail | Tạp chí · Dark · Duotone | đen-trắng, gold |
| Fitness / Gym | Dark · Rực rỡ | xanh lá, cam, đen |
| Mỹ phẩm | Luxe · Duotone | mauve, hồng |
| Tech / SaaS | Tối giản · Dark | xanh dương, tím |
| Giáo dục | Tối giản · Rực rỡ | xanh, vàng |
| BĐS / Cao cấp | Luxe · Tạp chí | đen, gold, navy |

## How to recommend (agent behavior)
1. From the brief get: industry + brand colors (GIVEN) and occasion + campaign (VARIABLE).
2. Pick Layout + Style from A/B, then nudge the style with C and harmonize with the brand colors.
3. Say it in Vietnamese, short, with the reason + an out:
   > "Mình đề xuất **Hero + Luxe**, tông hồng–gold (hợp nail + khai trương sang). OK không, hay đổi?"
4. She accepts, tweaks ("tối giản hơn đi"), or names her own — then build. If she gave nothing to
   go on, ask only the occasion.
