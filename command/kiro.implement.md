---
description: Implement the next pending task from .kiro specs
---

# Kiro Implementation Workflow

Your goal is to autonomously implement the next pending feature or task defined in the Kiro specs.

## 1. Locate and Select Task
1.  Search for `tasks.md` files in `.kiro/specs/`.
2.  If an argument is provided ($ARGUMENTS), use it to filter the spec directory. Otherwise, find the first `tasks.md` that contains pending tasks (`- [ ]`).
3.  Read the selected `tasks.md`.
4.  Identify the **first** task item that is unchecked (`- [ ]`).
    *   Note the line number and exact content.

## 2. Mark In-Progress
1.  Before doing ANY work, edit `tasks.md` to change the task status from `[ ]` to `[-]` (In Progress).

## 3. Understand Context
1.  Read the full description of the task and its sub-items.
2.  Read sibling files in the spec directory (e.g., `design.md`, `requirements.md`) if referenced or for general context.
3.  Plan the implementation based on these requirements.

## 4. Implement
1.  Execute the necessary actions to complete the task.
    *   Write code, create files, refactor, etc.
    *   If the task involves writing tests, write them.
2.  **Verify** your work:
    *   Run relevant tests.
    *   Run build/lint checks.
    *   Ensure the implementation meets the requirements.

## 5. Mark Complete
1.  Once the task is successfully implemented and verified, edit `tasks.md` to change the status from `[-]` to `[x]` (Complete).

## 6. Report
1.  Output a concise summary of what was completed.
