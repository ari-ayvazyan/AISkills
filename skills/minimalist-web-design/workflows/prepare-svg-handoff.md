# Workflow: Prepare SVGs for Motion/Animation Handoff

<required_reading>
**Read this reference file NOW:**
1. references/performance-and-svg.md
</required_reading>

<objective>
When minimalist lines or icons must be animated on scroll (e.g. with **GSAP DrawSVG**), the SVG must be prepared by design in a specific way. A path that has fills, excess anchor points, or no stable ID cannot be cleanly animated. This workflow enforces the handoff requirements.
</objective>

<process>

## Step 1: Strokes Only — No Fills

The artwork must consist purely of **path outlines (strokes)**, with **no filled areas (fills)**. DrawSVG-style animation draws a stroke along its length; a `fill` has nothing to draw. Convert any filled shapes to outlined strokes before export.

## Step 2: Reduce Anchor Points

Every unnecessary anchor point costs CPU during animation. Simplify the vector paths drastically — keep only the anchors needed to hold the shape.

## Step 3: Clean Export

Strip everything that isn't the path. On export, remove all empty groups, clipping masks, and metadata. Use a tool like **SVGOMG** to produce minimal, clean output.

## Step 4: Assign a Stable ID

Give the exact path to be animated a unique, descriptive `id` (e.g. `id="minimal-line"`) so developers can target it directly:

```html
<path id="minimal-line" d="M..." fill="none" stroke="#111" stroke-width="2" />
```

```js
// Developer side (GSAP DrawSVG)
gsap.from("#minimal-line", { drawSVG: 0 });
```

## Step 5: Consistent Stroke Width

Keep `stroke-width` consistent across the entire path. Variable stroke widths read inconsistently when drawn and complicate the animation.

## Step 6: Verify

Open the exported SVG and confirm:
- [ ] No `fill` on the animated path (`fill="none"` or no fill); it uses `stroke`
- [ ] Anchor points minimized
- [ ] No empty groups, clip-paths, or metadata left in the file
- [ ] The animated path carries a unique `id`
- [ ] `stroke-width` is uniform along the path

</process>

<success_criteria>
- [ ] SVG is strokes-only (no fills on animated paths)
- [ ] Anchor points reduced to the minimum
- [ ] Export cleaned via SVGOMG (no empty groups / clip-masks / metadata)
- [ ] Each animated path has a unique, descriptive `id`
- [ ] Consistent `stroke-width` throughout
- [ ] File verified ready for GSAP DrawSVG (or equivalent) targeting
</success_criteria>
