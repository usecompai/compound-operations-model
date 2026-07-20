# Case Study: Building a Company Brain Inside an 8-Figure Consumer Business

## An anonymized, evidence-first account of the reference deployment

**Evidence boundary:** verified 20 July 2026. Operational details are anonymized. Counts are a dated snapshot, not live telemetry.

## Company Profile

| Attribute | Public-safe detail |
|---|---|
| Company | European omnichannel consumer business |
| Scale | 8-figure annual revenue |
| Team | Roughly 40 people |
| Channels | Ecommerce, owned retail, department-store presence and wholesale |
| Starting stack | Commerce, inventory, accounting, lifecycle marketing, customer care, analytics, documents and team communication systems |
| AI operating layer | Shared Brain, 7 domain runtimes, founder command center, authenticated MCP tools and governed skills |
| Time in operation | More than one year of incremental production use |

The company did not begin with a blank technical stack or a dedicated internal engineering department. It began with working business systems, fragmented context and operators spending too much time reconciling the two.

## The Operating Problem

The bottleneck was not access to a capable model. It was the gap between what the company knew, what its systems showed and what people needed to do next.

- Decisions and exceptions lived across conversations, meetings, documents and individual memory.
- Sales, stock, marketing and product-cost information had to be reconciled across separate tools.
- Useful AI work was trapped in individual chats and could not be reused or audited consistently.
- Routine handoffs crossed spreadsheets, messages and source systems without one owner or receipt.
- Different people needed different access to the same operating memory.

## What Was Built

### 1. A shared Company Brain

Approved information from work conversations, generated meeting notes, documents and business systems is normalized into a structured, searchable memory. Durable facts retain source and date. Raw capture is separated from promoted knowledge.

### 2. One authenticated tool layer

The MCP layer gives people and agents a controlled way to read and, where policy allows, prepare or execute work in company systems. Identity, scope and action risk are checked separately from model confidence.

### 3. Specialist runtimes

Seven domain runtimes cover company direction, customer care, finance, retail, digital marketing, merchandising and people operations. They share the Brain but retain separate roles and authority boundaries.

### 4. Governed procedures

Repeatable work is packaged as skills with triggers, inputs, outputs, verification and stop conditions. Availability is not treated as approval: a capability can be installed without being canonical or cleared for consequential execution.

### 5. Receipts and human controls

The operating loop is: observe, decide, prepare or execute within authority, verify and record. Customer-facing, money, legal, people and destructive changes stop at a named human boundary unless a narrower policy explicitly allows them.

## Current Verified Snapshot

| Surface | 20 July 2026 snapshot |
|---|---:|
| Brain documents indexed | 5,235 |
| Embedding vectors | 24,469 |
| Pending embeddings | 112 |
| Skills available to the swarm | 374 |
| Company-governed canonical skills | 48 |
| Canonical skills with a recorded evaluation | 46 |
| Authenticated MCP tools | 98 |
| Production agent runtimes | 7 + founder command center |
| Read-only connector smoke | 14/14 green |
| Independent Google Workspace mail check | Green |
| Recorded action receipts | 46,221 |
| MCP authentication | `enforce` |
| Dated maturity assessment | 6.6/10 |

The public package contains 66 playbook chapters, 31 anonymized skills, 220 implementation-kit files and 21 executable patterns.

## Work The System Supports

The most useful outputs are not generic chat answers. They are operating surfaces and bounded workflows built over shared context.

### Company performance

Sales, stores, paid media, lifecycle marketing and product cost can be reconciled into one operating view with source references behind the numbers.

### Retail and stock

Teams can inspect sales velocity and availability by location, product and size, then prepare transfers or buying decisions for human approval.

### Marketing profitability

Campaign spend can be read alongside sales, returns and product cost so a budget decision is based on contribution rather than platform-reported revenue alone.

### Operations and finance handoff

A fulfilled shipment can trigger preparation of the invoice and collection trail. Duplicate, tax and total checks run before a finance owner posts anything.

### Reusable company tools

Internal dashboards, writing tools and operating utilities can be published through one protected catalog with versions, ownership and rollback evidence.

The public Live demo uses an isolated synthetic company to demonstrate these execution contracts. It does not expose or connect to the reference company's customer data.

## What Changed For Operators

The clearest result is structural rather than a fabricated headline percentage:

- recurring reports no longer have to start from disconnected exports;
- useful context survives the chat or meeting where it first appeared;
- a correction can improve a shared procedure instead of one person's prompt;
- teams can inspect where a result came from and who must approve the next step;
- internal tools have one protected route, owner and version history;
- completed work leaves a receipt that can be reviewed later.

Compai does not claim that the system alone caused company growth or avoided a specific number of hires. Those claims require a counterfactual the current evidence does not provide.

## Reference Economics

The reference deployment models an internal Brain and swarm operating cost of **EUR631/month**, or roughly **EUR21/day**, across a company of roughly 40 people. This covers models, compute and secure infrastructure. It is not a Compai licence price or an implementation quote.

Chapter 12 models a 16.2:1 return under explicit time and cost assumptions. That figure is a planning model, not audited realized value. Every deploying company should replace the assumptions with its own loaded salaries, licences, implementation time and verified hours returned.

## What Is Not Solved Yet

The release boundary includes material limitations:

1. Several agent runtimes and semantic retrieval share one physical node; tested high availability is not in place.
2. One team channel was degraded during the latest audit, although its runtime remained available.
3. Runtime backup coverage is incomplete even though the Brain itself has layered backup protection.
4. The embedding queue was not empty at release time.
5. Broad autonomous execution remains low. The system is strongest at capture, retrieval, analysis, preparation and bounded execution.
6. Fine-grained retrieval scoping is still rolling out domain by domain.
7. Generated meeting notes are useful, but complete native-transcript coverage is not claimed.

These constraints matter because a Company Brain should be judged as operating infrastructure, not as a demo.

## Replication Guidance

A sensible first deployment does not start by copying seven agents. It starts with one visible operating gap.

1. Choose one job with a measurable result and a named owner.
2. Connect only the sources needed for that job.
3. Begin read-only or prepare-for-review.
4. Define the human approval point before writing automation.
5. Verify the outcome and keep a receipt.
6. Repeat until the workflow is reliable, then package it as a skill.
7. Add another domain only when the shared Brain and controls can support it.

The public playbook and starter kit provide the method. The accumulated company context, local permissions and operating judgment must be built inside each deploying business.

**Inspect the evidence:** https://usecompai.com/live.html

**Implementation help:** hello@usecompai.com
