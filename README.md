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

### ecp-code-agent-skills · v0.1.1

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

**meta**

| Skill | Use | What it does | Source | License |
|---|---|---|---|---|
| [create-agent-skills](plugins/ecp-code-agent-skills/skills/meta/create-agent-skills) | 👤 | Expert guidance for Claude Code Skills. Use when working with SKILL.md files, authoring new skills, improving existing skills, or understanding skill structure. | - | - |
| [init-agent-project](plugins/ecp-code-agent-skills/skills/meta/init-agent-project) | 👤 | Bootstraps a project for AI-agent usage in any agent. | - | - |
| [mcp-builder](plugins/ecp-code-agent-skills/skills/meta/mcp-builder) | 👤 | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK). | - | - |

**planning**

| Skill | Use | What it does | Source | License |
|---|---|---|---|---|
| [codebase-design](plugins/ecp-code-agent-skills/skills/planning/codebase-design) | 🤖👤 | Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find deepening opportunities, decide where a seam goes, make code more testable or AI-navigable, or when another skill needs the deep-module vocabulary. | [Source](https://github.com/mattpocock/skills/tree/ed37663cc5fbef691ddfecd080dff42f7e7e350d/skills/engineering/codebase-design) | [License](https://github.com/mattpocock/skills/blob/ed37663cc5fbef691ddfecd080dff42f7e7e350d/LICENSE) |
| [improve-codebase-architecture](plugins/ecp-code-agent-skills/skills/planning/improve-codebase-architecture) | 👤 | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. | [Source](https://github.com/mattpocock/skills/tree/ed37663cc5fbef691ddfecd080dff42f7e7e350d/skills/engineering/improve-codebase-architecture) | [License](https://github.com/mattpocock/skills/blob/ed37663cc5fbef691ddfecd080dff42f7e7e350d/LICENSE) |

**web**

| Skill | Use | What it does | Source | License |
|---|---|---|---|---|
| [favicon-generator](plugins/ecp-code-agent-skills/skills/web/favicon-generator) | 👤 | Generate professional-quality favicons. Trigger when you need favicons, app icons, or browser tab icons. | - | - |
| [og-image-creator](plugins/ecp-code-agent-skills/skills/web/og-image-creator) | 👤 | Smart OG image generation that studies your codebase, understands routes and brand identity, then creates contextually appropriate Open Graph images using Playwright and React components. | - | - |
| [seo-optimizer](plugins/ecp-code-agent-skills/skills/web/seo-optimizer) | 👤 | Comprehensive SEO optimization for web applications. Use when asked to improve search rankings, add meta tags, create structured data, generate sitemaps, optimize for Core Web Vitals, or analyze SEO issues. Works with Next.js, Astro, React, and static HTML sites. | - | - |

**web/planning**

| Skill | Use | What it does | Source | License |
|---|---|---|---|---|
| [color-architect](plugins/ecp-code-agent-skills/skills/web/planning/color-architect) | 👤 | Generates strategic color palettes. Use when creating or updating app color schemes, theming, or brand colors. | - | - |
| [generate-app-names](plugins/ecp-code-agent-skills/skills/web/planning/generate-app-names) | 👤 | Generates strategic product and application names using linguistic engineering. Trigger when invoked with /generate-app-names | - | - |
| [minimalist-web-design](plugins/ecp-code-agent-skills/skills/web/planning/minimalist-web-design) | 👤 | Designs and reviews minimalist, editorial-feeling web interfaces to a 2026 standard — distinctive layouts, extreme typographic hierarchy, restrained-but-bold color, strict performance budgets, and motion/SVG developer handoff. Use when designing a landing page or marketing site, auditing an existing design for generic "visual recycling," or preparing animated SVGs (e.g. GSAP DrawSVG) for developer handoff. | - | - |

---

_Generated by [ecp-skillman](https://ecp-skillman.itdo.at/)._
