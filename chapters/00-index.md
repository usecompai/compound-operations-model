# Compai Playbook — Source Index

**By Compai** · Open-source educational portfolio · Built inside a profitable brand growing 100%+ annually · Repo: usecompai.com/repo

The playbook is a **journey**: eight sections in the order an SME actually builds an AI operating system. Read them in order the first time. Each section ends with a **Ship it** gate — the minimum working state before the next section makes sense.

The system you are about to build, in one sentence: it captures work as it happens, promotes durable signals, turns them into bounded execution loops, and leaves audit receipts for every consequential action — the operating memory of a company.

**The 30-day path:** week 1 = Start Here + The Brain (capture running) · week 2 = The Tools (hands on 2 systems) · week 3 = The Agents (first agent, propose-only) + Governance (authority matrix, scoped spaces) · week 4 = Operate (the loop live) + Proof (your own honest ledger).


## 1. START HERE — Why an AI operating system, what it looks like, and how far you can take it

1. [Introduction](01-introduction.html)
2. [The Problem](02-problem.html)
3. [Architecture](03-architecture.html)
4. [30-Second Company Brain](00a-30-second-brain.html)
5. [The 5 Pillars](15-five-pillars.html)
6. [Capability Maturity Ladder](00d-maturity-ladder.html)
7. [Live Dashboard Tour](00b-live-dashboard.html)

**Ship it — do not move on until:**
- [ ] You can explain the thesis in one sentence: capture the company, formalize it into a brain, execute on top.
- [ ] You know which rung of the maturity ladder you are on today.
- [ ] You have seen the live dashboard and know what “good” looks like.

## 2. THE BRAIN — Capture the company as it happens, formalize it into memory, make it retrievable

8. [The Company Brain](00-the-brain.html)
9. [The capture layer — Slack, Meet, Email, Drive](10m-capture-layer.html)
10. [The Capture Spine](10u-capture-spine.html)
11. [Ingest Layer](11f-ingest-layer.html)
12. [Memory Architecture](10b-memory-architecture.html)
13. [Brain v2 — from wiki to operational memory](10l-brain-v2-living-memory.html)
14. [The Intelligence Layer](10t-the-intelligence-layer.html)
15. [Domain Intelligence Indexes](10v-domain-intelligence-indexes.html)
16. [Knowledge Mining Loop](10g-knowledge-mining.html)
17. [Structured Data Sidecar](10y-structured-data-sidecar.html)

**Ship it — do not move on until:**
- [ ] A capture spine runs with at least 3 sources, each item stamped (source, timestamp, sensitivity).
- [ ] Capture keeps queueing when the model is down — you have tested it.
- [ ] Domain indexes exist with named owners; promotion-queue depth is on a dashboard.
- [ ] Tables over ~10k rows live in the sidecar with a dataset card, not in markdown.

## 3. THE TOOLS — One protocol between the brain and every real system — hands, not just answers

18. [MCP Server](10c-mcp-server.html)
19. [Technology Stack](10-stack.html)
20. [Consumer SME Stack Map](10k-stack-map.html)
21. [LLM Provider Abstraction](18-llm-providers.html)
22. [Provider Failure Semantics](10z-provider-failure-semantics.html)
23. [Webhooks + Slack Digest](21-webhooks-digest.html)

**Ship it — do not move on until:**
- [ ] An MCP (or equivalent) server connects the brain to at least 2 real systems.
- [ ] Your jobs report four states — ok / blocked-provider / blocked-reauth / failed-validation — never bare pass/fail.
- [ ] You can swap the model provider without losing any context.

## 4. THE AGENTS — Domain agents that execute on top of shared memory, and the factory that ships them

24. [Customer Service](04-agent-cs.html)
25. [Inventory & Supply](05-agent-ops.html)
26. [Finance & Reporting](06-agent-finance.html)
27. [Marketing & Lifecycle](07-agent-marketing.html)
28. [Wholesale & B2B](08-agent-wholesale.html)
29. [Retail & Physical](09-agent-retail.html)
30. [Merchandising](09b-agent-merchandising.html)
31. [HR & People Ops](09c-agent-hr.html)
32. [Agent Factory Pattern](17-agent-factory.html)
33. [Factory Runtime](19-factory-runtime.html)
34. [MVP Runtime](20-mvp-runtime.html)

