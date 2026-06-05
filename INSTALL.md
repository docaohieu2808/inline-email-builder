# Cài đặt — inline-email-builder

Skill này chạy trong một AI coding agent (Codex CLI hoặc Claude Code). Cài 1 lần, dùng mãi.

## Bước 1 — Cài agent (chọn 1)

- **Codex CLI** (OpenAI): cần tài khoản ChatGPT (Plus/Pro) hoặc API key.
  Cài theo hướng dẫn chính thức của OpenAI Codex, rồi đăng nhập.
- **Claude Code** (Anthropic): cần tài khoản Claude hoặc API key.
  `npm install -g @anthropic-ai/claude-code` rồi chạy `claude` để đăng nhập.

> Chỉ cần 1 trong 2. Skill viết theo chuẩn chung nên chạy được cả hai.

## Bước 2 — Cài skill (clone vào thư mục skills của agent)

**Codex CLI:**
```bash
git clone https://github.com/docaohieu2808/inline-email-builder.git \
  ~/.codex/skills/inline-email-builder
```

**Claude Code:**
```bash
git clone https://github.com/docaohieu2808/inline-email-builder.git \
  ~/.claude/skills/inline-email-builder
```

Cập nhật về sau:
```bash
cd ~/.codex/skills/inline-email-builder   # hoặc ~/.claude/...
git pull
```

## Bước 3 — Kiểm tra Python (cho bộ validate)

Cần `python3` (đa số máy có sẵn). Test:
```bash
cd ~/.codex/skills/inline-email-builder   # hoặc ~/.claude/...
python3 scripts/validate_email.py templates/examples/archetype-a-hero-media-rows.html
# kỳ vọng: "0 error(s)"
```

## Bước 4 — Dùng

Mở agent (gõ `codex` hoặc `claude` trong terminal) rồi gõ yêu cầu bằng lời thường, ví dụ:

> Làm email nail, khuyến mãi mùa xuân, brand Bloom Nails màu hồng, style modern minimal.

Agent tự nạp skill, sinh email HTML + danh sách "ảnh/token còn thiếu".
Muốn kỹ hơn thì điền form trong `references/brief-input-template.md` rồi dán vào.

Ô nào không nhập → AI tự gen. Ảnh/link không đưa → để token `[...]`, không bịa URL.
