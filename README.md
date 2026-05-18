# AISkills

A collection of CLI Agent skills and slash commands.

## Install

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
