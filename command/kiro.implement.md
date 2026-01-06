---
description: Implement all tasks from a .kiro spec file using subagents
---

# Kiro Sequential Subagent Implementation Workflow

Your goal is to orchestrate subagents to implement ALL pending tasks in a Kiro spec file sequentially. You are the **supervisor** - you do not implement tasks yourself, you delegate to subagents and ensure they complete their work.

## 1. Locate Task File

1. Search for `tasks.md` files in `.kiro/specs/`.
2. **FILTER:** Exclude any paths containing the string `--complete--` (these are already done).
3. Sort the remaining files by their directory prefix (e.g. `03`, `04`) to ensure sequential processing.
4. Select the first `tasks.md` file found.
5. If no `tasks.md` is found in a non-complete directory, stop and report "No pending specs found".

## 2. Parse and Clean Tasks

1. Read the entire `tasks.md` file.
2. **Read Context:** Read `requirements.md` and `design.md` (if they exist in the spec directory). This ensures you understand the architectural goals and "why" behind the tasks.
3. **Cleanup Step:** Before processing, perform a cleanup pass:
   - **Parent Tasks:** If a parent task is unchecked `[ ]` but **ALL** its indented subtasks are checked `[x]`, automatically mark the parent as `[x]` in the file. Do not spawn a subagent for this.
   - **Duplicates:** If you find clear duplicate task lines, mark the duplicates as `[x]`.
4. Create a todo list of the remaining pending tasks (`- [ ]`).
   - Focus on "leaf" tasks (tasks with no subtasks) or tasks where subtasks are incomplete.
   - Note the line number and exact content of each task.

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
   - Instructions to run the project's build and ALL tests, fixing any issues until they pass successfully
   - Instructions to report back what was done and confirm successful verification

2. Example subagent prompt structure:
   ```
   You are implementing a task from a Kiro spec.
   
   TASK FILE: [path to tasks.md]
   TASK TO IMPLEMENT: [exact task text]
   
    Instructions:
    1. Read the tasks.md and any sibling files (design.md, requirements.md) for context
    2. Implement the task completely - write code, create files, refactor as needed
    3. Run the project's build command and ALL relevant tests to verify your work
    4. CRITICAL: If the build or tests fail, you MUST fix the issues and re-run them until they pass before reporting completion.
    5. Report back:
       - What you implemented
       - Confirmation that the build and tests passed successfully
       - Any issues you encountered and how you fixed them


   
   Do NOT mark the task as complete in tasks.md - the supervisor will do that.
   ```

### 3.3 Verify Subagent Completion
1. Review the subagent's response carefully.
2. If the subagent reports SUCCESS:
   - Edit `tasks.md` to change the task status from `[-]` to `[x]`.
   - Update your todo list to mark this task as completed.
   - Create a git commit:
     - Stage all changes (`git add .`)
     - Commit with message "kiro: [task description]" (e.g. "kiro: Add login page")
3. If the subagent reports FAILURE or issues:
   - Spawn a NEW subagent to fix the issues or retry the task.
   - Repeat until the task is successfully completed.
   - Only then mark as `[x]` and commit.

### 3.4 Continue to Next Task
1. Move to the next pending task in the file.
2. Repeat steps 3.1-3.3.

## 4. Completion

1. Once ALL tasks in the `tasks.md` file are marked `[x]`:
   - Output a summary of all completed tasks.
   - Report any tasks that required retries and why.
   - Rename the spec folder to mark it as complete:
     - Identify the spec folder containing `tasks.md` (e.g., `.kiro/specs/01-login`).
     - Construct the new name by inserting `--complete--` after the initial number (e.g., `01-login` becomes `01--complete--login`).
     - Use the Bash tool to rename the folder: `mv "path/to/01-login" "path/to/01--complete--login"`.

## Important Rules

- **You are the supervisor**: Do NOT implement tasks yourself. Always delegate to subagents.
- **Sequential execution**: Wait for each subagent to complete before starting the next task.
- **Persistence**: If a subagent fails, retry with a new subagent until the task succeeds.
- **Verification**: Always verify the subagent's work by checking their response before marking complete.
- **Single responsibility**: Each subagent handles exactly ONE task.
