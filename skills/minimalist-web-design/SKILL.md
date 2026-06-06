---
name: minimalist-web-design
description: >
  Designs and reviews minimalist, editorial-feeling web interfaces to a 2026
  standard — distinctive layouts, extreme typographic hierarchy, restrained-but-bold
  color, strict performance budgets, and motion/SVG developer handoff. Use when
  designing a landing page or marketing site, auditing an existing design for
  generic "visual recycling," or preparing animated SVGs (e.g. GSAP DrawSVG) for
  developer handoff.
disable-model-invocation: true
---

<essential_principles>

**Principle 1: No Visual Recycling**
Never reach for the default SaaS/B2B template — a large hero image beside a vague headline and three feature cards. That layout signals "generic" before a word is read. The goal is unmistakable individuality and a handmade, editorial feel. If a layout could belong to any company in any industry, it has failed.

**Principle 2: Layered Borrowing, Never Copying**
Never clone a whole website. Decompose inspiration into four independent layers — **layout, typography, color, motion** — and borrow each deliberately and for a specific function. Combining well-chosen layers from different sources produces originality; copying one source whole produces a knockoff.

**Principle 3: Whitespace and One Concept per Screen**
Whitespace is an active design element, not leftover emptiness — it directs attention and lowers cognitive load. Spacing must be generous and consistent. Each viewport reduces to a single crystal-clear message; competing elements within one screen are a defect, not richness.

**Principle 4: Performance Is a Design Constraint**
Speed is a first-class design constraint, not a post-launch optimization. Target **LCP < 2.5s on mobile**. Every animation, font, image, and effect must justify its "performance cost" — if an element cannot prove its value against that cost, it is removed from the design, not deferred.

**Principle 5: Restraint Amplified by One Bold Move**
Limit to 2–3 typefaces and 2–3 primary colors. Break the restraint deliberately with extremes: oversized poster-scale headlines against small, perfectly legible body text; and high-saturation "dopamine" accent surfaces against an otherwise quiet palette. Restraint everywhere makes the one bold move land.

</essential_principles>

<intake>
**Ask the user which goal applies, then wait for the response:**

1. **Design** a new minimalist page or site (or produce a design spec)
2. **Audit** an existing page/design against the 2026 minimalist standard
3. **Prepare SVGs** for motion/animation developer handoff (GSAP DrawSVG, etc.)

If the user's intent is already explicit in their request, skip the question and route directly.
</intake>

<routing>
| Intent | Workflow |
|--------|----------|
| Design new page/site, "create a design", "spec a landing page" | `workflows/design-minimalist-page.md` |
| Review/critique existing design, "audit", "is this too generic" | `workflows/audit-design.md` |
| Prepare animated SVGs, "DrawSVG handoff", "stroke animation prep" | `workflows/prepare-svg-handoff.md` |

**After reading the workflow, follow it exactly.**
</routing>

<reference_index>
**Domain knowledge in `references/`:**

- **design-principles.md** — Core philosophy, dual moodboarding, layered borrowing, whitespace and one-concept-per-screen, asymmetric/editorial/brutalist composition, extreme typographic hierarchy, font limitation, maximalist/dopamine color systems, and asset rules (no stock, WebP/AVIF, video).
- **performance-and-svg.md** — Performance-first mindset, LCP budget, per-element performance-cost calculus, video/WebGL guidance, image optimization, and the full SVG-for-motion preparation rationale.
</reference_index>

<workflows_index>
| Workflow | Purpose |
|----------|---------|
| design-minimalist-page.md | Full procedure: dual moodboard → layout → type → color → assets → performance budget |
| audit-design.md | Review an existing design against the standard and produce prioritized findings |
| prepare-svg-handoff.md | Prepare stroke-based SVGs with stable IDs for scroll/motion animation |
</workflows_index>

<success_criteria>
A design produced or reviewed with this skill:
- [ ] Avoids the generic hero + three-feature-card template; reads as individual/editorial
- [ ] Borrows inspiration by isolated layer (layout/type/color/motion), never wholesale
- [ ] Uses generous, consistent whitespace and one concept per viewport
- [ ] Limits to 2–3 typefaces and 2–3 primary colors, with deliberate scale and accent extremes
- [ ] Uses no stock photography; assets shipped as WebP/AVIF at native dimensions
- [ ] Meets the mobile LCP < 2.5s budget, with every element justifying its performance cost
- [ ] (If applicable) Ships motion SVGs as clean strokes-only paths with stable IDs and consistent stroke-width
</success_criteria>
