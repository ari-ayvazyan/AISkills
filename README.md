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

### Other agents

These skills also work outside Claude Code (Cursor, Codex, Copilot and others) via [Vercel Labs Skills](https://github.com/vercel-labs/skills):

```bash
npx skills@latest add ari-ayvazyan/AISkills
```

## Plugins

Each plugin lists its skills with a short summary; expand a skill for the full description and source.

> | | |
> |---|---|
> | 🤖👤 | invoked either way: Claude can load it on its own, and you can call it with `/name` |
> | 🤖 | self-invoked by the agent only, hidden from the `/` menu |
> | 👤 | user-invoked only, Claude will not load it on its own |

### ecp-chat-skills · v0.1.3

Web/Chat Skills

```
/plugin install ecp-chat-skills@AISkills
```

| Skill | Use | What it does |
|---|---|---|
| [caveman](plugins/ecp-chat-skills/skills/caveman) | 👤 | Ultra-compressed communication mode. Us… |
| [formatted-summary](plugins/ecp-chat-skills/skills/formatted-summary) | 👤 | Summarizes texts in well digestible way |
| [grilling](plugins/ecp-chat-skills/skills/grilling) | 👤 | Grill the user relentlessly about a pla… |
| [handoff-micro-spec](plugins/ecp-chat-skills/skills/handoff-micro-spec) | 👤 | Turn a project idea into a minimal, on-… |
| [write-article](plugins/ecp-chat-skills/skills/write-article) | 👤 | Edit and improve articles by restructur… |

<details>
<summary>👤 <a href="plugins/ecp-chat-skills/skills/caveman"><code>caveman</code></a></summary>

Ultra-compressed communication mode. Use when user says "caveman mode" or invokes /caveman.

</details>

<details>
<summary>👤 <a href="plugins/ecp-chat-skills/skills/formatted-summary"><code>formatted-summary</code></a></summary>

Summarizes texts in well digestible way

</details>

<details>
<summary>👤 <a href="plugins/ecp-chat-skills/skills/grilling"><code>grilling</code></a></summary>

Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' trigger phrases.

Source: [github.com/mattpocock/skills](https://github.com/mattpocock/skills/tree/ed37663cc5fbef691ddfecd080dff42f7e7e350d/skills/productivity/grilling) · [License](https://github.com/mattpocock/skills/blob/ed37663cc5fbef691ddfecd080dff42f7e7e350d/LICENSE)

</details>

<details>
<summary>👤 <a href="plugins/ecp-chat-skills/skills/handoff-micro-spec"><code>handoff-micro-spec</code></a></summary>

Turn a project idea into a minimal, on-point SPEC.md (caveman style — least text, max info). Use when the user runs /micro-spec or asks to spec out / document a project idea.

</details>

<details>
<summary>👤 <a href="plugins/ecp-chat-skills/skills/write-article"><code>write-article</code></a></summary>

Edit and improve articles by restructuring sections, improving clarity, and tightening prose. Use when user wants to edit, revise, or improve an article draft.

Source: [github.com/mattpocock/skills](https://github.com/mattpocock/skills/tree/ed37663cc5fbef691ddfecd080dff42f7e7e350d/skills/personal/edit-article) · [License](https://github.com/mattpocock/skills/blob/ed37663cc5fbef691ddfecd080dff42f7e7e350d/LICENSE)

</details>

### ecp-code-agent-skills · v0.1.1

Coding Agent Skills

```
/plugin install ecp-code-agent-skills@AISkills
```

| Skill | Use | What it does |
|---|---|---|
| [architecture-decisions](plugins/ecp-code-agent-skills/skills/architecture-decisions) | 🤖👤 | ALWAYS Execute this skills before decid… |
| [diagnosing-bugs](plugins/ecp-code-agent-skills/skills/diagnosing-bugs) | 🤖👤 | Diagnosis loop for hard bugs and perfor… |
| [tdd](plugins/ecp-code-agent-skills/skills/tdd) | 🤖👤 | Test-driven development. Use when the u… |
| [teach](plugins/ecp-code-agent-skills/skills/teach) | 👤 | Teach the user a new skill or concept,… |

**meta**

| Skill | Use | What it does |
|---|---|---|
| [create-agent-skills](plugins/ecp-code-agent-skills/skills/meta/create-agent-skills) | 👤 | Expert guidance for Claude Code Skills.… |
| [init-agent-project](plugins/ecp-code-agent-skills/skills/meta/init-agent-project) | 👤 | Bootstraps a project for AI-agent usage… |
| [mcp-builder](plugins/ecp-code-agent-skills/skills/meta/mcp-builder) | 👤 | Guide for creating high-quality MCP (Mo… |

**planning**

| Skill | Use | What it does |
|---|---|---|
| [codebase-design](plugins/ecp-code-agent-skills/skills/planning/codebase-design) | 🤖👤 | Shared vocabulary for designing deep mo… |
| [improve-codebase-architecture](plugins/ecp-code-agent-skills/skills/planning/improve-codebase-architecture) | 👤 | Scan a codebase for deepening opportuni… |

**web**

| Skill | Use | What it does |
|---|---|---|
| [favicon-generator](plugins/ecp-code-agent-skills/skills/web/favicon-generator) | 👤 | Generate professional-quality favicons.… |
| [og-image-creator](plugins/ecp-code-agent-skills/skills/web/og-image-creator) | 👤 | Smart OG image generation that studies… |
| [seo-optimizer](plugins/ecp-code-agent-skills/skills/web/seo-optimizer) | 👤 | Comprehensive SEO optimization for web… |

**web/planning**

| Skill | Use | What it does |
|---|---|---|
| [color-architect](plugins/ecp-code-agent-skills/skills/web/planning/color-architect) | 👤 | Generates strategic color palettes. Use… |
| [generate-app-names](plugins/ecp-code-agent-skills/skills/web/planning/generate-app-names) | 👤 | Generates strategic product and applica… |
| [minimalist-web-design](plugins/ecp-code-agent-skills/skills/web/planning/minimalist-web-design) | 👤 | Designs and reviews minimalist, editori… |

<details>
<summary>🤖👤 <a href="plugins/ecp-code-agent-skills/skills/architecture-decisions"><code>architecture-decisions</code></a></summary>

ALWAYS Execute this skills before deciding any technical/architectural matter, to avoid reintroducing already-solved issues.

</details>

<details>
<summary>🤖👤 <a href="plugins/ecp-code-agent-skills/skills/diagnosing-bugs"><code>diagnosing-bugs</code></a></summary>

Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/throwing/failing/slow.

Source: [github.com/mattpocock/skills](https://github.com/mattpocock/skills/tree/ed37663cc5fbef691ddfecd080dff42f7e7e350d/skills/engineering/diagnosing-bugs) · [License](https://github.com/mattpocock/skills/blob/ed37663cc5fbef691ddfecd080dff42f7e7e350d/LICENSE)

</details>

<details>
<summary>🤖👤 <a href="plugins/ecp-code-agent-skills/skills/tdd"><code>tdd</code></a></summary>

Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integration tests.

Source: [github.com/mattpocock/skills](https://github.com/mattpocock/skills/tree/ed37663cc5fbef691ddfecd080dff42f7e7e350d/skills/engineering/tdd) · [License](https://github.com/mattpocock/skills/blob/ed37663cc5fbef691ddfecd080dff42f7e7e350d/LICENSE)

</details>

<details>
<summary>👤 <a href="plugins/ecp-code-agent-skills/skills/teach"><code>teach</code></a></summary>

Teach the user a new skill or concept, within this workspace.

Source: [github.com/mattpocock/skills](https://github.com/mattpocock/skills/tree/ed37663cc5fbef691ddfecd080dff42f7e7e350d/skills/productivity/teach) · [License](https://github.com/mattpocock/skills/blob/ed37663cc5fbef691ddfecd080dff42f7e7e350d/LICENSE)

</details>

<details>
<summary>👤 <a href="plugins/ecp-code-agent-skills/skills/meta/create-agent-skills"><code>create-agent-skills</code></a></summary>

Expert guidance for Claude Code Skills. Use when working with SKILL.md files, authoring new skills, improving existing skills, or understanding skill structure.

</details>

<details>
<summary>👤 <a href="plugins/ecp-code-agent-skills/skills/meta/init-agent-project"><code>init-agent-project</code></a></summary>

Bootstraps a project for AI-agent usage in any agent.

</details>

<details>
<summary>👤 <a href="plugins/ecp-code-agent-skills/skills/meta/mcp-builder"><code>mcp-builder</code></a></summary>

Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).

</details>

<details>
<summary>🤖👤 <a href="plugins/ecp-code-agent-skills/skills/planning/codebase-design"><code>codebase-design</code></a></summary>

Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find deepening opportunities, decide where a seam goes, make code more testable or AI-navigable, or when another skill needs the deep-module vocabulary.

Source: [github.com/mattpocock/skills](https://github.com/mattpocock/skills/tree/ed37663cc5fbef691ddfecd080dff42f7e7e350d/skills/engineering/codebase-design) · [License](https://github.com/mattpocock/skills/blob/ed37663cc5fbef691ddfecd080dff42f7e7e350d/LICENSE)

</details>

<details>
<summary>👤 <a href="plugins/ecp-code-agent-skills/skills/planning/improve-codebase-architecture"><code>improve-codebase-architecture</code></a></summary>

Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick.

Source: [github.com/mattpocock/skills](https://github.com/mattpocock/skills/tree/ed37663cc5fbef691ddfecd080dff42f7e7e350d/skills/engineering/improve-codebase-architecture) · [License](https://github.com/mattpocock/skills/blob/ed37663cc5fbef691ddfecd080dff42f7e7e350d/LICENSE)

</details>

<details>
<summary>👤 <a href="plugins/ecp-code-agent-skills/skills/web/favicon-generator"><code>favicon-generator</code></a></summary>

Generate professional-quality favicons. Trigger when you need favicons, app icons, or browser tab icons.

</details>

<details>
<summary>👤 <a href="plugins/ecp-code-agent-skills/skills/web/og-image-creator"><code>og-image-creator</code></a></summary>

Smart OG image generation that studies your codebase, understands routes and brand identity, then creates contextually appropriate Open Graph images using Playwright and React components.

</details>

<details>
<summary>👤 <a href="plugins/ecp-code-agent-skills/skills/web/seo-optimizer"><code>seo-optimizer</code></a></summary>

Comprehensive SEO optimization for web applications. Use when asked to improve search rankings, add meta tags, create structured data, generate sitemaps, optimize for Core Web Vitals, or analyze SEO issues. Works with Next.js, Astro, React, and static HTML sites.

</details>

<details>
<summary>👤 <a href="plugins/ecp-code-agent-skills/skills/web/planning/color-architect"><code>color-architect</code></a></summary>

Generates strategic color palettes. Use when creating or updating app color schemes, theming, or brand colors.

</details>

<details>
<summary>👤 <a href="plugins/ecp-code-agent-skills/skills/web/planning/generate-app-names"><code>generate-app-names</code></a></summary>

Generates strategic product and application names using linguistic engineering. Trigger when invoked with /generate-app-names

</details>

<details>
<summary>👤 <a href="plugins/ecp-code-agent-skills/skills/web/planning/minimalist-web-design"><code>minimalist-web-design</code></a></summary>

Designs and reviews minimalist, editorial-feeling web interfaces to a 2026 standard — distinctive layouts, extreme typographic hierarchy, restrained-but-bold color, strict performance budgets, and motion/SVG developer handoff. Use when designing a landing page or marketing site, auditing an existing design for generic "visual recycling," or preparing animated SVGs (e.g. GSAP DrawSVG) for developer handoff.

</details>

---

_Generated by [ecp-skillman](https://ecp-skillman.itdo.at/)._
