# Brief format — what she actually sends

She sends ONE compact prompt with these 8 fields. **The skill designs the FRAME and leaves the
message as `[title]` + `[content]` tokens — it does NOT write copy** (see SKILL "Your job = the
FRAME, not the words"). Blank style/layout fields → auto-pick a fitting one.

```
Tạo một email template hoàn chỉnh cho chiến dịch sau:

Doanh nghiệp:          (tên thương hiệu)
Ngành nghề:            (→ style lean cho frame — theming-guide)
Mục đích email:        (dịp: ra mắt · khuyến mãi · tri ân · newsletter · xác nhận…)
Đối tượng nhận email:  (khách mới · khách cũ · toàn bộ)
Thông điệp chính:      (chỉ tham khảo bối cảnh — KHÔNG gen; thân email là token [content])
Ưu đãi hoặc CTA:       (vd "giảm 10% cho 1000 đơn đầu", hoặc kèm mã code)
Phong cách mong muốn:  (sang trọng · chuyên nghiệp · tối giản · rực rỡ · dark…)
Màu thương hiệu:       (vd "Xanh bầu trời" → palette dựng quanh màu này)

Hãy tự thiết kế nội dung, bố cục và cấu trúc email cho phù hợp.
```

## Cách đọc brief
- **Màu thương hiệu = GIVEN** → harmonize palette quanh nó; đừng tự chế màu khác.
- **Thông điệp / Ưu đãi** → chỉ là bối cảnh; **KHÔNG gen chữ**. Thân email luôn là token `[content]`.
- **Đối tượng / Mục đích** → ảnh hưởng **tông THIẾT KẾ** (tri ân → luxe, sale → rực rỡ), không phải chữ.
- **Banner = optional** — chèn `[banner]` (ảnh foreground) cho ra mắt / khuyến mãi / showcase; bỏ cho
  mail tối giản / giao dịch. Cô ấy thêm/xoá được.
- **Mục đích + Phong cách** → chọn Layout + Style frame (`recommendations.md`), harmonize với Màu.
- Logo / ảnh / link KHÔNG có trong brief → để `[token]`, liệt kê ở cuối ("fill these").
- Mỗi brief = một thiết kế khác (anti-sameness) — đổi cấu trúc, đừng lặp mẫu lần trước.
- Luôn chạy `scripts/validate_email.py`, sửa hết ERROR trước khi trả.
