---
name: skill-authoring-standards
description: the reference deployment standard for writing and editing canonical skills (SKILL.md) in the Brain. Use whenever you create a skill, write a skill, edit a skill, review a skill draft, or convert a runbook/gotcha/process into a skill. Covers frontmatter, trigger quality, description keywords, structure, when-not-to-use, provenance, and the failure-mode taxonomy. Not for deciding WHICH skills to create (use suggest-skills) or for grading existing skills (use skill-evaluation).
owner: platform
created: 2026-07-05
created_by: claude-fable-5
sources: adapted from dzhng/skills (write-skills), davidondrej/skills (effective-agent-skills), tomicz/fable-5-train-opus-skills (authoring rules) — all MIT; synthesized for the reference deployment
---

# Skill Authoring Standards

A skill is **transfer of criterion, not a checklist**. The bar: a zero-context Sonnet-class agent (or GPT-5.5 swarm agent, or a new employee's Claude Desktop) reads only this file and behaves like someone who already made the mistakes. If a skill doesn't change what the agent actually does, it's prose, not a skill.

## When to write a skill (and when not)

- **Create** only after `skill_search` with 2-3 distinct keywords finds no existing home. If a close skill exists, **improve it instead** — duplication is how libraries rot.
- **Don't create** for: one-off tasks, things `brain_search` already answers, style preferences (those belong in the company master prompt), or anything you cannot verify (see Ground Truth).
- The decision of *what* deserves a skill belongs to [suggest-skills](../suggest-skills/SKILL.md). This skill governs *how* to write it once decided.

## The two surfaces: description routes, body executes

**Level 1 — frontmatter description (~100 tokens, always visible):** this is the ONLY thing an agent sees before deciding to load the skill. It must state *what the skill does* and *the literal situations that should trigger it*. Never summarize the workflow here — an agent that reads a workflow summary follows the summary and skips the body.

⚠️ **the reference deployment-specific (verified 2026-07-05):** `skill_search` is keyword/substring matching, NOT semantic. A multi-word query like "skill authoring write skills" can return zero results while "handoff" returns 13. Therefore the `description` (and body) must contain the **literal single keywords** an agent would search: write the words "spec", "handoff", "screenshot", not just their concepts. Include Spanish trigger words too when the team would say them ("nóminas", "vacaciones"). And because results are UNRANKED and the library has 350+ skills, common words drown ("skill" → 301 hits, "spec" → 267): every description needs at least one RARE distinctive keyword (returns <20 hits) — test it after writing.

**Level 2 — body (< ~2,500 words):** the how. If it grows beyond that, split reference material into `knowledge/skills/<slug>/references/*.md` and link it (Level 3). One skill = one job; a skill that bundles mission-tracking + execution + reporting is a framework, not a skill.

## Frontmatter (mandatory)

```yaml
---
name: <kebab-case, matches folder name>
description: <what it does + "Use when..." with literal trigger keywords + "Not for X (use <sibling>)">
owner: <platform | finance | marketing | retail | cs | hr | merch>
created: YYYY-MM-DD
created_by: <who/which model wrote it>
validated_on: <first real run that proved it works — add when it happens>
---
```

Add `stale_after: YYYY-MM-DD` when the skill contains volatile facts (versions, node maps, API endpoints).

## Structure (house template)

1. **Title + one-paragraph mission** — what this skill makes possible, in one breath.
2. **When to invoke / when NOT to** — trigger table if triggers are many; always include at least one "not for X → use [sibling]" pointer.
3. **Protocol** — numbered phases, each ending in an explicit completion criterion ("done when Y is observable"). Copy-pasteable commands with absolute paths. Imperative voice.
4. **Guardrails / Anti-patterns** — the ❌/✅ table. Each row earned by a real mistake, stated as the *smell*, not the war story.
5. **Verification** — how the agent proves the output is right *before* reporting done. Evidence, not vibes: command output, skill_search result, screenshot, diff.
6. **Provenance and maintenance** — where volatile facts came from + one-line re-verification commands for anything that may drift (e.g. "node map: re-verify with `brain_read knowledge/platform/agents/hermes-all-agents-migration-2026-07-05.md`"). Date-stamp volatile facts inline (`(verified 2026-07-05)`).
7. **Cross-references** — link related skills/docs by Brain path. **One home per fact**: if another doc owns a fact, link it, never copy it.
8. **Cambios** — changelog table (date, change, author).

## Ground truth only

- Verify every command, flag, path, tool name, and claim **before** writing it. A wrong runbook is worse than none — it sends a cheap model confidently down a wrong path it can't recognize.
- If a tool doesn't exist at the reference deployment, don't reference it: name the the reference deployment equivalent or mark it explicitly as *future candidate*.
- Unproven approaches stay labeled *open/candidate*. No oversell.
- Never paste secrets, tokens, or credential values — reference env var names or where credentials live.
- Prefer Brain paths over personal/local paths. A load-bearing step must not depend on one person's laptop; if it currently does (e.g. a Mac-only harness), say so explicitly.

## Examples document the problem, not the solution

Bake in the *smell/symptom* that should trigger judgment ("if red numbers equal green numbers, your revert didn't take"), never today's fix, file, or line number. Code changes; pointers rot; criterion survives.

## Failure-mode taxonomy (diagnose drafts against this)

| Mode | Smell |
|---|---|
| **Premature completion** | skill lets the agent declare done without evidence |
| **Embargo** | protocol order delays surfacing a critical finding — disclosure must never wait for step order |
| **Lucky pass** | works on the happy path only; no failure branches |
| **Duplication** | restates what another skill/doc owns → link instead |
| **Sediment** | stale facts nobody re-verifies → provenance section missing |
| **War story** | narrates the original incident instead of extracting the rule |
| **Implementation index** | points at today's file/line/value instead of teaching the judgment |
| **Sprawl** | tries to be a framework; can't say its job in one sentence |
| **No-op** | reads fine, changes no behavior — delete it |

## Rules that must not break

1. Absolute ALWAYS/NEVER only with the exception stated inline — an absolute rule with unstated edge cases gets silently ignored.
2. Separate **Constraints** (MUST NOT) from **Conventions** (usually do) — mixing them teaches agents that constraints are negotiable.
3. Match strictness to fragility: exact scripts for fragile/irreversible operations, loose heuristics for judgment tasks.
4. Skills distribute via Brain canonical + `skill_read`/`skill_search` — **never copy SKILL.md to nodes** unless a runtime specifically requires it (see [swarm-propagation](../swarm-propagation/SKILL.md) type F).

## Ship checklist

```
□ skill_search dedup done (2-3 keyword queries, results reviewed)
□ Frontmatter complete; description has literal trigger keywords (ES+EN where relevant)
□ Every command/path verified against the real system
□ When-NOT-to-use + sibling pointer present
□ Verification section gives evidence, not vibes
□ Provenance section lists re-verification commands for volatile facts
□ Draft diagnosed against the failure-mode taxonomy
□ Post-write: skill_search("<distinctive keyword>") returns the new skill
□ Propose an eval case for skill-evaluation (builder ≠ judge)
```

## Cross-references

- What to create: [suggest-skills](../suggest-skills/SKILL.md)
- How to grade: [skill-evaluation](../skill-evaluation/SKILL.md)
- Distribution: [swarm-propagation](../swarm-propagation/SKILL.md) (type F)
- Mandatory pre-execution review: `knowledge/platform/rules/brain-skills-review-before-execution.md`

## Provenance and maintenance

- skill_search behavior (keyword/substring, multi-word fails): observed live 2026-07-05. Re-verify: `skill_search("skill authoring write skills")` (expect 0) vs `skill_search("authoring")` (expect ≥1).
- Canonical skills location `knowledge/skills/<slug>/SKILL.md`: re-verify with `brain_list("knowledge/skills")`.

## Cambios

| Fecha | Cambio | Por |
|---|---|---|
| 2026-07-05 | Created — synthesis of dzhng write-skills, davidondrej effective-agent-skills, tomicz authoring rules, adapted to the reference deployment Brain/skill_search reality. | Claude Code (Fable 5) |
