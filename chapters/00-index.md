# Compai Playbook — Source Index

**By Compai** · Open-source educational portfolio · Built inside a profitable brand growing 100%+ annually · Repo: usecompai.com/repo

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

**Ship it — do not move on until:**
- [ ] You can explain the thesis in one sentence: capture the company, formalize it into a brain, execute on top.
- [ ] You know which rung of the maturity ladder you are on today.
- [ ] You have seen the live dashboard and know what “good” looks like.

## 2. THE BRAIN — Capture the company as it happens, formalize it into memory, make it retrievable

8. [The Company Brain](00-the-brain.md)
9. [The capture layer — Slack, Meet, Email, Drive](10m-capture-layer.md)
10. [The Capture Spine](10u-capture-spine.md)
11. [Ingest Layer](11f-ingest-layer.md)
12. [Memory Architecture](10b-memory-architecture.md)
13. [Brain v2 — from wiki to operational memory](10l-brain-v2-living-memory.md)
14. [The Intelligence Layer](10t-the-intelligence-layer.md)
15. [Truth and Evidence](10aa-truth-and-evidence.md)
16. [Domain Intelligence Indexes](10v-domain-intelligence-indexes.md)
17. [Knowledge Mining Loop](10g-knowledge-mining.md)
18. [Structured Data Sidecar](10y-structured-data-sidecar.md)

**Ship it — do not move on until:**
- [ ] A capture spine runs with at least 3 sources, each item stamped (source, timestamp, sensitivity).
- [ ] Capture keeps queueing when the model is down — you have tested it.
- [ ] Domain indexes exist with named owners; promotion-queue depth is on a dashboard.
- [ ] Tables over ~10k rows live in the sidecar with a dataset card, not in markdown.
- [ ] Every public claim carries a date, status and evidence class; known gaps remain visible.

## 3. THE TOOLS — One protocol between the brain and every real system — hands, not just answers

19. [MCP Server](10c-mcp-server.md)
20. [Technology Stack](10-stack.md)
21. [Consumer SME Stack Map](10k-stack-map.md)
22. [LLM Provider Abstraction](18-llm-providers.md)
23. [Provider Failure Semantics](10z-provider-failure-semantics.md)
24. [Webhooks + Slack Digest](21-webhooks-digest.md)

**Ship it — do not move on until:**
- [ ] An MCP (or equivalent) server connects the brain to at least 2 real systems.
- [ ] Your jobs report four states — ok / blocked-provider / blocked-reauth / failed-validation — never bare pass/fail.
- [ ] You can swap the model provider without losing any context.

## 4. THE AGENTS — Domain agents that execute on top of shared memory, and the factory that ships them

25. [Customer Service](04-agent-cs.md)
26. [Inventory & Supply](05-agent-ops.md)
27. [Finance & Reporting](06-agent-finance.md)
28. [Marketing & Lifecycle](07-agent-marketing.md)
29. [Wholesale & B2B](08-agent-wholesale.md)
30. [Retail & Physical](09-agent-retail.md)
31. [Merchandising](09b-agent-merchandising.md)
32. [HR & People Ops](09c-agent-hr.md)
33. [Agent Factory Pattern](17-agent-factory.md)
34. [Factory Runtime](19-factory-runtime.md)
35. [MVP Runtime](20-mvp-runtime.md)

**Ship it — do not move on until:**
- [ ] Your first agent runs in ONE domain, propose-only, reading its scoped index.
- [ ] It writes decisions back to the brain — the second agent can see what the first learned.
- [ ] You ship the second agent from the factory pattern, not from scratch.

## 5. GOVERNANCE — Bounded execution: scope, security, audit — safe to depend on

36. [Agentic Governance](16-agentic-governance.md)
37. [Hardening the Brain](10s-hardening-the-brain.md)
38. [Brain Spaces](10x-brain-spaces.md)
39. [Architecture Contract](10ab-architecture-contract.md)
40. [Skill Governance](10ac-skill-governance.md)
41. [Public-by-default — agents in the open](10q-public-by-default.md)
42. [Governed Internal Publishing](11h-internal-publishing.md)
43. [Organ Health Control Plane](11i-organ-health.md)
44. [EU AI Act Compliance](11d-eu-ai-act-compliance.md)

**Ship it — do not move on until:**
- [ ] An authority matrix (read / propose / execute) exists for every agent.
- [ ] Finance, HR and legal live in scoped spaces BEFORE any external exposure.
- [ ] Runtime identity, workspace ownership and artifact storage match the architecture contract.
- [ ] Every canonical skill has a builder, an independent judge, evidence and a promotion state.
- [ ] Published artifacts live on a protected company route with versions and receipts.
- [ ] Degraded organs open tasks in a queue someone drains — not dashboard tiles.

## 6. OPERATE — The loops that turn captured context into work — and make the system improve weekly

45. [The Context-to-Work Loop](10w-context-to-work.md)
46. [Closure-First Execution](10ad-closure-first-execution.md)
47. [Operational compounding loop](10r-operational-compounding-loop.md)
48. [Tasks, outputs, decisions, health](10p-tasks-outputs-health.md)
49. [Master Prompt as source of truth](10o-master-prompt.md)
50. [Council vs Punta de Flecha](10h-council-vs-flecha.md)
51. [Master Calendar](10j-master-calendar.md)
52. [Profit Throttle](10e-profit-throttle.md)
53. [Invoice Pipeline](10i-invoice-pipeline.md)
54. [AI-Native Team Onboarding](14-team-onboarding.md)
55. [Onboarding Experience](22-onboarding-experience.md)

**Ship it — do not move on until:**
- [ ] The context-to-work loop runs: signals become candidates, work objects, receipts.
- [ ] One approved task has completed ten reviewed runs at ≥80% verified closure before adding generators.
- [ ] The human digest is capped (≤10 items) and actually gets drained daily.
- [ ] Every correction becomes a rule — the system is measurably sharper than last month.

## 7. BUILD IT — The executable path: setup, bootstrap, templates, downloadable artifacts

56. [Implementation Paths](11-implementation.md)
57. [Setup 1-click](10n-setup-1-click.md)
58. [Brand Bootstrap](11e-brand-bootstrap.md)
59. [OpenClaw Setup Guide](11c-openclaw-setup.md)
60. [Downloadable Artifacts](00c-artifacts-index.md)
61. [Pattern Library](10f-pattern-library.md)

**Ship it — do not move on until:**
- [ ] You ran the setup on your own infrastructure and adapted the templates — not copied them blind.
- [ ] Your brain has its first 50 real documents and one working loop end to end.

## 8. PROOF — Honest ROI, production lessons, and the failure ledger

62. [ROI Analysis](12-roi.md)
63. [Production Lessons](11b-production-lessons.md)
64. [Failure Ledger](11g-failure-ledger.md)
65. [Advanced Capabilities](10d-advanced-capabilities.md)

**Ship it — do not move on until:**
- [ ] You keep your own two-layer ROI ledger with every cost counted — including all the seats.
- [ ] You keep a failure ledger. If it is empty, you are not measuring.

---

**Version 5.0 — Truth & Execution** · 12 July 2026 — This release adds the evidence contract, architecture invariants, skill governance and a closure-first execution gate. It also publishes the current reference snapshot without converting pilots into production claims: 4,842 Brain documents, 373 available skills, 47 canonical skills, 97 MCP tools, seven production agent runtimes, authentication in enforce, 15 connector smoke tests green and a 42,000+ receipt action ledger. 66 chapters including this source index. The public repo includes the full playbook plus starter kit artifacts, templates and evals.
