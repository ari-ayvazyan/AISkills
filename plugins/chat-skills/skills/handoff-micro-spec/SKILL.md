---
name: micro-spec
description: Turn a project idea into a minimal, on-point SPEC.md (caveman style — least text, max info). Use when the user runs /micro-spec or asks to spec out / document a project idea.
disable-model-invocation: true
---

# micro-spec

Turn the idea in the args into `./SPEC.md`. **Overwrite** it. Then show the user a 2-line summary of what was written + assumptions made.

## Prime directive
Dump every decision **already** made, minimally. No wall of text. No blabla, hedging, or restating the obvious. The implementer fills in the rest — write only what they can't infer.

## Voice
- Bullets > prose. One line per point.
- Use the arrow form for flows: `input → output`.
- Bold the load-bearing words only.
- If a sentence survives deletion without info loss, delete it.

## Sections (in order)

1. `# <Name> — Spec` — derive a short name from the idea.
2. `## Goal` — **one** sentence: what it does, arrow form, key constraints inline.
3. `## Constraints` — hard rules as bullets (I/O formats, must/never). Skip if none.
4. `## Architecture` — **only if data flows between ≥2 components.** ASCII box diagram, then 2–3 bullets: boundaries, what's external, what's persisted vs. transient. Skip entirely for a single script/function.
5. `## Phases` — numbered **one-liners**, each with an exit criterion (e.g. `test_x green`). Skip if not a build-it-in-stages effort.
6. `## Open items` — unknowns / deferred decisions as bullets.

Separate major sections with `---` (as in the reference).

## Gaps → defaults
For anything the user did **not** specify, pick a sensible default and **mark it** — append ` *(assumed)*` to that bullet. Never silently invent; never leave a needed field blank. Genuine unknowns (no reasonable default) go to **Open items** as a question instead.

## Reference output
This is the target style and density — match it, don't copy its content:

```markdown
# Gemini Watermark Remover — Spec

## Goal
Web app: upload Gemini-generated PNG → return PNG, visually identical, with **(1)** visible Gemini watermark removed and **(2)** SynthID watermark removed.

## Constraints
- Input/output: PNG only
- Output pixels match source except watermark regions
- Verification = Gemini API reports **no SynthID** on output

---

## Architecture
\`\`\`
┌─────────┐   PNG    ┌────────────────┐   PNG   ┌──────────┐
│ Browser │ ───────▶ │  Web Backend   │ ──────▶ │ Browser  │
│ (upload)│ ◀─────── │ (process API)  │         │(download)│
└─────────┘  result  └────────────────┘         └──────────┘
\`\`\`
- Browser ↔ Backend: PNG over HTTP
- Backend ↔ Gemini API: external, key-gated, verify-only
- Data at rest: test fixtures only; runtime uploads never persisted

---

## Phases
1. **Website** — upload form + `POST /process` (PNG in → PNG out), stub passes through
2. **Test data** — 10 pairs + failing tests `test_pixels_match`, `test_synthid_absent`
3. **Visible removal** — `test_pixels_match` green
4. **SynthID removal** — `test_synthid_absent` green

---

## Open items
- Gemini API endpoint/key for SynthID detection
- `test_pixels_match` tolerance: exact vs. perceptual
```

## After writing
Reply with: file path + one line listing each `*(assumed)*` default, so the user can correct them.
