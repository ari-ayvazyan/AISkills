# Workflow: Design a Minimalist Page or Site

<required_reading>
**Read these reference files NOW:**
1. references/design-principles.md
2. references/performance-and-svg.md
</required_reading>

<process>

## Step 1: Dual Moodboarding (Strictly Separated)

Split research into two distinct boards. Do not mix them — they answer different questions.

- **"Feel" moodboard** — aesthetics, typography, atmosphere, originality.
  Sources: **Awwwards**, **Site Inspire**.
- **"Performance" moodboard** — conversion, proven UI patterns, flows that work.
  Sources: **Mobbin**, **Land-book**.

For each saved reference, note *which layer* you are borrowing (layout / typography / color / motion) and *why* — never "the whole site."

## Step 2: Choose a Layout Strategy

Reject the generic SaaS template (big hero + vague headline + three feature cards). Pick a composition that creates tension and individuality:

- **Asymmetric grid** — off-balance columns, deliberate weight on one side
- **F-pattern / Z-pattern** — guide the eye along a known reading path
- **Triangular composition** — three anchor points forming visual movement
- **Brutalist minimalism** — raw, heavily grid-based, visible edges, content over decoration

Apply **one concept per viewport** — each screen carries a single clear message. Make whitespace generous and consistent; treat it as an active element directing attention.

## Step 3: Define Typographic Hierarchy

- Limit to **2–3 typeface families**, favor modern, very clean sans-serifs.
- Use **drastic scale jumps**: oversized, poster-like ("oversized") headlines in direct contrast to small, perfectly legible body text. Avoid timid, evenly-stepped type scales — the contrast *is* the design.

## Step 4: Color Strategy

- Limit to **2–3 primary colors**.
- Break the reduced aesthetic with **maximalist color systems / dopamine hues** — high-saturation, almost garish colors reserved for specific accent surfaces. Prefer these punchy accent blocks over soft, classic gradients.
- (If a full palette is needed, the `color-architect` skill can generate one within these constraints.)

## Step 5: Asset Rules

- **No stock photography.** Use authentic, professional images or purpose-built custom illustrations that reinforce brand character.
- **Video:** avoid heavy background `.mp4`. Use lightweight `.webm`, or generate backgrounds programmatically via WebGL (e.g. animated Bayer dithering).
- **Images:** optimize losslessly to **WebP** or **AVIF**, and serve at the exact native display dimensions.

## Step 6: Performance Budget Check

For every element decided above, calculate its **performance cost**. Each animation, font, and graphic must prove its value or be cut.

- Target: **LCP < 2.5s on mobile.**
- If anything endangers that budget without clear value, remove it now — do not "optimize later."

## Step 7: Deliver

Produce the design (or a written spec) capturing: layout strategy, type pairing + scale, color set + accent usage, asset plan, and the performance budget with per-element justifications.

</process>

<success_criteria>
- [ ] Two separate moodboards created ("Feel" + "Performance") with per-layer borrowing notes
- [ ] Layout avoids the generic template and uses an intentional composition
- [ ] One concept per viewport; whitespace generous and consistent
- [ ] 2–3 typefaces with drastic headline/body scale contrast
- [ ] 2–3 primary colors plus deliberate dopamine-hue accents
- [ ] No stock photos; assets planned as WebP/AVIF at native size; video as .webm/WebGL
- [ ] Every element has a justified performance cost; mobile LCP < 2.5s targeted
</success_criteria>
