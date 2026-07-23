# Workflow: Set Up Agent Files

<required_reading>
**Read this reference file NOW:**
1. references/agent-registry.md
</required_reading>

<process>
## Step 1: Ask which agents to support

Use the host agent's native structured-question / multi-select tool (Claude: `AskUserQuestion` with `multiSelect: true`). Present these options with descriptions, **defaulting Claude / Antigravity / Codex to selected**:

- **Claude** — Claude Code (does not read AGENTS.md natively → gets a `CLAUDE.md` stub)
- **Antigravity** — Google's agentic IDE
- **Codex** — OpenAI Codex CLI (reads AGENTS.md natively → no stub)
- **Other** — free-text for Gemini, Cursor, Windsurf, etc.

If the agent has no question tool, fall back to a numbered text prompt listing the same options.

## Step 2: Create or merge AGENTS.md

Check for an existing `AGENTS.md` at the project root.
- **If absent:** scaffold a starter with sections for: project overview/name, build & test commands (placeholders if unknown), code conventions, and an empty area for the feature blocks added by later workflows. Keep it short and editable.
- **If present:** leave the user's content intact. Later workflows append their own clearly-delimited sections idempotently.

## Step 3: Create per-agent stub files

For each selected agent, consult `references/agent-registry.md`:
- If the agent **reads `AGENTS.md` natively** (e.g. Codex) → create **no** stub.
- Otherwise → create its stub file (e.g. `CLAUDE.md`, `GEMINI.md`) whose **entire content is the single line:**
  ```
  @AGENTS.md
  ```
- If a stub file already exists with **other content**, ask the user before overwriting; if it already contains exactly `@AGENTS.md`, leave it.

## Step 4: Record selected agents

Remember the selected-agents list for this session — the feature workflows install MCP servers for exactly these agents.

## Step 5: Continue

Unless the user asked for only agent-file setup, proceed to `workflows/install-features.md`.
</process>

<success_criteria>
- [ ] User was asked (via native question tool) which agents to support, with Claude/Antigravity/Codex pre-selected
- [ ] `AGENTS.md` exists at the project root (created or preserved)
- [ ] Each non-native agent has a stub containing only `@AGENTS.md`; native agents (Codex) have none
- [ ] No existing user file was clobbered without asking
- [ ] Selected-agents list recorded for the feature workflows
</success_criteria>
