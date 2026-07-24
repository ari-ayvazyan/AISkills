---
name: architecture-decisions
description: >
  ALWAYS Execute this skills before deciding any
  technical/architectural matter, to avoid reintroducing already-solved issues.
---

Maintains a compact architecture_log.md recording every
architectural decision (WHAT + WHY) when a technical topic is introduced,
removed, or changed. ALWAYS read architecture_log.md before deciding any
technical/architectural matter, to avoid reintroducing already-solved issues

Keep a running architecture log. Read it before deciding; append to it after deciding.

## When active

Always. This skill governs every technical/architectural decision in the session.

## Read before deciding

BEFORE settling any architectural choice — library/framework, data store, API shape, auth, build tooling, module boundary, concurrency model, error-handling strategy, deployment target, naming convention, or any decision that constrains future code — read `architecture_log.md` (project root; check `docs/` if absent).

Purpose: do not re-litigate or reintroduce something already decided or already rejected. If a candidate choice contradicts a logged decision, surface it -> "contradicts log entry [date/topic], reopen?" before proceeding.

If the file does not exist, create it lazily the first time a decision is made.

## Write after deciding

When a decision is **introduced**, **removed**, or **changed**, append an entry. Trigger on real architectural moves, not trivia (variable renames, formatting, one-off bugfixes).

## Format

Super compact. Use `->` for reasoning instead of full sentences. One entry = one decision. Newest at top.

```
## <topic> [INTRODUCED | REMOVED | CHANGED]
WHAT: <the decision, one line>
WHY: <driver -> consequence -> chosen because ...>
```

Compactness is the default. **Exception:** when brevity would create ambiguity, lose nuance, or risk misreading a future reader, use as many words as needed for clarity — correctness beats terseness.

For CHANGED/REMOVED, name what it replaces -> link the old topic so the history reads as a chain.

## Examples

```
## state management [CHANGED]
WHAT: Redux -> Zustand for client state.
WHY: Redux boilerplate -> slow feature velocity; app state is small/local ->
     Zustand enough. (Supersedes 2025-11-02 Redux entry.)

## API pagination [INTRODUCED]
WHAT: cursor-based pagination, not offset.
WHY: offset drifts on inserts -> dup/missing rows; cursor stable under writes.

## Background jobs [REMOVED]
WHAT: dropped in-process setInterval workers.
WHY: lost on restart + no retry -> moved to durable queue (see queue entry).

## Job queue [INTRODUCED]
WHAT: BullMQ on Redis for async jobs.
WHY: need durability + retries + visibility; Redis already in stack -> no new infra.

## Auth tokens [INTRODUCED]
WHAT: short-lived JWT (15m) access + rotating refresh token in httpOnly cookie.
  Rationale spelled out because the tradeoff is subtle: a longer-lived access
  token would reduce refresh traffic but widens the theft window, and storing
  the access token in JS-readable storage invites XSS exfiltration — so the
  access token stays short and out of localStorage, refresh stays httpOnly.
WHY: balance XSS exposure vs refresh load -> chosen as above.
```

## Persistence

Stay active for the whole session once a project is in scope. Do not drift: every later architectural decision still gets a read-before / write-after pass.