**Ship it — do not move on until:**
- [ ] Your first agent runs in ONE domain, propose-only, reading its scoped index.
- [ ] It writes decisions back to the brain — the second agent can see what the first learned.
- [ ] You ship the second agent from the factory pattern, not from scratch.

## 5. GOVERNANCE — Bounded execution: scope, security, audit — safe to depend on

35. [Agentic Governance](16-agentic-governance.html)
36. [Hardening the Brain](10s-hardening-the-brain.html)
37. [Brain Spaces](10x-brain-spaces.html)
38. [Public-by-default — agents in the open](10q-public-by-default.html)
39. [Governed Internal Publishing](11h-internal-publishing.html)
40. [Organ Health Control Plane](11i-organ-health.html)
41. [EU AI Act Compliance](11d-eu-ai-act-compliance.html)

**Ship it — do not move on until:**
- [ ] An authority matrix (read / propose / execute) exists for every agent.
- [ ] Finance, HR and legal live in scoped spaces BEFORE any external exposure.
- [ ] Published artifacts live on a protected company route with versions and receipts.
- [ ] Degraded organs open tasks in a queue someone drains — not dashboard tiles.

## 6. OPERATE — The loops that turn captured context into work — and make the system improve weekly

42. [The Context-to-Work Loop](10w-context-to-work.html)
43. [Operational compounding loop](10r-operational-compounding-loop.html)
44. [Tasks, outputs, decisions, health](10p-tasks-outputs-health.html)
45. [Master Prompt as source of truth](10o-master-prompt.html)
46. [Council vs Punta de Flecha](10h-council-vs-flecha.html)
47. [Master Calendar](10j-master-calendar.html)
48. [Profit Throttle](10e-profit-throttle.html)
49. [Invoice Pipeline](10i-invoice-pipeline.html)
50. [AI-Native Team Onboarding](14-team-onboarding.html)
51. [Onboarding Experience](22-onboarding-experience.html)

**Ship it — do not move on until:**
- [ ] The context-to-work loop runs: signals become candidates, work objects, receipts.
- [ ] The human digest is capped (≤10 items) and actually gets drained daily.
- [ ] Every correction becomes a rule — the system is measurably sharper than last month.

## 7. BUILD IT — The executable path: setup, bootstrap, templates, downloadable artifacts

52. [Implementation Paths](11-implementation.html)
53. [Setup 1-click](10n-setup-1-click.html)
54. [Brand Bootstrap](11e-brand-bootstrap.html)
55. [OpenClaw Setup Guide](11c-openclaw-setup.html)
56. [Downloadable Artifacts](00c-artifacts-index.html)
57. [Pattern Library](10f-pattern-library.html)

**Ship it — do not move on until:**
- [ ] You ran the setup on your own infrastructure and adapted the templates — not copied them blind.
- [ ] Your brain has its first 50 real documents and one working loop end to end.

## 8. PROOF — Honest ROI, production lessons, and the failure ledger

58. [ROI Analysis](12-roi.html)
59. [Production Lessons](11b-production-lessons.html)
60. [Failure Ledger](11g-failure-ledger.html)
61. [Advanced Capabilities](10d-advanced-capabilities.html)

**Ship it — do not move on until:**
- [ ] You keep your own two-layer ROI ledger with every cost counted — including all the seats.
- [ ] You keep a failure ledger. If it is empty, you are not measuring.

---

**Version 4.0** · July 2026 — The playbook is reorganized as the eight-section SME journey and adds the operating-memory layer from our latest production work: the capture spine, domain intelligence indexes, the context-to-work loop, brain spaces, the structured data sidecar, provider failure semantics, governed internal publishing, and the organ health control plane. 62 chapters. The public repo includes the full playbook plus starter kit artifacts, templates and evals.
