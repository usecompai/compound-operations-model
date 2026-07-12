---
name: skill-evaluation
description: Evaluate whether a the reference deployment skill actually works — blind runner + separate judge against a bar, rubric scoring, pass-rate on re-runs, and defect diagnosis. Use when asked to evaluate a skill, eval skills, run a blind eval, score against a rubric, test a skill, audit skill quality, grade a skill, review the skill library, or before promoting a new skill to the company master prompt or the whole swarm. Not for writing skills (use skill-authoring-standards) or deciding which to create (use suggest-skills).
owner: platform
created: 2026-07-05
created_by: claude-fable-5
sources: adapted from dzhng/skills (eval-skills, MIT) + the reference deployment local skill-eval-harness criteria
---

# Skill Evaluation

A skill that has never been evaluated is a hypothesis. This skill turns "looks good" into evidence: a **fresh runner** executes the skill on a realistic case, a **separate judge** grades the artifact against a bar, and misses get diagnosed before anything is rewritten. **The builder of a skill is never its only judge.**

## When to invoke

- A new skill was just written (minimum: static rubric, ideally one blind run).
- Before a skill is referenced in the company master prompt or propagated swarm-wide.
- Quarterly library audit, or when an agent visibly misused/ignored a skill in the wild.
- After editing a skill to fix a failure — re-test **all** its cases, not just the one that failed.

**Not for:** grading one-off outputs (use `review-output` if available locally, or a judge subagent), or evaluating loops (use `loop-library` audit criteria).

## Two evaluation modes — pick deliberately

- **Judgment mode (default):** the judge holds the artifact to a *bar* ("a zero-context agent following this would not lose data") — not to an expected output. Most the reference deployment skills encode judgment; grading them against a fixed checklist degenerates into conformance theater that stops testing the judgment.
- **Conformance mode (only for fragile/mechanical skills):** exact expected outputs/commands, byte-level where it matters (e.g. rollout steps, API auth headers).

## Protocol

### Phase 1 — Static rubric (~10 min, no execution)

Score the SKILL.md itself, 0/1 per row:

| # | Criterion |
|---|---|
| 1 | Frontmatter complete; description states what + literal trigger keywords |
| 2 | Trigger test: would `skill_search` with the obvious keyword actually surface it? (run it) |
| 3 | When-NOT-to-use present with sibling pointer |
| 4 | Protocol steps end in observable completion criteria |
| 5 | Output contract explicit (what the agent must return/produce) |
| 6 | Anti-patterns/gotchas present and earned (not generic filler) |
| 7 | Verification section demands evidence, not vibes |
| 8 | Provenance/maintenance: volatile facts date-stamped with re-verification commands |
| 9 | No unverified claims, no invented paths/commands (spot-check 3) |
| 10 | Size discipline: body ≤ ~2,500 words, references split out |
| 11 | No duplication: no fact owned by another doc restated here |
| 12 | Failure-mode scan: none of the taxonomy modes from [skill-authoring-standards](../skill-authoring-standards/SKILL.md) present |

≤7/12 → the skill needs work before any dynamic eval. Record the score in the eval report.

### Phase 2 — Blind run (the real test)

1. **Write a golden case**: a realistic input/task the skill should handle, WITHOUT hinting at the skill's internal steps. Include what a strong result must contain (the bar), kept hidden from the runner.
2. **Runner**: a fresh agent (subagent, or a cheap-tier session — Sonnet-class, since that's the real swarm consumer) gets ONLY the case + access to the skill. No conversation history, no author context.
3. **Judge**: a *different* fresh agent gets the runner's artifact + the bar. Prompt it to try to prove the output does NOT meet the bar. The judge never sees the runner's reasoning, only the artifact.
4. **Nondeterminism**: borderline results get 2-3 re-runs; report a **pass rate**, not a verdict. A skill that passes 1 of 3 is not fixed.

### Phase 3 — Diagnose before editing

For each miss, decide: **skill defect** (the skill misled or under-specified) vs **bad case** (the case demanded something outside the skill's job — fix the case or the bar, not the skill). Editing a skill to chase a wrong bar makes it worse. Map defects to the failure-mode taxonomy, fix, then re-run **all** cases.

### Phase 4 — Report

Write findings to `knowledge/platform/strategy/skill-eval-<scope>-<date>.md` (or the skill's own Cambios entry for a single-skill eval): rubric score, cases run, pass rate, defects found with taxonomy label, fixes applied, what remains open.

## Automated batch option (Mac-local, verified 2026-07-05)

the founder's Mac has a batch harness: `~/.claude/skills/skill-eval-harness/` → `cd /workspace && make skill-eval-harness` → report in `outputs/ai-native-ops/YYYY-MM-DD/skill-eval-harness/`. It runs static criteria (rubric rows 1-7 approximately) over local skills. **It only exists on the founder's Mac** — swarm agents apply Phase 1 manually. Porting it to the VPS is a future candidate (Codex task).

## Guardrails

| ❌ | ✅ |
|---|---|
| Builder grades own skill and ships | Separate judge, fresh context, tries to refute |
| Judge gets the expected output | Judge gets the bar; expected outputs only in conformance mode |
| One lucky pass = validated | Pass rate over re-runs on borderline cases |
| Failing eval → rewrite skill immediately | Diagnose defect-vs-bad-case first |
| Eval finds 12 weak skills → silently rewrite all | the change-approval rule: report the list, the founder decides ✅/❌ per skill |
| Runner is a frontier model | Runner matches the real consumer tier (Sonnet/GPT-5.5 class) |

## Verification

Done when: rubric scores recorded, at least one blind run per new skill with judge verdict, report path exists and is readable via `brain_read`.

## Cross-references

- Authoring standard the rubric enforces: [skill-authoring-standards](../skill-authoring-standards/SKILL.md)
- What to create/improve: [suggest-skills](../suggest-skills/SKILL.md)
- Adversarial judging for high-stakes outputs: [punta-de-flecha](../punta-de-flecha/SKILL.md)
- Builder≠judge doctrine: [fable-prompting](../fable-prompting/SKILL.md) §4

## Provenance and maintenance

- Mac harness path + make target: verified 2026-07-05 by reading `~/.claude/skills/skill-eval-harness/SKILL.md`. Re-verify: `ls /workspace/Makefile` on the Mac.
- Swarm consumer tiers (Sonnet/GPT-5.5): re-verify `brain_read("knowledge/platform/agents/model-routing-real-2026-07-04.md")`.

## Cambios

| Fecha | Cambio | Por |
|---|---|---|
| 2026-07-05 | Created — dzhng eval-skills blind-run/judge/pass-rate mechanics + the reference deployment local harness rubric, adapted to Brain + swarm tiers. | Claude Code (Fable 5) |
