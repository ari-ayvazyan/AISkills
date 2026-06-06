# Workflow: Audit a Design Against the 2026 Minimalist Standard

<required_reading>
**Read these reference files NOW:**
1. references/design-principles.md
2. references/performance-and-svg.md
</required_reading>

<process>

## Step 1: Gather the Target

Obtain what you are auditing: a live URL, screenshots, a design file, or the rendered code in the codebase. If reviewing code, locate the relevant components, stylesheets, and asset files.

## Step 2: Run the Checklist

Evaluate against each criterion. For every issue, record **severity** (Critical / Major / Minor) and a concrete fix.

**1. Visual recycling**
- Is this the generic hero + vague headline + three feature cards template?
- Could this layout belong to any company in any industry? (If yes → Critical.)
- Does it feel handmade/editorial, or off-the-shelf?

**2. Composition & whitespace**
- Is whitespace generous and consistent, or cramped/uneven?
- Does each viewport carry exactly one clear concept, or compete for attention?
- Is there intentional tension (asymmetry / F / Z / triangular / brutalist), or a flat predictable grid?

**3. Typography**
- 2–3 typeface families max? Clean modern sans-serifs?
- Drastic scale contrast between headline and body, or a timid even scale?
- Is body text perfectly legible?

**4. Color discipline**
- 2–3 primary colors max?
- Are accents bold/saturated dopamine hues used surgically, or muddy gradients everywhere?

**5. Assets**
- Any stock photography? (Flag it.)
- Heavy background `.mp4`? (Flag — recommend `.webm` or WebGL.)
- Images in WebP/AVIF and sized to native display dimensions?

**6. Performance budget**
- Estimated/measured **LCP < 2.5s on mobile**?
- Does every animation, font, and graphic justify its performance cost? Identify elements to cut.

## Step 3: Produce Prioritized Findings

Output a findings list grouped by severity:

```
## Design Audit — [target]

### Critical
- [Finding] → [Fix]

### Major
- [Finding] → [Fix]

### Minor
- [Finding] → [Fix]

### Verdict
[One line: does it meet the 2026 minimalist standard? What is the single highest-impact change?]
```

</process>

<success_criteria>
- [ ] All six criterion groups evaluated (recycling, composition, type, color, assets, performance)
- [ ] Each finding has a severity and a concrete fix
- [ ] LCP / performance cost assessed, not skipped
- [ ] A clear verdict and single highest-impact recommendation given
</success_criteria>
