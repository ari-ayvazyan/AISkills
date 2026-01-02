---
description: Implement all tasks from a .kiro spec file using subagents
---

# Kiro Sequential Subagent Implementation Workflow

Your goal is to orchestrate subagents to implement ALL pending tasks in a Kiro spec file sequentially. You are the **supervisor** - you do not implement tasks yourself, you delegate to subagents and ensure they complete their work.

## 1. Locate Task File

1. Search for `tasks.md` files in `.kiro/specs/`.
2. If an argument is provided ($ARGUMENTS), use it to filter the spec directory.
3. Otherwise, find the first `tasks.md` that contains pending tasks (`- [ ]`).
4. Read the selected `tasks.md` and note the full path.

## 2. Parse All Tasks

1. Read the entire `tasks.md` file.
2. Create a todo list of ALL pending tasks (`- [ ]`) found in the file.
3. Note the line number and exact content of each task.

## 3. Sequential Task Execution Loop

For EACH pending task, in order:

### 3.1 Mark Task In-Progress
1. Edit `tasks.md` to change the current task status from `[ ]` to `[-]`.

### 3.2 Spawn Subagent
1. Use the Task tool to spawn a `general` subagent with a detailed prompt that includes:
   - The exact task to implement (copy the task description verbatim)
   - The path to the `tasks.md` file
   - Instructions to read sibling context files (design.md, requirements.md, etc.)
   - Instructions to implement the task completely
   - Instructions to run tests/build/lint to verify
   - Instructions to report back what was done and whether it succeeded

2. Example subagent prompt structure:
   ```
   You are implementing a task from a Kiro spec.
   
   TASK FILE: [path to tasks.md]
   TASK TO IMPLEMENT: [exact task text]
   
   Instructions:
   1. Read the tasks.md and any sibling files (design.md, requirements.md) for context
   2. Implement the task completely - write code, create files, refactor as needed
   3. Run relevant tests, build, and lint to verify your work
   4. Report back:
      - What you implemented
      - Whether tests/build passed
      - Any issues encountered
   
   Do NOT mark the task as complete in tasks.md - the supervisor will do that.
   ```

### 3.3 Verify Subagent Completion
1. Review the subagent's response carefully.
2. If the subagent reports SUCCESS:
   - Edit `tasks.md` to change the task status from `[-]` to `[x]`.
   - Update your todo list to mark this task as completed.
3. If the subagent reports FAILURE or issues:
   - Spawn a NEW subagent to fix the issues or retry the task.
   - Repeat until the task is successfully completed.
   - Only then mark as `[x]`.

### 3.4 Continue to Next Task
1. Move to the next pending task in the file.
2. Repeat steps 3.1-3.3.

## 4. Completion

1. Once ALL tasks in the `tasks.md` file are marked `[x]`:
   - Output a summary of all completed tasks.
   - Report any tasks that required retries and why.

## Important Rules

- **You are the supervisor**: Do NOT implement tasks yourself. Always delegate to subagents.
- **Sequential execution**: Wait for each subagent to complete before starting the next task.
- **Persistence**: If a subagent fails, retry with a new subagent until the task succeeds.
- **Verification**: Always verify the subagent's work by checking their response before marking complete.
- **Single responsibility**: Each subagent handles exactly ONE task.
