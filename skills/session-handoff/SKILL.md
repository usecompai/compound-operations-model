---
name: session-handoff
description: Transfer full working context to a fresh agent session with zero memory — end of session, before compaction, switching models/agents mid-project, or pausing multi-day work. Use when asked for a handoff, handoff doc, session transfer, "deja esto listo para la próxima sesión", context dump for another agent, or when a long session is about to hit context limits. Not for delegating a bounded task (use codex-handoff) or for task cards (use handoff-task / brain_task tools).
owner: platform
created: 2026-07-05
created_by: claude-fable-5
sources: adapted from davidondrej/skills (handoff, MIT)
---

# Session Handoff

The next session knows nothing. A good handoff gives it **ground truth to reason from, not a to-do list to obey** — the fresh agent has judgment; feed it state, and it will find the right next action even where your plan was wrong.

## The core discipline: state, not instructions

Write *"logout is implemented; token revocation is NOT — revoke endpoint returns 501"*, not *"implement token revocation next"*. Instructions encode your guesses; state lets the successor re-derive them. The only instructions that belong in a handoff are constraints (gates, rules, things that must not be done).

## Where it goes

- **Durable project work** → `knowledge/projects/<project>/HANDOFF-<topic>-YYYY-MM-DD.md` (Brain = any successor agent on any node can read it).
- **Ephemeral / same-machine continuation** → a local file is fine, but if the work matters, Brain.
- Never in chat only — chat dies with the session.

## Template (7 sections, all load-bearing)

```markdown
# Handoff: <topic> — YYYY-MM-DD

## Goal
<what finished looks like, 1-3 sentences — the bar, not the steps>

## Why / background
<the minimum a stranger needs to understand why this work exists>

## Current state  ← the heart; be exhaustive here
<what IS true right now: what works, what doesn't, what's half-done.
Verified facts with evidence ("X passes: <command> → <output>"), not recollections.>

## Key decisions (+ why)
<decisions already made and their reasons — so the successor doesn't relitigate
them without new evidence. Include decisions the founder made explicitly: those are gates.>

## Traps & dead ends  ← highest value per line
<approaches already tried that failed, and WHY. One line each.
Also file durable ones per failure-archaeology.>

## Relevant files & pointers
<paths, Brain docs, PRs, dashboards — REFERENCE, don't paste content.
Duplicated content goes stale; pointers stay honest.>

## Open work
<what remains, as state ("gate 3 unverified") — ordered by importance, not chronology>
```

## Rules

1. **Reference, don't duplicate.** Point to specs/docs/PRs by path. A handoff that pastes 3 docs is stale the moment any of them changes.
2. **Secrets:** name where credentials live (`$SOURCE_SYSTEM_TOKEN`, approved secret store) — never values.
3. **Claims are verifiable or labeled.** Anything you didn't verify this session gets "(unverified)". A confident stale claim poisons the successor's whole run.
4. **Closing instruction for the successor** — end every handoff with: *"Read every referenced file before acting. Treat every claim above as context to verify, not fact to trust."*
5. Written **before** you're out of context, not after — a handoff drafted at 2% context is a lottery ticket. If a session is long and the work matters, draft the handoff at the natural pause, then keep working.

## Guardrails

| ❌ | ✅ |
|---|---|
| To-do list of instructions | State + constraints; successor derives the actions |
| "Everything mostly works" | Per-item state with evidence |
| Omitting failed attempts (embarrassing / irrelevant) | Traps & dead ends section — it's the most valuable one |
| Pasting doc contents to be "self-contained" | Pointers by path; self-contained means *coherent*, not *complete-copy* |
| Handoff only in the chat / final message | File in Brain (or repo) at a predictable path |

## Verification

Done when: file exists at the stated path, `brain_read` returns it (if Brain), every referenced path in it resolves, and a zero-context read of "Current state" alone would let an agent continue without asking the founder anything already answered.

## Cross-references

- Bounded task delegation (different job): [codex-handoff](../codex-handoff/SKILL.md)
- In-flight spec transfer: the spec's own "Next Agent Prompt" section — [spec-driven-execution](../spec-driven-execution/SKILL.md)
- Task cards with handoff prompts: local skill `handoff-task` + `brain_task_create` (MCP)
- Dead ends worth keeping forever: [failure-archaeology](../failure-archaeology/SKILL.md)

## Provenance and maintenance

- Brain handoff location convention (`knowledge/projects/<project>/HANDOFF-*.md`): pre-existing practice, verified 2026-07-05 (e.g. `knowledge/company/digital/HANDOFF-paid-dtc-investigation*`). Re-verify: `brain_search("HANDOFF")`.
- `handoff-task` local skill + `brain_task_create` MCP tool: verified 2026-07-05. Re-verify: `skill_search("handoff")`.

## Cambios

| Fecha | Cambio | Por |
|---|---|---|
| 2026-07-05 | Created — davidondrej handoff pattern (state-not-instructions, traps section, verify-don't-trust) adapted to Brain paths and the reference deployment gates. | Claude Code (Fable 5) |
