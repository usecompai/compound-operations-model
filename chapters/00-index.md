# Compai Playbook — Source Index

**By Compai** · Open, source-available educational portfolio · Built inside an 8-figure consumer company · Repo: usecompai.com/repo

The playbook is a **journey**: eight sections in the order an SME actually builds an AI operating system. Read them in order the first time. Each section ends with a **Ship it** gate — the minimum working state before the next section makes sense.

The system you are about to build, in one sentence: it captures work as it happens, promotes durable signals, turns them into bounded execution loops, and leaves audit receipts for every consequential action — the operating memory of a company.

**The 30-day path:** week 1 = Start Here + The Brain (capture running) · week 2 = The Tools (hands on 2 systems) · week 3 = The Agents (first agent, propose-only) + Governance (authority matrix, truth manifest, scoped spaces) · week 4 = Operate (one bounded closure-first pilot) + Proof (your own honest ledger).


## 1. START HERE — Why an AI operating system, what it looks like, and how far you can take it

1. [Introduction](01-introduction.md)
2. [The Problem](02-problem.md)
3. [Architecture](03-architecture.md)
4. [30-Second Company Brain](00a-30-second-brain.md)
5. [The 5 Pillars](15-five-pillars.md)
6. [Capability Maturity Ladder](00d-maturity-ladder.md)
7. [Live Dashboard Tour](00b-live-dashboard.md)
8. [The Company Operating Layer](23-operating-layer.md)

**Ship it — do not move on until:**
- [ ] You can explain the thesis in one sentence: capture the company, formalize it into a brain, execute on top.
- [ ] You know which rung of the maturity ladder you are on today.
- [ ] You have seen the live dashboard and know what “good” looks like.

## 2. THE BRAIN — Capture the company as it happens, formalize it into memory, make it retrievable

9. [The Company Brain](00-the-brain.md)
10. [Compile Context Before Work](24-context-compiler.md)
11. [The capture layer — Slack, Meet, Email, Drive](10m-capture-layer.md)
12. [The Capture Spine](10u-capture-spine.md)
13. [Ingest Layer](11f-ingest-layer.md)
14. [Memory Architecture](10b-memory-architecture.md)
15. [Brain v2 — from wiki to operational memory](10l-brain-v2-living-memory.md)
16. [The Intelligence Layer](10t-the-intelligence-layer.md)
17. [Truth and Evidence](10aa-truth-and-evidence.md)
18. [Domain Intelligence Indexes](10v-domain-intelligence-indexes.md)
19. [Knowledge Mining Loop](10g-knowledge-mining.md)
20. [Structured Data Sidecar](10y-structured-data-sidecar.md)

**Ship it — do not move on until:**
- [ ] A capture spine runs with at least 3 sources, each item stamped (source, timestamp, sensitivity).
- [ ] Capture keeps queueing when the model is down — you have tested it.
- [ ] Domain indexes exist with named owners; promotion-queue depth is on a dashboard.
- [ ] Tables over ~10k rows live in the sidecar with a dataset card, not in markdown.
- [ ] Every public claim carries a date, status and evidence class; known gaps remain visible.

## 3. THE TOOLS — One protocol between the brain and every real system — hands, not just answers

21. [MCP Server](10c-mcp-server.md)
22. [Technology Stack](10-stack.md)
23. [Consumer SME Stack Map](10k-stack-map.md)
24. [LLM Provider Abstraction](18-llm-providers.md)
25. [Provider Failure Semantics](10z-provider-failure-semantics.md)
26. [Webhooks + Slack Digest](21-webhooks-digest.md)
27. [From Skills To Verified Capabilities](25-capability-registry.md)

**Ship it — do not move on until:**
- [ ] An MCP (or equivalent) server connects the brain to at least 2 real systems.
- [ ] Your jobs report four states — ok / blocked-provider / blocked-reauth / failed-validation — never bare pass/fail.
- [ ] You can swap the model provider without losing any context.

## 4. THE AGENTS — Domain agents that execute on top of shared memory, and the factory that ships them

28. [Customer Service](04-agent-cs.md)
29. [Inventory & Supply](05-agent-ops.md)
30. [Finance & Reporting](06-agent-finance.md)
31. [Marketing & Lifecycle](07-agent-marketing.md)
32. [Wholesale & B2B](08-agent-wholesale.md)
33. [Retail & Physical](09-agent-retail.md)
34. [Merchandising](09b-agent-merchandising.md)
35. [HR & People Ops](09c-agent-hr.md)
36. [Agent Factory Pattern](17-agent-factory.md)
37. [Factory Runtime](19-factory-runtime.md)
38. [MVP Runtime](20-mvp-runtime.md)

