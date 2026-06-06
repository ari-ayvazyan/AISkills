# Workflow: Add Architecture Decision Documentation

<required_reading>
No reference required.
</required_reading>

<process>
## Step 1: Create architecture_log.md if absent

Check for `architecture_log.md` at the project root. If it doesn't exist, create it with a short header and an example entry showing the required shape — every entry must capture **WHAT** changed and **WHY**:

```markdown
# Architecture Log

A running log of architectural decisions: topics introduced, removed, or changed.
Each entry records WHAT was decided and WHY, so future work doesn't reintroduce
already-solved problems. Read this file before making any technical decision.

## <YYYY-MM-DD> — <short title>
- **Status:** introduced | changed | removed
- **WHAT:** <the decision / what changed in the architecture>
- **WHY:** <the reasoning, constraints, and alternatives rejected>
- **Consequences / supersedes:** <follow-on effects; links to entries this replaces>
```

If the file already exists, leave its content intact.

## Step 2: Add instructions to AGENTS.md

Read `AGENTS.md`. If a `## Architecture Log` section already exists, stop (idempotent). Otherwise append:

```markdown
## Architecture Log

This project maintains `architecture_log.md`, a running record of architectural
decisions (topics introduced, removed, or changed). Each entry documents WHAT was
decided and WHY.

- **BEFORE considering and before finalizing any technical/architectural decision, READ `architecture_log.md`.** Check whether the topic was already decided to avoid reintroducing problems that were previously solved or reversing a deliberate choice.
- **AFTER making a decision that introduces, removes, or changes an architectural topic, ADD an entry** to `architecture_log.md` capturing WHAT changed and WHY (including alternatives rejected and consequences). Date each entry.
- If a new decision supersedes an earlier one, reference the entry it replaces rather than silently contradicting it.
```

## Step 3: Confirm

Report that `architecture_log.md` exists and that the read-before-deciding / write-after-deciding instructions were added to `AGENTS.md`.
</process>

<success_criteria>
- [ ] `architecture_log.md` exists with a WHAT/WHY entry template (created, or preserved if present)
- [ ] `AGENTS.md` contains the Architecture Log section exactly once (idempotent on re-run)
- [ ] Instructions tell the agent to READ the log before deciding and to ADD a WHAT/WHY entry after deciding
</success_criteria>
