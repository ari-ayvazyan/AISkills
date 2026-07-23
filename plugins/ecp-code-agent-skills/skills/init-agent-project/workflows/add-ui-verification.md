# Workflow: Add UI Verification Instructions

<required_reading>
No reference required.
</required_reading>

<process>
## Step 1: Check for an existing block

Read `AGENTS.md`. If a `## UI Verification` section already exists, stop — do not duplicate it.

## Step 2: Append the section

Append the following clearly-delimited section to `AGENTS.md`:

```markdown
## UI Verification

BEFORE doing a ui change use the playwright mcp to open the page containing the affected ui and create a screenshot of it. After your change is complete, create a second screenshot. Compare the Before/After to identify new ui issues, also issues that were created indirectly in other places. Also verify the UI/UX of the new component, are styling best practices followed? Does spacing look good? Does something feel too packed? Are visual weights balanced? etc. Once identified, fix all of those issues and repeat until they are solved.
```

## Step 3: Flag the dependency

This instruction relies on the **Playwright MCP**. If it is not installed for the selected agents, tell the user and suggest running `workflows/install-playwright-mcp.md`.
</process>

<success_criteria>
- [ ] `AGENTS.md` contains the UI Verification section exactly once (idempotent on re-run)
- [ ] Dependency on the Playwright MCP surfaced if it isn't installed
</success_criteria>
