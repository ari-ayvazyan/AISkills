# Setup

## 1. Install the requirements
- **ripgrep (`rg`)**: required at scale. On Windows: `winget install BurntSushi.ripgrep.MSVC`. On macOS: `brew install ripgrep`.
- **Python 3.8+**: only for the checker. The script needs no packages.

## 2. Optional: change the location
By default, each project keeps its own knowledge in `./knowledge`, starting at the project root. The folder is created when the first learning is saved.

To change this, set the `Knowledge root:` line in this skill's `SKILL.md`, for example to an absolute path so that all projects share one folder. It is the only setting.

## 3. Allow access
Only needed if the knowledge folder lies outside the project: the agent must be allowed to read and write it, or it will ask every time or fail.

- **Claude Code**: add the folder under `permissions.additionalDirectories` in `~/.claude/settings.json`.
- **Other agents**: add it to the sandbox's writable folders.

## 4. Make retrieval reliable
A skill only loads when the agent decides it fits, and agents often do not think of it before starting work. Add this to the always-on file, `~/.claude/CLAUDE.md` for Claude Code and `AGENTS.md` for most others:

```Use the knowledge-base skill: search it before non-trivial work in a field it may cover, and when a task ends, write to the knowledge base only when asked to do so.```

## Ingesting sources
Ask the agent, for example: `Ingest this into the knowledge base: <link, file path or pasted text>`. It can only open what it has access to: links need a web tool, emails need a mail connector or pasted text.

## Maintenance
    python <skill folder>/scripts/kb_check.py <knowledge folder>
    python <skill folder>/scripts/kb_check.py <knowledge folder> --stale-days 365

The first finds broken links, unlisted files and exceeded limits. The second also lists old files, which you can review or delete.
