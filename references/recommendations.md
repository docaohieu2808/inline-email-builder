# Recommendation engine — suggest the FRAME's Style + look

The agent is a **consultant, not a menu**. Read the brief, **proactively recommend a Style + frame
treatment** (header / banner / footer / colour) with a one-line reason; she accepts or tweaks. The
skill designs the FRAME only — the body is `[content]` (she fills), so there's no body "layout" to pick.

## Two kinds of input
- **GIVEN (brand property, not chosen per email):** industry, brand colours. Context — never ask her
  to pick "by colour/industry". Harmonize the frame with her colour; don't invent a palette.
- **VARIABLE (per email):** occasion + campaign → drive the Style + frame treatment.

## Occasion → Style lean
| Dịp | Style |
|---|---|
| Khai trương / Ra mắt | Rực rỡ · Dark · Tạp chí |
| Sinh nhật khách | Tối giản · Duotone pastel |
| Sale / giảm giá | Rực rỡ · Dark |
| Bản tin định kỳ | Tối giản · Tạp chí |
| Tri ân / cảm ơn | Luxe · Tối giản |
| Mời sự kiện | Tạp chí · Dark |
| Xác nhận đặt lịch / đơn | Tối giản · Cổ điển |

## Industry → style lean (context)
| Ngành | Lean |
|---|---|
| Nail / Spa / Beauty | Luxe · Tối giản |
| Nhà hàng / F&B | Rực rỡ · Tạp chí |
| Thời trang / Retail | Tạp chí · Dark · Duotone |
| Fitness / Gym | Dark · Rực rỡ |
| Mỹ phẩm | Luxe · Duotone |
| Tech / SaaS | Tối giản · Dark |
| Giáo dục | Tối giản · Rực rỡ |
| BĐS / Cao cấp | Luxe · Tạp chí |

## Vary the LAYOUT each time (avoid a templated shell)
Two emails of the same occasion must NOT use the same layout. Vary (see `layout-patterns.md`):
- **Logo position** — left · centred · with a tagline · right · in a coloured header band.
- **Banner** — include `[banner]` (launch/promo/showcase) or skip (plain/transactional).
- **Image block** — none · 2-across · 2×2 grid · 2-stacked+text (left or right) · 1 hero.
- **Footer + social** — text row · icon row (`[icon_*]`) · "Theo dõi:" label · in the header · minimal vs full.
Recolouring the same shell is NOT enough — change the layout (logo / banner / image block / footer).

## How to recommend (agent behavior)
1. From the brief: industry + brand colours (GIVEN), occasion + campaign (VARIABLE).
2. Pick a Style + a frame treatment you have NOT just used; harmonize with the brand colour.
3. Say it in Vietnamese, short, with the reason + an out:
   > "Mình đề xuất **frame Luxe**: logo giữa + tagline, footer hairline, tông hồng–gold. OK không?"
4. She accepts / tweaks / names her own — then build. Text stays `[title]` + `[content]`.
