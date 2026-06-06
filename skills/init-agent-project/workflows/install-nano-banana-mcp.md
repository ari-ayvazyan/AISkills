# Workflow: Install Nano Banana Image MCP

<required_reading>
**Read these reference files NOW:**
1. references/mcp-install-patterns.md
2. references/agent-registry.md
</required_reading>

<process>
## Step 1: Re-fetch the latest README

Use the host agent's web-fetch tool on https://github.com/ConechoAI/Nano-Banana-MCP and prefer the current install commands and required env vars. If no fetch tool exists, ask the user to paste the install section or proceed with the fallback in `mcp-install-patterns.md` (and say it may be outdated).

## Step 2: Ask for the GEMINI_API_KEY

Use the host agent's native question tool to ask the user for their `GEMINI_API_KEY` (from https://aistudio.google.com/app/apikey).
- **If provided:** inject it into each install command's `env` / `--env`.
- **If withheld:** use the placeholder `<YOUR_GEMINI_API_KEY>` and, at the end, tell the user the exact file and key to edit before the server will work.

Follow `<secrets_handling>` in `mcp-install-patterns.md` — never commit/invent a real key.

## Step 3: Install for each selected agent

For every agent in the selected-agents list:
- **Claude Code:** `claude mcp add nano-banana --env GEMINI_API_KEY=<KEY-or-placeholder> -- npx nano-banana-mcp`
- **Codex:** `codex mcp add nano-banana --env GEMINI_API_KEY=<KEY-or-placeholder> npx nano-banana-mcp`
- **Known config-file agents:** merge the canonical `nano-banana` entry (with the `env` block) into the agent's MCP config.
- **Unknown agent / no known CLI:** write canonical JSON to the config location if known, else emit a manual-setup note with the JSON.

Merge idempotently — if a `nano-banana` server already exists, ask before replacing.

## Step 4: Verify and report

Confirm where possible (e.g. `claude mcp list`). Report per agent, and if any placeholder key was written, prominently remind the user which file(s) to edit.
</process>

<success_criteria>
- [ ] Latest README consulted (or fallback explicitly flagged)
- [ ] User asked for `GEMINI_API_KEY`; real key injected or placeholder written with edit instructions
- [ ] Nano Banana MCP configured for every selected agent
- [ ] No real key committed or invented; no duplicate server entries
- [ ] Per-agent result + any placeholder reminder reported
</success_criteria>
