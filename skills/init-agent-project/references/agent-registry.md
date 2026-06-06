# Reference: Agent Registry

<purpose>
How to configure each known agent: whether it reads `AGENTS.md` natively, the stub
filename to create if it doesn't, the MCP install command to prefer, and the MCP config
file it ultimately writes. Use this to decide which stubs to create and how to install
MCP servers. For any agent not listed, follow `<unknown_agents>` at the bottom.
</purpose>

<registry>
| Agent | Reads AGENTS.md natively? | Stub file to create | MCP install command | MCP config location |
|-------|--------------------------|---------------------|---------------------|---------------------|
| Codex (OpenAI CLI) | **Yes** | none | `codex mcp add <name> <cmd> <args...>` | `~/.codex/config.toml` (`[mcp_servers.<name>]`) |
| Claude Code | No | `CLAUDE.md` | `claude mcp add <name> <cmd> <args...>` | `.mcp.json` (project) or `~/.claude.json` (user) |
| Antigravity (Google IDE) | Unconfirmed — treat as No | `AGENTS.md` is consumed; if not, the running agent should write the IDE's MCP config and a stub if needed | No documented CLI — write canonical JSON to the IDE's MCP config if known, else emit a manual-setup note | IDE settings / MCP config (let the executing agent determine) |
| Gemini CLI | No | `GEMINI.md` | Standard MCP config | `~/.gemini/settings.json` (`mcpServers`) |
| Cursor | No | `.cursorrules` or `AGENTS.md` import per Cursor docs | Settings → MCP → Add Server (or `~/.cursor/mcp.json`) | `~/.cursor/mcp.json` |
| Windsurf | No | `.windsurfrules` | Windsurf MCP settings | `~/.codeium/windsurf/mcp_config.json` |
| VS Code (Copilot) | No | (uses Copilot instructions) | `code --add-mcp '{...}'` | `~/.copilot/mcp-config.json` |
</registry>

<notes>
- **Codex is the key exception:** it reads `AGENTS.md` directly, so do **not** create a stub for Codex. Claude does **not**, so Claude always gets a `CLAUDE.md` stub containing only `@AGENTS.md`.
- The "Stub file" column is the file whose **entire content is the single line `@AGENTS.md`**. Do not put real instructions there.
- Config locations drift between versions. **Always confirm against the live README / agent docs at runtime** (see `mcp-install-patterns.md`) before writing a file. The values here are sensible defaults, not guarantees.
- Antigravity has no documented MCP CLI as of this writing — the executing agent should reason about the current install path itself, write the canonical JSON if it can determine the location, and otherwise hand the user a clear manual step. Do not invent a command.
</notes>

<unknown_agents>
When the user names an agent not in the table:
1. Assume it does **not** read `AGENTS.md` unless you can confirm otherwise; create a stub named after the agent (e.g. `<AGENT>.md`) containing only `@AGENTS.md`, and tell the user to adjust if the agent uses a different instruction filename.
2. For MCP installs, prefer the agent's own documented CLI if you know it; otherwise write the **canonical `mcpServers` JSON** (see `mcp-install-patterns.md`) to the agent's config file if you can determine it, and if not, output the JSON plus a short instruction telling the user where to paste it.
3. Never fabricate a command or path. State explicitly when you are giving a manual fallback.
</unknown_agents>
