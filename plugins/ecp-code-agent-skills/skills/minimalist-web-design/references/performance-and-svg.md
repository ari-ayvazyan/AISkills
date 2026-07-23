# Reference: Performance-First Design & SVG Motion Handoff

Domain knowledge for the performance budget and SVG handoff steps.

## Performance-First Design

Make speed the central design constraint, not a post-launch optimization.

### The Mobile LCP Budget
**Largest Contentful Paint (LCP) must be under 2.5 seconds on mobile devices.** LCP
measures when the largest visible element finishes loading — the moment the page
feels "there." On mobile networks and CPUs this budget is tight, so it shapes
design choices rather than reacting to them.

### Calculate the "Performance Cost" of Every Element
Every animation, typeface, and graphic must prove its value. If an element cannot
justify its cost, it is rigorously removed from the design — not deferred to a
later optimization pass. Treat each addition as spending from a fixed budget.

Practical implications:
- Each web font is a request + render-blocking cost; 2–3 families maximum is also a
  performance decision, not only an aesthetic one.
- Heavy background `.mp4` video is the classic budget-killer → use `.webm` or
  generate backgrounds via WebGL (e.g. animated Bayer dithering).
- Images: lossless **WebP**/**AVIF**, served at exact native display dimensions —
  never ship oversized images scaled down by the browser.

## SVG Motion Handoff (e.g. GSAP DrawSVG)

When minimalist lines or icons are animated on scroll, the SVG must be prepared by
design so developers can animate it cleanly. The requirements and the reasoning:

### Strokes Only — No Fills
The design must contain **no filled areas (fills)** and consist purely of path
outlines (**strokes**). Stroke-drawing animation (like DrawSVG) animates the length
of a stroke; a fill has nothing to "draw," so filled shapes cannot be line-animated.

### Reduce Anchor Points
Every unnecessary anchor point costs CPU during animation. Simplify the vector
paths drastically — keep only the anchors required to hold the shape.

### Clean Export Code
On export, remove all empty groups, clipping masks, and metadata. Use a tool like
**SVGOMG** to produce minimal output. Cruft bloats the file and complicates
targeting.

### Assign IDs
Give the exact path to be animated a unique `id` (e.g. `id="minimal-line"`) so
developers can target it directly:

```html
<path id="minimal-line" d="M..." fill="none" stroke="#111" stroke-width="2" />
```

### Consistent Stroke Width
Keep the `stroke-width` property consistent across the entire path. Variable widths
read inconsistently when the line is drawn and complicate the animation.
