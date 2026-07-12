---
name: spec-driven-execution
description: Turn a big or ambiguous technical task into a spec of independently verifiable slices, implement slice-by-slice with verification gates, and close the spec with a claim audit. Use when asked to write a spec, implement a spec, plan a build, break down a feature, structure a multi-day or multi-week technical project or migration, or when a Codex/agent delegation is too big for one self-contained prompt. Not for small tasks (single codex-handoff prompt suffices) or non-technical plans.
owner: platform
created: 2026-07-05
created_by: claude-fable-5
sources: adapted from dzhng/skills (write-spec, implement-spec, close-spec — MIT), integrated with the reference deployment codex-handoff and 3-phase methodology
---

# Spec-Driven Execution

The the reference deployment 3-phase rule (Research → Plan → Implement) says a plan must exist; this skill defines what a plan that survives contact with execution looks like: a **spec made of independently verifiable slices**, each small enough to hand to Codex or a swarm agent as one self-contained prompt, each verifiable without trusting the implementer's word.

## When to invoke / when not

- **Invoke:** task needs >1 delegation, touches >1 system, will take >1 session, or has ambiguity that would make a single [codex-handoff](../codex-handoff/SKILL.md) prompt a guess.
- **Skip:** one script, one fix, one clear deliverable → go straight to codex-handoff. A spec for a 30-minute task is bureaucracy.

## What an independently verifiable slice is

A slice earns its place when it has all four:
1. **A seam** — the interface it exposes (function signature, file contract, API shape, data format). Named, so the next slice can build against it before this one is perfect.
2. **A playable artifact** — something a human or agent can RUN to see it work (CLI probe, test page, dry-run command, sample output file). Not "the code exists".
3. **A verification gate** — the explicit check that must pass (test command, expected output, screenshot comparison, reconciliation number). The gate is written in the spec BEFORE implementation, so the implementer can't negotiate it afterward.
4. **Independence** — buildable and verifiable without unrelated slices existing first. Independent slices can run as parallel delegations.

If a slice hides multiple variables or contains a broad verb ("make it robust", "clean up the data"), it is fog — **re-slice it recursively** until every leaf has one question, one seam, one verdict.

## Protocol

### Phase 1 — Write the spec

1. **Research first** (the reference deployment rule): Brain (`brain_search`), source systems, reference implementations. Document what is settled vs open.
2. **For high-stakes specs, draft blind in parallel:** give 2-3 fresh subagents the same brief independently and compare. Where drafts agree → firm ground. Where they diverge → that's exactly where to think hardest before committing. (Skip for routine specs.)
3. **Materialize** to ONE canonical location:
   - Code work in a repo → `specs/<feature>/README.md` in that repo.
   - Brain/platform/ops work → `knowledge/projects/<project>/spec-<feature>.md`.
4. Spec structure: goal + hard bar (see [fable-prompting](../fable-prompting/SKILL.md)) · slice list with seams/artifacts/gates · dependency order (what can run in parallel) · out-of-scope list (explicit) · **Next Agent Prompt** — a final section written in second person that lets a fresh zero-context agent pick the work up with no chat history. If you can't write that section, the spec isn't done.

### Phase 2 — Implement, one slice = one pass

For each slice, in dependency order (independent slices → parallel delegations):
1. Delegate or implement the slice (delegation → codex-handoff, with the slice's gate pasted in as the success criteria).
2. **Run the verification gate yourself.** The implementer's report is a claim, not evidence. A sandboxed/delegated implementer ships code it never saw run — the orchestrator verifies in the real environment (browser, real API, real data).
3. Mark the slice done IN THE SPEC with the evidence (command + output, screenshot path, number).
4. Every 2-3 slices, or after any failed gate: **maintenance checkpoint** — re-read the spec; prune slices reality invalidated; log plan deviations as new open questions. A spec that contradicts the codebase is worse than none.
5. **Do not stop while open slices remain** unless: a gate fails un-fixably (→ re-scope, don't patch around — the reference deployment rule: revert & re-scope), a hard-stop trigger appears, or budget/timebox is reached.
   **Hard-stop triggers (automatic, never a judgment call):** production deploy/restart, spend or budget change, credentials/auth changes, any deletion of existing data/files, customer-facing/HR/legal/external communications, company master prompt or governance-doc changes, multi-node rollout. A slice touching ANY of these pauses for the founder's explicit OK before executing that slice — same list as [fable-prompting](../fable-prompting/SKILL.md) house rules.

### Phase 3 — Close the spec

When all gates are green:
1. Rewrite the spec doc from *build plan* into *rationale record*: why it's built this way, the invariants that must hold, the dead ends tried (→ also file per [failure-archaeology](../failure-archaeology/SKILL.md)), pointers into the final system. Delete the slice ladder.
2. **Claim audit by a fresh agent:** every remaining statement in the closed doc gets checked against the real system by someone who didn't write it. Stale claims are defects that block closing.
3. Move/mark it closed (`specs/done/` in repos; status line in Brain docs) and record durable learnings via `brain_write`.

## Guardrails

| ❌ | ✅ |
|---|---|
| Slices split by file/layer ("backend part", "frontend part") | Slices split by verifiable behavior |
| Gate defined after implementation | Gate written in the spec before any code |
| "Implementer says tests pass" = done | Orchestrator runs the gate; evidence in the spec |
| Spec grows stale while code moves on | Maintenance checkpoint every 2-3 slices |
| Broad verbs survive slicing ("improve", "robust") | Recursive re-slice until one variable per slice |
| Spec closed as-is, full of stale build notes | Rationale rewrite + fresh-agent claim audit |
| Weakening a gate so a slice passes | Gates only change at maintenance checkpoints, stated explicitly, with reason |

## Verification

Spec phase done when the Next Agent Prompt exists and a zero-context read makes sense. Implementation done when every slice shows evidence. Close done when the claim audit found zero stale claims.

## Cross-references

- Per-slice delegation mechanics: [codex-handoff](../codex-handoff/SKILL.md)
- Goal/bar/loop doctrine the spec header follows: [fable-prompting](../fable-prompting/SKILL.md)
- Session-boundary transfer of an in-flight spec: [session-handoff](../session-handoff/SKILL.md)
- Dead ends discovered during implementation: [failure-archaeology](../failure-archaeology/SKILL.md)
- Visual gates: [visual-review](../visual-review/SKILL.md)

## Provenance and maintenance

- the reference deployment 3-phase methodology + revert-and-re-scope rule: company master prompt / `~/.claude/CLAUDE.md` "Metodología de Trabajo". Re-verify there if this drifts.

## Cambios

| Fecha | Cambio | Por |
|---|---|---|
| 2026-07-05 | Created — dzhng spec loop (slices/gates/blind drafts/claim audit) adapted to the reference deployment delegation reality. | Claude Code (Fable 5) |
