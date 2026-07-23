# Workflow: Install Playwright MCP

<required_reading>
**Read these reference files NOW:**
1. references/mcp-install-patterns.md
2. references/agent-registry.md
</required_reading>

<process>
## Step 1: Re-fetch the latest README

Use the host agent's web-fetch tool on https://github.com/microsoft/playwright-mcp and prefer the current install commands. If no fetch tool exists, ask the user to paste the install section or proceed with the fallback in `mcp-install-patterns.md` (and say it may be outdated).

## Step 2: Install for each selected agent

For every agent in the selected-agents list (from `setup-agent-files.md`), use its method from `agent-registry.md` / `mcp-install-patterns.md`:
- **Claude Code:** `claude mcp add playwright npx @playwright/mcp@latest`
- **Codex:** `codex mcp add playwright npx "@playwright/mcp@latest"`
- **Known config-file agents (Gemini, Cursor, Windsurf, VS Code):** merge the canonical `playwright` entry into that agent's MCP config.
- **Unknown agent / no known CLI (e.g. Antigravity):** write the canonical JSON to its config location if you can determine it; otherwise output the JSON and a clear instruction telling the user where to paste it. Never fabricate a command.

Merge idempotently — if a `playwright` server already exists, ask before replacing.

## Step 3: Verify and report

Where a verification command exists (e.g. `claude mcp list`), run it to confirm. Report per agent: installed via command / written to config / manual step required.
</process>

<success_criteria>
- [ ] Latest README consulted (or fallback explicitly flagged)
- [ ] Playwright MCP configured for every selected agent (command, config write, or manual note)
- [ ] No duplicate server entries created
- [ ] Per-agent result reported
</success_criteria>
