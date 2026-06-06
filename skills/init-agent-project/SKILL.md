---
name: init-agent-project
description: >
  Bootstraps a project for AI-agent usage in any agent.
disable-model-invocation: true
---

<essential_principles>

**Principle 1: AGENTS.md Is the Single Source of Truth**
All agent instructions live in one file at the project root: `AGENTS.md`. Agents that read `AGENTS.md` natively (e.g. Codex) use it directly. Agents that do **not** read it natively (e.g. Claude → `CLAUDE.md`, Gemini → `GEMINI.md`) get a thin **stub file whose only content is `@AGENTS.md`** — an import/include that points back to the canonical file. Never duplicate instruction content across files; the stub only imports.

**Principle 2: Agent-Agnostic Execution**
This skill runs inside *any* agent, so it never relies on a single vendor's tooling. Before installing an MCP server, **re-fetch the latest README at runtime** (the reference files carry URLs + fallback commands) so install commands stay current. For an agent you know how to configure, use its native install command. For an agent you do not, **write the canonical MCP JSON to its config location if known, otherwise emit a clear manual-setup note** — never guess a fake CLI command.

**Principle 3: Ask, Don't Assume**
At every decision point, present choices using the **host agent's own native structured-question / selection tool** — Claude has `AskUserQuestion`; Codex, Gemini and other CLIs have their own interactive question mechanisms. Always offer suggested options. Only fall back to plain numbered text prompts when the running agent has no question tool at all.

**Principle 4: Secrets Are Prompted, Never Invented**
For any API key (e.g. `GEMINI_API_KEY` for Nano Banana), ask the user. If they don't provide it, write a clearly-marked placeholder like `<YOUR_GEMINI_API_KEY>` and tell them exactly which file to edit. Never hardcode a real key and never invent one.

**Principle 5: Idempotent**
Detect existing `AGENTS.md`, stub files, MCP entries, and appended sections. Merge or append rather than clobber; skip work already done. Re-running the skill must not duplicate sections or overwrite a user-customized file without asking first.

</essential_principles>

<intake>
This skill runs as a short linear pipeline. Unless the user asks for a single sub-step, run the two core workflows in order:

1. `workflows/setup-agent-files.md` — ask which agents to support, then write `AGENTS.md` + any needed stub files.
2. `workflows/install-features.md` — ask which features to install, then run the matching install workflow(s).

**If the user explicitly wants just one piece** (e.g. "just add UI verification", "only install playwright"), use the routing table to jump straight there. Otherwise begin at `setup-agent-files.md`.

Always present the agent and feature choices through the host agent's native question tool (see Principle 3).
</intake>

<routing>
| Intent | Workflow |
|--------|----------|
| Full setup, "init for agents", "set up this repo" | `workflows/setup-agent-files.md` then `workflows/install-features.md` |
| "which agents", "create AGENTS.md", "add CLAUDE.md" | `workflows/setup-agent-files.md` |
| "install features", "add MCPs" | `workflows/install-features.md` |
| "playwright mcp", "browser automation" | `workflows/install-playwright-mcp.md` |
| "nano banana", "image generation mcp" | `workflows/install-nano-banana-mcp.md` |
| "ui verification", "screenshot before/after" | `workflows/add-ui-verification.md` |

**After reading the workflow, follow it exactly.**
</routing>

<reference_index>
**Domain knowledge in `references/`:**

- **agent-registry.md** — Known agents and how each is configured: whether it reads `AGENTS.md` natively, its stub filename if not, its MCP install command, and its MCP config file path. Includes guidance for handling unknown agents.
- **mcp-install-patterns.md** — Canonical `mcpServers` JSON for the Playwright and Nano Banana servers, the per-agent install-command matrix, the runtime-refetch rule, secrets handling, and idempotent-merge guidance for existing configs.
</reference_index>

<workflows_index>

| Workflow | Purpose |
|----------|---------|
| setup-agent-files.md | Ask which agents to support; create/merge `AGENTS.md` and per-agent `@AGENTS.md` stubs |
| install-features.md | Ask which features to install; route to the matching install workflow(s) |
| install-playwright-mcp.md | Install the Playwright MCP for each selected agent |
| install-nano-banana-mcp.md | Install the Nano Banana image MCP (with prompted `GEMINI_API_KEY`) per agent |
| add-ui-verification.md | Append the before/after screenshot UI-verification section to `AGENTS.md` |
</workflows_index>

<success_criteria>
A project initialized with this skill:

- [ ] Has an `AGENTS.md` at the project root holding all agent instructions
- [ ] Has a `@AGENTS.md` stub for every selected agent that doesn't read `AGENTS.md` natively (and none for those that do, e.g. Codex)
- [ ] Has each requested MCP server configured for every selected agent (via native command where known, canonical config + note otherwise)
- [ ] Stores no real secrets in committed config — placeholders + instructions where a key was withheld
- [ ] Contains each selected instruction block (UI verification) exactly once, even after re-running
</success_criteria>
