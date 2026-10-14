---
name: failure-archaeology
description: Never re-fight a settled battle. Discipline for recording and RETRIEVING past failures — gotchas, incidents, postmortems, dead ends, reverted fixes — as symptom → root cause → evidence → status. Use before debugging anything that smells familiar, when an incident closes, when a fix gets reverted, when an approach is abandoned, or when asked to document a bug just solved, write a postmortem, do failure archaeology, incident memory, or "did we hit this before". Not for capturing general knowledge (use brain_capture / brain_write) or live task tracking.
owner: platform
created: 2026-07-05
created_by: claude-fable-5
validated_on: 2026-07-06 blind eval — zero-context Sonnet runner discovered the skill via skill_search and produced _chronicle-codex-oauth.md (11 entries) + _chronicle-qmd.md (9 entries); separate judge verdict PASS/PASS, no defects
sources: adapted from tomicz/fable-5-train-opus-skills (failure-archaeology pattern, MIT), built on the reference deployment's existing knowledge/platform/gotchas/ practice
---

# Failure Archaeology

the reference deployment already pays for its lessons — `knowledge/platform/gotchas/` holds ~90 entries (91 files incl. _index.md, counted 2026-07-05). The failure mode is not capture, it's **retrieval**: an agent burns 40 minutes re-deriving why Codex OAuth died when `openai-codex-refresh-token-reused-2026-05-14.md` already settled it. This skill makes the archive load-bearing in both directions.

## The rule that matters most

**Before investigating any failure, search the archaeology first.** 60 seconds of search beats re-fighting a settled battle:

```
brain_search("<distinctive error string or symptom keyword>")
brain_search("<system name> <failure verb>")   # e.g. "codex auth", "qmd hang", "mcp timeout"
brain_list("knowledge/platform/gotchas")        # scan filenames — they are date-stamped symptom slugs
```

If a hit explains your symptom: read it, apply the settled fix, and note in your output that the archaeology resolved it. If a hit is *close but different*, say explicitly how your case differs — that difference is the new entry's opening line.

## When to write an entry

Write to `knowledge/platform/gotchas/<symptom-slug>-YYYY-MM-DD.md` when ANY of:
- An investigation took >20 minutes and ended in a root cause.
- A fix was **reverted** or an approach **abandoned** — dead ends are the highest-value entries because they are invisible in the final system.
- The same symptom appeared for the second time (recurrence = the first entry failed retrieval; improve its keywords too).
- An external system behaved contrary to its docs (API quirks, auth flows, rate limits).

## Entry format (the four fields that make it retrievable)

```markdown
# <Symptom in plain words> — YYYY-MM-DD

**Symptom:** what was observed, with the LITERAL error strings (future agents grep these).
**Root cause:** the actual mechanism, 2-4 sentences. Not the fix — the WHY.
**Evidence:** commands run + output that proved it (paths, dates, numbers).
**Status:** settled | open | recurring (Nth time: link prior entries)

**Fix / decision:** what was done or deliberately NOT done.
**Wrong paths tried:** approaches that looked right and weren't — one line each, so nobody retries them.
```

Rules:
- **Literal error strings verbatim** — retrieval works by substring; "token error" finds nothing, `refresh_token_reused` finds the entry.
- **Symptom in the filename**, not the fix ("mcp-timeout-long-deliberations" not "async-job-pattern").
- One incident per file. If a root cause explains several symptoms, one file owns the cause, others link it.
- No secret values in evidence — variable names and file paths only.

## Consolidation (quarterly, or when a domain accumulates 5+ entries)

Individual entries answer "did we hit this?"; a **chronicle** answers "what does this system keep teaching us?". When a domain (Codex auth, QMD, MCP transport…) accumulates entries, write/update a chronicle doc `knowledge/platform/gotchas/_chronicle-<domain>.md`: a table of symptom → root cause → status → entry link, ordered by date, with the standing invariant extracted on top (e.g. *"Codex refresh tokens are single-use; any sharing across profiles eventually kills all of them — gotcha entries 2026-05-14, 05-20, 05-25, 05-26, plus the 2026-07-03 channel change recorded inside codex-handoff/SKILL.md"*). The chronicle is the transfer of criterion; entries are its evidence.

## Guardrails

| ❌ | ✅ |
|---|---|
| Start debugging a familiar smell from scratch | brain_search the symptom first, always |
| Write the war story (chronology of your session) | Extract symptom/cause/evidence/status; the session narrative dies with the session |
| Record only what worked | Record reverted fixes and dead ends explicitly |
| Paraphrase error messages | Paste them verbatim — they are the search keys |
| Treat recurrence as bad luck | Recurrence = retrieval failure; strengthen the old entry's keywords + link entries |
| Bury root causes in daily memory/ files only | memory/ is a diary; gotchas/ is the archive. Cause goes to gotchas, memory links it |

## Verification

Entry is done when: `brain_search("<its literal error string>")` returns it, status field present, and no secret values inside. Chronicle is done when every linked entry resolves via `brain_read`.

## Cross-references

- Capture tools: `brain_capture`, `brain_write` (general knowledge — not failure-specific)
- Debug delegation with gotcha-doc requirement built in: internal `codex-handoff` skill, template B (not included in this public package)
- Audit that uses closed-loop evidence: [brain-due-diligence](../brain-due-diligence/SKILL.md)
- Exemplary existing entries: `knowledge/platform/gotchas/openai-codex-refresh-token-reused-2026-05-14.md`, `knowledge/platform/gotchas/qmd-vps-raw-overindexing-and-embed-hang-2026-06-01.md`

## Provenance and maintenance

- Gotchas dir + ~95 entries: verified 2026-07-05 via `brain_list("knowledge/platform/gotchas")`. Re-verify the same way.
- No chronicles exist yet as of 2026-07-05 (first candidates: Codex/OAuth auth — 4+ entries; QMD — 6+ entries).

## Cambios

| Fecha | Cambio | Por |
|---|---|---|
| 2026-07-05 | Created — tomicz failure-archaeology pattern grafted onto existing the reference deployment gotchas practice; adds retrieval-first rule, entry format, chronicles. | Claude Code (Fable 5) |
