---
name: architecture-plan
description: Generate concise, mobile-friendly architecture cards for reviewing plans, proposed changes, finished work and commit overviews.
---

# Architecture Card Review

Use this skill **if and only if a high-level architectural review is requested**:
- A plan requested by the user (e.g., plan mode, "plan this", "propose how").
- A suggested change awaiting user review or approval.
- An architecture overview of commits (generate one card per commit, including the commit hash and date).
- Work was finished, and you want to communicate to the user what has changed.


## Core Principles
1. **Mobile-First Brevity:** The card must fit on a single phone screen. 
   - **No tables.**
   - Use concise phrases instead of full sentences.
   - Include only what a reviewer must not miss.
   - **No implementation details:** Omit file names, function names, code snippets, or build steps.

## Card Layout

Follow this exact vertical structure:

1. **Title:** `# <The result in a few words>`
2. **Size:** `**Size:** None | Extension | New part | Changed rule`
3. **Diagram:** Required whenever parts, connections, or networks are added or modified (see rules below).
4. **Entries:** One line per changing category formatted as `**Label:** <about 12 words>`.

## Diagram Rules

- **Orientation & Block:** Must be vertical and enclosed in a standard code block (` ``` `).
- **Width Limit:** **At most 30 characters wide** to prevent horizontal scrolling on mobile devices.
- **State & Markers:** Show the planned target state. Clearly mark new or altered elements with `NEW`, `CHANGED`, or `GONE`.
- **No Redundancy:** The text entries below the diagram must never repeat what is already shown in the diagram.

## Entry Categories

Check every category below, but **only include entries that have a change** (except `Undo`, which is always required):

- **Parts:** Apps, containers, tables, external systems, background workers, or file stores.
- **Connections:** Who talks to whom.
- **Data:** What is stored where, who owns it, and who may write to it.
- **Contracts:** What others rely on (APIs, events, config fields, file formats).
- **Rules:** Who decides and what happens automatically.
- **Failure:** Behavior when a part gives no answer or times out.
- **Access:** Who may do or see what, permissions, and secrets.
- **Operation:** Deployments, migrations, and server setup.
- **Other:** Whatever else changes what a part is, knows, may do, or depends on.
- **Undo:** *(Always required)* How hard it is to revert once live.
- **Not part of this:** *(Include in plans)* Scope exclusions that a reviewer might otherwise expect.

## Example Output

````markdown
# VAT IDs checked in VIES

**Size:** New part

```
Invoices
   │ NEW: before issuing
   ▼
Contacts ──► vat_checks NEW
   │ NEW
   ▼
VIES NEW (EU, external)
```

**Data:** One row per check, add-only, audited. Own VAT ID sent to VIES.
**Rules:** Invalid ID blocks the invoice. Admins can override.
**Failure:** No answer: issued only if valid before. Wait up to 45 s.
**Operation:** 1 additive migration.
**Undo:** Medium. Dropping the table deletes the proofs.
**Not part of this:** Regular re-checks.
````