**Ship it — do not move on until:**
- [ ] Your first agent runs in ONE domain, propose-only, reading its scoped index.
- [ ] It writes decisions back to the brain — the second agent can see what the first learned.
- [ ] You ship the second agent from the factory pattern, not from scratch.

## 5. GOVERNANCE — Bounded execution: scope, security, audit — safe to depend on

39. [Agentic Governance](16-agentic-governance.md)
40. [Hardening the Brain](10s-hardening-the-brain.md)
41. [Brain Spaces](10x-brain-spaces.md)
42. [Architecture Contract](10ab-architecture-contract.md)
43. [Skill Governance](10ac-skill-governance.md)
44. [Public-by-default — agents in the open](10q-public-by-default.md)
45. [Governed Internal Publishing](11h-internal-publishing.md)
46. [Organ Health Control Plane](11i-organ-health.md)
47. [EU AI Act Compliance](11d-eu-ai-act-compliance.md)
48. [Humans And Autonomous Runtimes](26-human-work-mode.md)
49. [Workspaces, Publishing And Rollback](27-workspaces-publishing.md)

**Ship it — do not move on until:**
- [ ] An authority matrix (read / propose / execute) exists for every agent.
- [ ] Finance, HR and legal live in scoped spaces BEFORE any external exposure.
- [ ] Runtime identity, workspace ownership and artifact storage match the architecture contract.
- [ ] Every canonical skill has a builder, an independent judge, evidence and a promotion state.
- [ ] Published artifacts live on a protected company route with versions and receipts.
- [ ] Degraded organs open tasks in a queue someone drains — not dashboard tiles.

## 6. OPERATE — The loops that turn captured context into work — and make the system improve weekly

50. [The Context-to-Work Loop](10w-context-to-work.md)
51. [Closure-First Execution](10ad-closure-first-execution.md)
52. [Operational compounding loop](10r-operational-compounding-loop.md)
53. [Tasks, outputs, decisions, health](10p-tasks-outputs-health.md)
54. [Master Prompt as source of truth](10o-master-prompt.md)
55. [Council vs Punta de Flecha](10h-council-vs-flecha.md)
56. [Master Calendar](10j-master-calendar.md)
57. [Profit Throttle](10e-profit-throttle.md)
58. [Invoice Pipeline](10i-invoice-pipeline.md)
59. [AI-Native Team Onboarding](14-team-onboarding.md)
60. [Onboarding Experience](22-onboarding-experience.md)
61. [Decision Packs And Outcome Receipts](28-decision-packs-outcome-receipts.md)

**Ship it — do not move on until:**
- [ ] The context-to-work loop runs: signals become candidates, work objects, receipts.
- [ ] One approved task has completed ten reviewed runs at ≥80% verified closure before adding generators.
- [ ] The human digest is capped (≤10 items) and actually gets drained daily.
- [ ] Every correction becomes a rule — the system is measurably sharper than last month.

## 7. BUILD IT — The executable path: setup, bootstrap, templates, downloadable artifacts

62. [Implementation Paths](11-implementation.md)
63. [Setup 1-click](10n-setup-1-click.md)
64. [Brand Bootstrap](11e-brand-bootstrap.md)
65. [OpenClaw Setup Guide](11c-openclaw-setup.md)
66. [Downloadable Artifacts](00c-artifacts-index.md)
67. [Pattern Library](10f-pattern-library.md)

**Ship it — do not move on until:**
- [ ] You ran the setup on your own infrastructure and adapted the templates — not copied them blind.
- [ ] Your brain has its first 50 real documents and one working loop end to end.

## 8. PROOF — Honest ROI, production lessons, and the failure ledger

68. [ROI Analysis](12-roi.md)
69. [Production Lessons](11b-production-lessons.md)
70. [Failure Ledger](11g-failure-ledger.md)
71. [Advanced Capabilities](10d-advanced-capabilities.md)

**Ship it — do not move on until:**
- [ ] You keep your own two-layer ROI ledger with every cost counted — including all the seats.
- [ ] You keep a failure ledger. If it is empty, you are not measuring.

---

**Version 6.2 — Codex-First Bootstrap** · 15 September 2026 — This release adds a practical, phase-gated route for building the Company Brain with Codex while keeping memory, permissions and state model-independent. The dated evidence boundary reports 45 of 55 core capabilities ready, seven production domain agents online, authenticated MCP and lexical Brain retrieval ready. Company-source ingestion and the Context Compiler were degraded, so those states remain visible. A full offsite restore passed in isolation on 9 September with one inherited ledger warning. 72 chapters including this source index.
