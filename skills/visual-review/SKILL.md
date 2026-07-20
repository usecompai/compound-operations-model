---
name: visual-review
description: Verify visual work with evidence instead of vibes — screenshot critique by a fresh judge, before/after comparison, crops of the disputed detail, and a distance-not-verdict mindset. Use when reviewing a UI, landing, email template, dashboard, canvas, or design change; when doing a screenshot critique, comparing screenshots, doing visual QA or UI QA on a landing page, checking a clone against a reference, or before declaring any visual deliverable done. Not for choosing a design direction or running a dedicated accessibility audit.
owner: platform
created: 2026-07-05
created_by: claude-fable-5
sources: adapted from dzhng/skills (screenshot-critique, compare-screenshots — MIT)
---

# Visual Review

the reference deployment rule (the founder, formalized ~jun-2026): **visual verification is mandatory before shipping visual work, and the implementer's word is not verification.** This skill is the how. It rests on one bias-killer: the person who built the thing cannot be the only one who looks at it.

## When to invoke

Any deliverable a human will *look at*: your storefront changes, email templates, dashboards, decks, canvases, generated images, UI clones. Especially when Codex implemented it — Codex never designs and often never *sees* its own output rendered; the orchestrator owns the looking.

## Protocol

### 1. Capture real evidence

Screenshot the actual rendered artifact (real browser, real email client preview, real device width when it matters — mobile is where the reference deployment traffic is). Tools by context, whatever is available on the node: `pp-agent-capture` (the founder's Mac), `canvas` snapshot (OpenClaw/Hermes nodes), browser preview/screenshot tooling. A code diff or the implementer's own screenshot is NOT capture.

### 2. Crop before judging

Make 2-4x **crops of every element under judgment** (the button, the spacing, the typography pair). Full-page screenshots hide small defects; if the complaint is "too faint" or "misaligned", the crop is mandatory, not optional.

### 3. Fresh judge, unprimed

Spawn/ask a separate agent with **zero context about intent or effort** — only the screenshots + crops + a neutral prompt: *"List concrete visible defects: alignment, spacing, typography, color, contrast, truncation, overflow, inconsistent states. Cite the crop each defect appears in."* Do not tell it what you changed or what you hope it says. Defects the judge finds independently that you also suspected = highest-priority fixes.

### 4. Comparisons: establish ground truth BEFORE looking at the diff

When comparing two versions (before/after, candidate vs reference):
- **The baseline can be wrong too.** First state, from the brief/brand/reference, what the image *should* show. Only then compare. "Closer to the baseline" is not "better" if the baseline had the bug.
- Judge **which is less wrong against the ground truth**, element by element (layout, density, color, type, states) — not holistically ("feels better" is not a finding).
- Call any numeric similarity a **distance, never a verdict** — pixels can match while the one thing that matters is broken, and differ harmlessly everywhere else.
- If the call is a genuine taste call → stop and ask the founder with both images + your recommendation. Don't default to either version.

### 5. Loop

Fix the biggest defect, re-capture, re-judge. Taste-dependent work is never one pass (see the internal `fable-prompting` skill, section 5). Stop when the fresh judge finds no material defects, or the founder accepts.

## Brand gate (the reference deployment-specific, mandatory)

Before the loop starts, the artifact must comply with the company's current brand guidelines: approved logo assets, type, color, spacing and accessibility rules. A pixel-perfect artifact with a placeholder logo still fails.

## Guardrails

| ❌ | ✅ |
|---|---|
| "Code merged, looks right in the diff" | Rendered screenshot or it didn't happen |
| Builder critiques own output and ships | Fresh unprimed judge, screenshots only |
| Full-page screenshot as the only evidence | Crops of every judged element |
| "97% pixel match → done" | Distance is a signal; the judge's element-by-element findings decide |
| Baseline treated as truth | Ground truth from brief/brand first; baseline is just an earlier attempt |
| Judge told "I improved the spacing, confirm" | Neutral prompt; priming the judge deletes its value |
| One pass on taste-dependent work | Loop until judge finds no material defects |

## Verification

Done when: evidence pack exists (screenshots + crops + judge output), material defects fixed with re-capture proof, brand gate passed, and taste calls (if any) explicitly resolved by the founder — not silently by the builder.

## Cross-references

- Design research upstream: the company's design-research and brand-guideline sources.
- Builder != judge doctrine: internal `fable-prompting` skill (not included in this public package)
- Visual gates inside specs: [spec-driven-execution](../spec-driven-execution/SKILL.md)
- Codex-never-designs rule: `knowledge/platform/rules/` (design/hosting rules) + the founder's standing instruction

## Provenance and maintenance

- Capture tools per node (pp-agent-capture / canvas / browser tooling): availability drifts — re-verify with `skill_search("capture")` / `skill_search("canvas")` before instructing a specific node.

## Cambios

| Fecha | Cambio | Por |
|---|---|---|
| 2026-07-05 | Created — dzhng screenshot-critique + compare-screenshots distilled; brand gate + Codex-never-designs integration. | Claude Code (Fable 5) |
