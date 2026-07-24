# AISkills

Claude Code plugin marketplace, managed with [ecp-skillman](https://ecp-skillman.itdo.at/).

## Install

### Claude Code

Add this marketplace in Claude Code:

```
/plugin marketplace add ari-ayvazyan/AISkills
```

Then install a plugin:

```
/plugin install ecp-chat-skills@AISkills
/plugin install ecp-code-agent-skills@AISkills
```

<details>
<summary><strong>Other agents</strong> (Cursor, Codex, Copilot, Antigravity, OpenCode, and others)</summary>

**Copy the skills once** with [Vercel Labs Skills](https://github.com/vercel-labs/skills):

```bash
npx skills@latest add ari-ayvazyan/AISkills
```

Or serve them live over MCP with [ecp-bridge](https://www.npmjs.com/package/ecp-bridge). Skills stay in this repo and auto-update whenever it changes, with no reinstall needed:

```json
{
  "mcpServers": {
    "ecp-bridge": {
      "command": "npx",
      "args": [
        "-y",
        "ecp-bridge",
        "ari-ayvazyan/AISkills",
        "ecp-chat-skills,ecp-code-agent-skills"
      ]
    }
  }
}
```

Add that to your MCP client config. The final argument is optional: omit it to serve every plugin in the marketplace, or pass a comma-separated subset as shown.

</details>

## Plugins

Each plugin lists its skills with a summary, source, and license.

> | | |
> |---|---|
> | 🤖👤 | invoked either way: Claude can load it on its own, and you can call it with `/name` |
> | 🤖 | self-invoked by the agent only, hidden from the `/` menu |
> | 👤 | user-invoked only, Claude will not load it on its own |

### ecp-chat-skills · v0.1.6

Web/Chat Skills

```
/plugin install ecp-chat-skills@AISkills
```

| Skill | Use | What it does | Source | License |
|---|---|---|---|---|
| [caveman](plugins/ecp-chat-skills/skills/caveman) | 👤 | Ultra-compressed communication mode. Use when user says "caveman mode" or invokes /caveman. | - | - |
| [formatted-summary](plugins/ecp-chat-skills/skills/formatted-summary) | 👤 | Summarizes texts in well digestible way | - | - |
| [grilling](plugins/ecp-chat-skills/skills/grilling) | 👤 | Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' trigger phrases. | [Source](https://github.com/mattpocock/skills/tree/ed37663cc5fbef691ddfecd080dff42f7e7e350d/skills/productivity/grilling) | [License](https://github.com/mattpocock/skills/blob/ed37663cc5fbef691ddfecd080dff42f7e7e350d/LICENSE) |
| [handoff-micro-spec](plugins/ecp-chat-skills/skills/handoff-micro-spec) | 👤 | Turn a project idea into a minimal, on-point SPEC.md (caveman style — least text, max info). Use when the user runs /micro-spec or asks to spec out / document a project idea. | - | - |
| [write-article](plugins/ecp-chat-skills/skills/write-article) | 👤 | Edit and improve articles by restructuring sections, improving clarity, and tightening prose. Use when user wants to edit, revise, or improve an article draft. | [Source](https://github.com/mattpocock/skills/tree/ed37663cc5fbef691ddfecd080dff42f7e7e350d/skills/personal/edit-article) | [License](https://github.com/mattpocock/skills/blob/ed37663cc5fbef691ddfecd080dff42f7e7e350d/LICENSE) |

### ecp-code-agent-skills · v0.1.2

Coding Agent Skills

```
/plugin install ecp-code-agent-skills@AISkills
```

| Skill | Use | What it does | Source | License |
|---|---|---|---|---|
| [architecture-decisions](plugins/ecp-code-agent-skills/skills/architecture-decisions) | 🤖👤 | ALWAYS Execute this skills before deciding any technical/architectural matter, to avoid reintroducing already-solved issues. | - | - |
| [diagnosing-bugs](plugins/ecp-code-agent-skills/skills/diagnosing-bugs) | 🤖👤 | Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/throwing/failing/slow. | [Source](https://github.com/mattpocock/skills/tree/ed37663cc5fbef691ddfecd080dff42f7e7e350d/skills/engineering/diagnosing-bugs) | [License](https://github.com/mattpocock/skills/blob/ed37663cc5fbef691ddfecd080dff42f7e7e350d/LICENSE) |
| [tdd](plugins/ecp-code-agent-skills/skills/tdd) | 🤖👤 | Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integration tests. | [Source](https://github.com/mattpocock/skills/tree/ed37663cc5fbef691ddfecd080dff42f7e7e350d/skills/engineering/tdd) | [License](https://github.com/mattpocock/skills/blob/ed37663cc5fbef691ddfecd080dff42f7e7e350d/LICENSE) |
| [teach](plugins/ecp-code-agent-skills/skills/teach) | 👤 | Teach the user a new skill or concept, within this workspace. | [Source](https://github.com/mattpocock/skills/tree/ed37663cc5fbef691ddfecd080dff42f7e7e350d/skills/productivity/teach) | [License](https://github.com/mattpocock/skills/blob/ed37663cc5fbef691ddfecd080dff42f7e7e350d/LICENSE) |

**frontend/skills**

| Skill | Use | What it does | Source | License |
|---|---|---|---|---|
| [brandkit](plugins/ecp-code-agent-skills/skills/brandkit) | 🤖👤 | Premium brand-kit image generation skill for creating high-end brand-guidelines boards, logo systems, identity decks, and visual-world presentations. Trained for minimalist, cinematic, editorial, dark-tech, luxury, cultural, security, gaming, developer-tool, and consumer-app brand systems. Optimized for intentional logo concepting, refined composition, sparse typography, strong symbolic meaning, premium mockups, art-directed imagery, and flexible grid layouts. | [Source](https://github.com/Leonxlnx/taste-skill/tree/e988add20dab0fa97d7a76781c48961c8184288e/skills/brandkit) | [License](https://github.com/Leonxlnx/taste-skill/blob/e988add20dab0fa97d7a76781c48961c8184288e/LICENSE) |
| [design-taste-frontend](plugins/ecp-code-agent-skills/skills/design-taste-frontend) | 🤖👤 | Anti-slop frontend skill for landing pages, portfolios, and redesigns. The agent reads the brief, infers the right design direction, and ships interfaces that do not look templated. Real design systems when applicable, audit-first on redesigns, strict pre-flight check. | [Source](https://github.com/Leonxlnx/taste-skill/tree/e988add20dab0fa97d7a76781c48961c8184288e/skills/taste-skill) | [License](https://github.com/Leonxlnx/taste-skill/blob/e988add20dab0fa97d7a76781c48961c8184288e/LICENSE) |
| [full-output-enforcement](plugins/ecp-code-agent-skills/skills/full-output-enforcement) | 🤖👤 | Overrides default LLM truncation behavior. Enforces complete code generation, bans placeholder patterns, and handles token-limit splits cleanly. Apply to any task requiring exhaustive, unabridged output. | [Source](https://github.com/Leonxlnx/taste-skill/tree/e988add20dab0fa97d7a76781c48961c8184288e/skills/output-skill) | [License](https://github.com/Leonxlnx/taste-skill/blob/e988add20dab0fa97d7a76781c48961c8184288e/LICENSE) |
| [gpt-taste](plugins/ecp-code-agent-skills/skills/gpt-taste) | 🤖👤 | Elite UX/UI & Advanced GSAP Motion Engineer. Enforces Python-driven true randomization for layout variance, strict AIDA page structure, wide editorial typography (bans 6-line wraps), gapless bento grids, strict GSAP ScrollTriggers (pinning, stacking, scrubbing), inline micro-images, and massive section spacing. | [Source](https://github.com/Leonxlnx/taste-skill/tree/e988add20dab0fa97d7a76781c48961c8184288e/skills/gpt-tasteskill) | [License](https://github.com/Leonxlnx/taste-skill/blob/e988add20dab0fa97d7a76781c48961c8184288e/LICENSE) |
| [high-end-visual-design](plugins/ecp-code-agent-skills/skills/high-end-visual-design) | 🤖👤 | Teaches the AI to design like a high-end agency. Defines the exact fonts, spacing, shadows, card structures, and animations that make a website feel expensive. Blocks all the common defaults that make AI designs look cheap or generic. | [Source](https://github.com/Leonxlnx/taste-skill/tree/e988add20dab0fa97d7a76781c48961c8184288e/skills/soft-skill) | [License](https://github.com/Leonxlnx/taste-skill/blob/e988add20dab0fa97d7a76781c48961c8184288e/LICENSE) |
| [image-to-code](plugins/ecp-code-agent-skills/skills/image-to-code) | 🤖👤 | Elite website image-to-code skill for Codex. For visually important web tasks, it must first generate the design image(s) itself, deeply analyze them, then implement the website to match them as closely as possible. In Codex, it must prefer large, readable, section-specific images instead of tiny compressed boards, generate fresh standalone images for sections or detail views instead of cropping old ones, avoid lazy under-generation, avoid cards-inside-cards-inside-cards UI, and keep the hero clean, spacious, readable, and visible on a small laptop. | [Source](https://github.com/Leonxlnx/taste-skill/tree/e988add20dab0fa97d7a76781c48961c8184288e/skills/image-to-code-skill) | [License](https://github.com/Leonxlnx/taste-skill/blob/e988add20dab0fa97d7a76781c48961c8184288e/LICENSE) |
| [imagegen-frontend-mobile](plugins/ecp-code-agent-skills/skills/imagegen-frontend-mobile) | 🤖👤 | Elite mobile app image-generation skill for creating premium, app-native screen concepts and flows. Designed for iOS, Android, and cross-platform mobile products. Prioritizes clean hierarchy, comfortably readable text, strong multi-screen consistency, controlled color palettes, non-generic creative direction, textured surfaces, image-led composition, tasteful custom iconography, and clean phone mockup framing. By default, screens should be shown inside a subtle premium iPhone or similar phone mockup with a visible frame, while the main focus stays on the app content itself. This skill generates images only. It does not write code. | [Source](https://github.com/Leonxlnx/taste-skill/tree/e988add20dab0fa97d7a76781c48961c8184288e/skills/imagegen-frontend-mobile) | [License](https://github.com/Leonxlnx/taste-skill/blob/e988add20dab0fa97d7a76781c48961c8184288e/LICENSE) |
| [imagegen-frontend-web](plugins/ecp-code-agent-skills/skills/imagegen-frontend-web) | 🤖👤 | Elite frontend image-direction skill for generating premium, conversion-aware website design references. CRITICAL OUTPUT RULE — generate ONE separate horizontal image FOR EVERY section. A landing page with 8 sections produces 8 images. Never compress multiple sections into one image. Enforces composition variety (not always left-text / right-image), background-image freedom, varied CTAs, varied hero scales (giant / mid / mini minimalist), narrative concept spine, second-read moments, and a single consistent palette across all images. Optimized for landing pages, marketing sites, and product comps that developers or coding models can accurately recreate. | [Source](https://github.com/Leonxlnx/taste-skill/tree/e988add20dab0fa97d7a76781c48961c8184288e/skills/imagegen-frontend-web) | [License](https://github.com/Leonxlnx/taste-skill/blob/e988add20dab0fa97d7a76781c48961c8184288e/LICENSE) |
| [industrial-brutalist-ui](plugins/ecp-code-agent-skills/skills/industrial-brutalist-ui) | 🤖👤 | Raw mechanical interfaces fusing Swiss typographic print with military terminal aesthetics. Rigid grids, extreme type scale contrast, utilitarian color, analog degradation effects. For data-heavy dashboards, portfolios, or editorial sites that need to feel like declassified blueprints. | [Source](https://github.com/Leonxlnx/taste-skill/tree/e988add20dab0fa97d7a76781c48961c8184288e/skills/brutalist-skill) | [License](https://github.com/Leonxlnx/taste-skill/blob/e988add20dab0fa97d7a76781c48961c8184288e/LICENSE) |
| [minimalist-ui](plugins/ecp-code-agent-skills/skills/minimalist-ui) | 🤖👤 | Clean editorial-style interfaces. Warm monochrome palette, typographic contrast, flat bento grids, muted pastels. No gradients, no heavy shadows. | [Source](https://github.com/Leonxlnx/taste-skill/tree/e988add20dab0fa97d7a76781c48961c8184288e/skills/minimalist-skill) | [License](https://github.com/Leonxlnx/taste-skill/blob/e988add20dab0fa97d7a76781c48961c8184288e/LICENSE) |
| [redesign-existing-projects](plugins/ecp-code-agent-skills/skills/redesign-existing-projects) | 🤖👤 | Upgrades existing websites and apps to premium quality. Audits current design, identifies generic AI patterns, and applies high-end design standards without breaking functionality. Works with any CSS framework or vanilla CSS. | [Source](https://github.com/Leonxlnx/taste-skill/tree/e988add20dab0fa97d7a76781c48961c8184288e/skills/redesign-skill) | [License](https://github.com/Leonxlnx/taste-skill/blob/e988add20dab0fa97d7a76781c48961c8184288e/LICENSE) |
| [stitch-design-taste](plugins/ecp-code-agent-skills/skills/stitch-design-taste) | 🤖👤 | Semantic Design System Skill for Google Stitch. Generates agent-friendly DESIGN.md files that enforce premium, anti-generic UI standards — strict typography, calibrated color, asymmetric layouts, perpetual micro-motion, and hardware-accelerated performance. | [Source](https://github.com/Leonxlnx/taste-skill/tree/e988add20dab0fa97d7a76781c48961c8184288e/skills/stitch-skill) | [License](https://github.com/Leonxlnx/taste-skill/blob/e988add20dab0fa97d7a76781c48961c8184288e/LICENSE) |

**meta**

| Skill | Use | What it does | Source | License |
|---|---|---|---|---|
| [create-agent-skills](plugins/ecp-code-agent-skills/skills/create-agent-skills) | 👤 | Expert guidance for Claude Code Skills. Use when working with SKILL.md files, authoring new skills, improving existing skills, or understanding skill structure. | - | - |
| [init-agent-project](plugins/ecp-code-agent-skills/skills/init-agent-project) | 👤 | Bootstraps a project for AI-agent usage in any agent. | - | - |
| [mcp-builder](plugins/ecp-code-agent-skills/skills/mcp-builder) | 👤 | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK). | - | - |

**planning**

| Skill | Use | What it does | Source | License |
|---|---|---|---|---|
| [codebase-design](plugins/ecp-code-agent-skills/skills/codebase-design) | 🤖👤 | Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find deepening opportunities, decide where a seam goes, make code more testable or AI-navigable, or when another skill needs the deep-module vocabulary. | [Source](https://github.com/mattpocock/skills/tree/ed37663cc5fbef691ddfecd080dff42f7e7e350d/skills/engineering/codebase-design) | [License](https://github.com/mattpocock/skills/blob/ed37663cc5fbef691ddfecd080dff42f7e7e350d/LICENSE) |
| [improve-codebase-architecture](plugins/ecp-code-agent-skills/skills/improve-codebase-architecture) | 👤 | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. | [Source](https://github.com/mattpocock/skills/tree/ed37663cc5fbef691ddfecd080dff42f7e7e350d/skills/engineering/improve-codebase-architecture) | [License](https://github.com/mattpocock/skills/blob/ed37663cc5fbef691ddfecd080dff42f7e7e350d/LICENSE) |

**web**

| Skill | Use | What it does | Source | License |
|---|---|---|---|---|
| [favicon-generator](plugins/ecp-code-agent-skills/skills/favicon-generator) | 👤 | Generate professional-quality favicons. Trigger when you need favicons, app icons, or browser tab icons. | - | - |
| [og-image-creator](plugins/ecp-code-agent-skills/skills/og-image-creator) | 👤 | Smart OG image generation that studies your codebase, understands routes and brand identity, then creates contextually appropriate Open Graph images using Playwright and React components. | - | - |
| [seo-optimizer](plugins/ecp-code-agent-skills/skills/seo-optimizer) | 👤 | Comprehensive SEO optimization for web applications. Use when asked to improve search rankings, add meta tags, create structured data, generate sitemaps, optimize for Core Web Vitals, or analyze SEO issues. Works with Next.js, Astro, React, and static HTML sites. | - | - |

**web/planning**

| Skill | Use | What it does | Source | License |
|---|---|---|---|---|
| [color-architect](plugins/ecp-code-agent-skills/skills/color-architect) | 👤 | Generates strategic color palettes. Use when creating or updating app color schemes, theming, or brand colors. | - | - |
| [generate-app-names](plugins/ecp-code-agent-skills/skills/generate-app-names) | 👤 | Generates strategic product and application names using linguistic engineering. Trigger when invoked with /generate-app-names | - | - |
| [minimalist-web-design](plugins/ecp-code-agent-skills/skills/minimalist-web-design) | 👤 | Designs and reviews minimalist, editorial-feeling web interfaces to a 2026 standard — distinctive layouts, extreme typographic hierarchy, restrained-but-bold color, strict performance budgets, and motion/SVG developer handoff. Use when designing a landing page or marketing site, auditing an existing design for generic "visual recycling," or preparing animated SVGs (e.g. GSAP DrawSVG) for developer handoff. | - | - |

---

_Generated by [ecp-skillman](https://ecp-skillman.itdo.at/)._
