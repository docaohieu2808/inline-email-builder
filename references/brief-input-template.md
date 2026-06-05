# Brief input form — email template

The user (or her teammate) fills what they know and leaves the rest blank. **Any blank field →
the AI auto-generates a sensible value that fits the rest of the brief.** Images/links not given
are left as `[tokens]` and listed under "still needed".

---

## FORM (copy, fill, send)

```
# BRIEF — EMAIL TEMPLATE
# Điền cái nào biết. Ô nào để TRỐNG → AI tự gen cho hợp.

## 1. Cơ bản
Ngành / chủ đề        :
Dịp / mục đích        :   (khuyến mãi · newsletter · sinh nhật · ra mắt · xác nhận đặt lịch · thông báo)
Ngôn ngữ              :   (VI / EN — trống = EN)
Tông giọng            :   (vui · sang · khẩn · nhẹ nhàng — trống = hợp dịp)

## 2. Thương hiệu
Tên thương hiệu       :
Logo (URL ảnh)        :   (trống = để token [logo])
Màu thương hiệu (hex) :   (vd #ff6f91, #66d0d0 — trống = AI chọn theo ngành)
Font ưu tiên          :   (web-safe thôi — trống = AI chọn)

## 3. Kiểu nhìn
Style / phong cách    :   (modern minimal · dark · sang trọng · khuyến mãi · cổ điển · bento — trống = AI chọn)
Layout / bố cục       :   (hero+ảnh-chữ · lưới menu · 1 cột · voucher — trống = AI chọn)
Có banner?            :   (có / không — trống = AI quyết)

## 4. Nội dung
Tiêu đề (headline)    :   (trống = AI viết)
Nội dung chính        :   (gạch ý hoặc đoạn — trống = AI viết theo dịp)
Nút CTA (chữ)         :   (vd "Đặt lịch ngay" — trống = AI đề xuất)
Link CTA (URL)        :   (trống = để token [cta_url])
Ưu đãi / mã (nếu có)  :   (vd "Giảm 20%, mã SPRING20")

## 5. Ảnh
Ảnh banner/sản phẩm   :   (mỗi dòng 1 URL https — trống = để token + AI ghi chú ảnh cần)

## 6. Link & chân trang
Website               :
Facebook              :
Instagram             :
YouTube / TikTok      :
Contact (địa chỉ/SĐT) :
Unsubscribe URL       :   (trống = để token [unsubscribe])

## 7. Ghi chú thêm
                      :   (bất cứ yêu cầu riêng gì)
```

---

## Worked example (partial fill → AI completes the rest)

```
Ngành / chủ đề        : nail / spa
Dịp / mục đích        : khuyến mãi mùa xuân
Tên thương hiệu       : Bloom Nails
Màu thương hiệu       : #ff6f91, #66d0d0
Style                 : modern minimal
Ưu đãi / mã           : giảm 15% tuần này
Instagram             : https://instagram.com/bloomnails
```
→ AI sinh: tiêu đề + nội dung tiếng Anh tông vui, layout hero tối giản, palette từ 2 màu cho,
nút pill "Book now", để token `[logo] [banner] [cta_url] [facebook] [youtube] [unsubscribe]`,
liệt kê ảnh cần (logo, 1 hero). Validate sạch trước khi trả.

## AI fill rules (when a field is blank)
- **Industry/occasion blank** → ask once if totally empty; otherwise infer from any given field.
- **Title/content blank** → write copy fitting industry + occasion + tone + language.
- **Style/layout blank** → choose a fresh combo per `modern-style.md` + `layout-patterns.md`;
  don't repeat the last design.
- **Colors/font blank** → pick per `theming-guide.md`.
- **Images/logo/links blank** → leave the matching `[token]`; collect them into a final
  "images needed" + "tokens left to fill" list. Never invent fake URLs.
- Always run `scripts/validate_email.py` and fix every ERROR before returning.
