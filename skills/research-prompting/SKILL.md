---
name: research-prompting
description: Write research prompts that come back decision-ready — zero-prior-knowledge framing, evidence hierarchy, fact/inference separation, and a mandatory gap round. Use when formulating a research prompt, deep research request, competitive research, market research, due diligence question, or when delegating research to exa_search, an agent, Codex, or an external researcher. Not for running the research itself end-to-end (deep-research, autoresearch, gemini-deep-research, exa_search EXECUTE research — this skill writes the brief that feeds them), not for the reference deployment strategic deliberation (use council/punta-de-flecha), and not for Brain lookups (brain_search first, always).
owner: platform
created: 2026-07-05
created_by: claude-fable-5
sources: adapted from davidondrej/skills (research-prompt, MIT)
---

# Research Prompting

Research quality is set at prompt time, not search time. A researcher — human, agent, or API — with a vague prompt returns a vague dump; the same researcher with a self-contained prompt and an explicit bar returns something you can decide on.

## Order of operations (the reference deployment, non-negotiable)

1. **Brain first.** `brain_search` the topic — if the reference deployment already paid for the answer, the research prompt shrinks or dies.
2. **Live data from source systems** (commerce, analytics, advertising, accounting…) — never ask external research for numbers we own. Shopify, not GA4, for revenue.
3. Only then: external research, with the prompt built below.

## The prompt: one self-contained paragraph

Write ONE paragraph (no headers, no bullets) that a researcher with **zero prior knowledge** can execute without a single clarifying question:

1. **Open with 1-2 sentences of plain-English context** — what the reference deployment/the project is *as relevant to this question* ("the reference deployment is a Spanish fashion brand, ~€10M revenue, DTC + retail…"). Never assume the researcher knows anything.
2. **The question, sharply bounded** — what exactly, over what time window, for which geography/segment, and what decision it feeds ("we will use this to decide whether to X").
3. **The evidence bar** — what sources count (see hierarchy below) and the output contract.
4. **What we already know/believe** — stated as beliefs to check, not facts, so the researcher challenges instead of confirming.

Constrain the **output hard, the method loosely** — specify exactly what comes back; let the researcher choose the path.

## Evidence hierarchy (goes in every prompt)

1. **Primary:** official docs, filings, earnings reports, papers, primary datasets, the company's own site/API.
2. **Secondary:** reputable press, named-analyst reports.
3. **Weak signal only:** forums, Reddit, X — usable as leads, **never as factual proof**.

On contradiction between sources: **do not force consensus.** Report both, labeled: fact (sourced) / inference (reasoned) / uncertainty (unresolved). A fake-consensus answer is worse than an honest split.

## Output contract (paste into the prompt)

> For every key finding: the specific claim + the source link + one line on why it matters for the decision. Corroborate load-bearing claims with a second independent primary source where possible; mark single-source claims as such. Before finishing, run a self-critique pass: list gaps, contradictions, and single-source claims, then do one more search round to close them. Separate throughout: fact / inference / uncertainty.

The self-critique + extra round is the **gap round** — it's mandatory. First-plausible-answer research is how bad decisions get confident.

## Execution routes (the reference deployment)

| Need | Route |
|---|---|
| Quick multi-source sweep | `exa_search` (2+ queries, different angles; 4+ for "extensive"; 8+ across refined batches for "deep") |
| Long autonomous research | delegate to Codex/agent with the paragraph prompt (codex-handoff) or local deep-research harness where available |
| Strategic deliberation on the findings | `council_query` / `punta_de_flecha` — AFTER research, on the evidence |

## Guardrails

| ❌ | ✅ |
|---|---|
| Research prompt assumes context ("our Q3 plan") | Zero-prior-knowledge opener, self-contained |
| "Find out about X" | Bounded question + the decision it feeds |
| Reddit thread cited as proof | Weak-signal tier: lead to verify against primary |
| Contradictions smoothed into one answer | Fact/inference/uncertainty, both sides reported |
| Stops at first plausible answer | Gap round mandatory |
| External research for our own metrics | Source systems own our numbers |

## Verification

A prompt is done when a stranger could execute it without questions. Research is done when: every key claim has a source link, single-source claims are labeled, the gap round ran, and the answer states what evidence would change the conclusion.

## Cross-references

- Deliberation on results: [punta-de-flecha](../punta-de-flecha/SKILL.md), `council_query`
- Analysis house rules (dato/inferencia/decisión): [fable-prompting](../fable-prompting/SKILL.md) modo C
- Delegating the execution: [codex-handoff](../codex-handoff/SKILL.md)

## Cambios

| Fecha | Cambio | Por |
|---|---|---|
| 2026-07-05 | Created — davidondrej research-prompt discipline (zero-context framing, evidence hierarchy, gap round) + the reference deployment Brain-first order and execution routes. | Claude Code (Fable 5) |
