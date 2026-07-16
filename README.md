# AISkills

A collection of CLI Agent skills and slash commands.

## Install

### As a Claude Code plugin (recommended)

Works in the Claude Code CLI and in Claude Code on the web (claude.ai). Inside a Claude Code session, run:

```
/plugin marketplace add ari-ayvazyan/AISkills
/plugin install aiskills@aiskills
/reload-plugins
```

All skills and commands are then available under the `aiskills` namespace, e.g. `/aiskills:micro-spec`, `/aiskills:verify-all`, `/aiskills:kiro.implement`. Skills with model-invocation descriptions are also picked up automatically based on context.

The plugin has no pinned version, so every push to this repo counts as a new version — `/plugin update` (or auto-update) picks up the latest commit.

Teams can auto-prompt installation for a project by adding this to the project's `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "aiskills": {
      "source": { "source": "github", "repo": "ari-ayvazyan/AISkills" }
    }
  },
  "enabledPlugins": { "aiskills@aiskills": true }
}
```

### Manual Install
Copy the commands and skills folder into your cli agent dir. eg. .claude/


### Install everything

Install all skills from this repo into your user-global Claude Code skills directory (`~/.claude/skills/`):

```bash
npx skills add ari-ayvazyan/AISkills --all
```

Flags:
- `-g` — install to your user directory instead of the current project

## Update / Remove

```bash
npx skills update          # upgrade installed skills
npx skills remove <name>   # uninstall a specific skill
```

## Slash commands

The slash commands under `commands/` are not picked up automatically — copy the ones you want into `~/.claude/commands/` (global) or `.claude/commands/` (project):
