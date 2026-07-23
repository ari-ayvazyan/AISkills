# Workflow: Install Features

<required_reading>
No reference required up front. Each selected feature's workflow lists its own reading.
</required_reading>

<process>
## Step 1: Ask which features to install

Use the host agent's native multi-select question tool. Present these options (none pre-selected), with descriptions:

- **Playwright MCP** — browser automation / screenshots via `@playwright/mcp`
- **Nano Banana image MCP** — AI image generation/editing (needs `GEMINI_API_KEY`)
- **UI Verification playwright instructions** — before/after screenshot review on UI changes (works best with Playwright MCP)

If the agent has no question tool, fall back to a numbered multi-choice text prompt.

## Step 2: Note dependencies

- **UI Verification** is instruction-only (it edits `AGENTS.md`); it doesn't install software.
- UI Verification relies on the **Playwright MCP**. If the user picked UI Verification but not Playwright MCP, point this out and suggest adding it.

## Step 3: Run the selected workflows in order

For each selected feature, run its workflow and use the **selected-agents list** from `setup-agent-files.md`:
- Playwright MCP → `workflows/install-playwright-mcp.md`
- Nano Banana image MCP → `workflows/install-nano-banana-mcp.md`
- UI Verification → `workflows/add-ui-verification.md`

## Step 4: Summarize

Report what was configured per agent, list any placeholders the user must fill in (e.g. `GEMINI_API_KEY`), and note any manual-setup fallbacks emitted for agents without a known install path.
</process>

<success_criteria>
- [ ] User was asked (via native question tool) which features to install
- [ ] Each selected feature workflow ran against the selected-agents list
- [ ] Dependencies were surfaced (UI Verification ⇒ Playwright MCP)
- [ ] A clear per-agent summary was given, including any placeholders / manual steps
</success_criteria>
