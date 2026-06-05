# inline-email-builder

A Claude/Codex **Agent Skill** that turns a short brief into a production-ready **email HTML
fragment** — inline CSS only, no `<style>`/`<head>`/`<html>`, mobile-responsive without media
queries, compatible with `[token]` merge pipelines.

It is a **framework, not a fixed template**: every request produces a fresh design. Two
independent dials — **layout** (7 archetypes) × **style** (modern minimal, dark, editorial,
duotone…) — so two emails never look the same. Blank brief fields are auto-generated; images and
links you don't provide are left as `[tokens]` and listed as "still needed" (no fake URLs).

## Install

See [INSTALL.md](INSTALL.md). Quick version (Codex):
```bash
git clone https://github.com/docaohieu2808/inline-email-builder.git ~/.codex/skills/inline-email-builder
```
(Claude Code: clone into `~/.claude/skills/inline-email-builder` instead.)

## Use

In the agent, just describe what you want:
> Làm email nail, khuyến mãi mùa xuân, brand Bloom Nails màu hồng, style modern minimal.

Or fill the form in `references/brief-input-template.md` for precise control.

## What's inside

| Path | Purpose |
|---|---|
| `SKILL.md` | entry point — rules, workflow, token contract |
| `references/email-html-rules.md` | the hard constraints + why (inline-only, fluid responsive, image rules) |
| `references/layout-patterns.md` | 7 layout archetypes (A–G) to remix |
| `references/modern-style.md` | modern look guidance (whitespace, big type, pill buttons, dark mode) |
| `references/theming-guide.md` | palette + web-safe font per industry |
| `references/brief-input-template.md` | the fill-in brief form |
| `references/tokens.md` | merge-token contract |
| `templates/` | base skeleton + blocks (banner, CTA, media-row) + 4 example designs |
| `scripts/validate_email.py` | dependency-free linter (fails on forbidden tags / non-https img / unfilled theme tokens) |
| `scripts/fill_tokens.py` | merge a JSON of token values into a fragment |

## The one constraint

Custom brand web-fonts need `<style>`/`@font-face`, which the inline-only pipeline bans → use a
web-safe stack. Everything else (modern layouts, dark mode, responsive multi-column) works inline.

MIT.
