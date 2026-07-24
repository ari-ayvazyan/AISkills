---
name: color-architect
description: Generates strategic color palettes. Use when creating or updating app color schemes, theming, or brand colors.
disable-model-invocation: true
---

<essential_principles>

**Principle 1: Color is Psychology, Not Preference**
Color selection must align with the app's purpose and target audience. A fintech app requires trust (blues), a wellness app needs calm (greens/lavenders), an e-commerce site demands urgency (strategic reds). Never select colors purely on aesthetics.

**Principle 2: The 60-30-10 Distribution Rule**
- **60% Dominant**: Backgrounds, large sections (typically neutrals)
- **30% Secondary**: Navigation, sidebars, cards (brand support)
- **10% Accent**: CTAs, active states, focus indicators (high contrast, attention-grabbing)

**Principle 3: Accessibility is Non-Negotiable**
All color combinations must meet WCAG 2.1 AA standards:
- Normal text: 4.5:1 contrast ratio minimum
- Large text (>18pt): 3:1 minimum
- UI components (borders, focus rings): 3:1 minimum
- Never rely on color alone to convey meaning

**Principle 4: Light and Dark Mode Parity**
Both modes must maintain the same emotional impact and accessibility standards. Dark mode is NOT simple inversion—it requires:
- Reduced saturation to prevent eye strain
- Progressive lightening for elevation (surfaces closer = lighter)
- Re-tested contrast ratios

**Principle 5: Always Research Before Applying**
Theme locations vary by framework:
- Tailwind/shadcn: `globals.css` with CSS variables
- Material UI: `theme.ts` or `createTheme()`
- Chakra UI: `theme.ts` with `extendTheme()`
- Plain CSS: Various stylesheet locations
- **Always search the codebase first** to find where colors are defined

</essential_principles>

<intake>
**Before proceeding, gather project context:**

1. Search for existing theme/color configuration in the codebase
2. Look for README.md or project description files
3. Identify the styling framework (Tailwind, MUI, Chakra, CSS-in-JS, etc.)

**Then ask if any critical info is missing:**
- What is the app's primary purpose/industry?
- Who is the target audience?
- Are there existing brand colors that must be preserved?

**Wait for user response if questions are needed. Otherwise proceed to workflow.**
</intake>

<routing>
| Intent | Workflow |
|--------|----------|
| Generate/apply colors, "create theme", "pick colors" | `workflows/generate-colors.md` |
| Analyze existing colors, "audit theme" | `workflows/generate-colors.md` (audit mode) |

**After reading the workflow, follow it exactly.**
</routing>

<reference_index>
**Domain knowledge in `references/`:**

**Color Science & Strategy**: color-theory-guide.md
- Perceptual color spaces (HCT, LCH, OKLCH)
- Psychological color mapping by industry
- Harmonic relationships (complementary, analogous, triadic)
- 2025 design trends
- WCAG accessibility requirements
- Token architecture patterns
</reference_index>

<workflows_index>
| Workflow | Purpose |
|----------|---------|
| generate-colors.md | Full workflow: analyze project → gather requirements → generate palette → apply to theme |
</workflows_index>

<success_criteria>
Color architecture is complete when:
- [ ] Project purpose and audience understood
- [ ] Existing theme location identified
- [ ] Primary, secondary, and accent colors selected with psychological rationale
- [ ] Neutral scale generated (not pure gray—tinted for brand cohesion)
- [ ] Semantic colors defined (success, warning, error, info)
- [ ] Both light and dark mode variants created
- [ ] All combinations pass WCAG AA contrast checks
- [ ] Colors applied to correct theme configuration file
</success_criteria>
