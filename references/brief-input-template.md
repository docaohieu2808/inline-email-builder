# Brief format — what she actually sends

She sends ONE compact prompt with these 8 fields. Fill what's known; **`tự viết` / blank → AI
generates** a fitting value. This is the real format — don't ask her to fill anything else.

```
Tạo một email template hoàn chỉnh cho chiến dịch sau:

Doanh nghiệp:          (tên thương hiệu)
Ngành nghề:            (→ tone + style lean — copywriting-rules / theming-guide)
Mục đích email:        (dịp: ra mắt · khuyến mãi · tri ân · newsletter · xác nhận…)
Đối tượng nhận email:  (khách mới · khách cũ · toàn bộ)
Thông điệp chính:      ("tự viết" = AI tự viết toàn bộ copy)
Ưu đãi hoặc CTA:       (vd "giảm 10% cho 1000 đơn đầu", hoặc kèm mã code)
Phong cách mong muốn:  (sang trọng · chuyên nghiệp · tối giản · rực rỡ · dark…)
Màu thương hiệu:       (vd "Xanh bầu trời" → palette dựng quanh màu này)

Hãy tự thiết kế nội dung, bố cục và cấu trúc email cho phù hợp.
```

## Cách đọc brief
- **Màu thương hiệu = GIVEN** → harmonize palette quanh nó; đừng tự chế màu khác.
- **Thông điệp "tự viết"** → tự viết toàn bộ copy (tiếng Việt đủ dấu, NFC).
- **Đối tượng** quyết góc copy: *khách mới* = chào mừng / đơn đầu tiên · *khách cũ* = tri ân / loyalty ·
  *toàn bộ* = thông điệp rộng, không nhắm 1 nhóm.
- **Mục đích + Phong cách** → chọn Layout + Style (`recommendations.md`), harmonize với Màu.
- Logo / ảnh / link KHÔNG có trong brief → để `[token]`, liệt kê ở cuối ("fill these").
- Mỗi brief = một thiết kế khác (anti-sameness) — đổi cấu trúc, đừng lặp mẫu lần trước.
- Luôn chạy `scripts/validate_email.py`, sửa hết ERROR trước khi trả.
