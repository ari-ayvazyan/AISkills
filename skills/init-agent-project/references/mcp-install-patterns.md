# Reference: MCP Install Patterns

<runtime_refetch_rule>
**Before installing any MCP server, fetch its current README** using the host agent's
web-fetch tool (Claude: `WebFetch`) and prefer the commands found there. The snippets
below are a self-contained fallback that was accurate at authoring time but can drift.

- Playwright MCP: https://github.com/microsoft/playwright-mcp
- Nano Banana MCP: https://github.com/ConechoAI/Nano-Banana-MCP

If no fetch tool is available, ask the user to paste the relevant README section, or
proceed with the fallback values below and tell the user they may be outdated.
</runtime_refetch_rule>

<playwright_mcp>
**Package:** `@playwright/mcp` (run via `npx @playwright/mcp@latest`)

Canonical JSON:
```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

Per-agent install:
- **Claude Code:** `claude mcp add playwright npx @playwright/mcp@latest`
- **Codex:** `codex mcp add playwright npx "@playwright/mcp@latest"` (writes `[mcp_servers.playwright]` to `~/.codex/config.toml`)
- **VS Code:** `code --add-mcp '{"name":"playwright","command":"npx","args":["@playwright/mcp@latest"]}'`
- **Gemini / Cursor / Windsurf / unknown:** merge the canonical JSON into the agent's MCP config (see `agent-registry.md`).
</playwright_mcp>

<nano_banana_mcp>
**Package:** `nano-banana-mcp` (run via `npx nano-banana-mcp`)
**Requires:** `GEMINI_API_KEY` (from Google AI Studio: https://aistudio.google.com/app/apikey)
**Tools provided:** `generate_image`, `edit_image`, `continue_editing`

Canonical JSON:
```json
{
  "mcpServers": {
    "nano-banana": {
      "command": "npx",
      "args": ["nano-banana-mcp"],
      "env": {
        "GEMINI_API_KEY": "<YOUR_GEMINI_API_KEY>"
      }
    }
  }
}
```

Per-agent install:
- **Claude Code:** `claude mcp add nano-banana --env GEMINI_API_KEY=<KEY> -- npx nano-banana-mcp`
  (if the user withholds the key, write the canonical JSON with the placeholder instead, or pass the placeholder and tell them to edit it)
- **Codex:** `codex mcp add nano-banana --env GEMINI_API_KEY=<KEY> npx nano-banana-mcp` (writes `~/.codex/config.toml`)
- **Others / unknown:** merge the canonical JSON (with the `env` block) into the agent's MCP config.
</nano_banana_mcp>

<secrets_handling>
1. Ask the user for the key via the host agent's question tool.
2. If provided, inject it into the `env` block / `--env` flag of the install command.
3. If withheld, write the literal placeholder `<YOUR_GEMINI_API_KEY>` and tell the user the exact file + key to edit before the server will work.
4. Never commit a real key, never invent one, and prefer not to echo a provided key back in plaintext output.
</secrets_handling>

<idempotency>
- Before writing, read the target config. If a server with the same name already exists, ask whether to replace it rather than creating a duplicate.
- When merging JSON, preserve other existing `mcpServers` entries — add/replace only the relevant key.
- For TOML (`~/.codex/config.toml`), prefer `codex mcp add` (which merges) over hand-editing.
</idempotency>
