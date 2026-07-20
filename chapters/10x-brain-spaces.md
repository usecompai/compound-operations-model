# Chapter 10x: Brain Spaces — Scoped Memory for Agents and People

> **Implementation status, 20 July 2026:** Brain Spaces is the deployed architecture contract and the target policy for every external surface. Per-identity authentication is enforced today. Fine-grained, retrieval-level scoping for every sensitive tree is staged and rolling out domain by domain; it is not yet universal. The design below is therefore both the contract we operate toward and the acceptance test for completing that rollout.

## The near-miss that convinced us

Picture a demo. We are showing the system to a room of people who do not work here — a prospective partner, maybe, or a room of founders who wanted to see how the agents actually run. Someone types a normal-sounding question: "What does it cost us to keep the retail team staffed?" The agent does exactly what a good agent does. It searches everything it can reach, finds the most relevant document, and answers with a precise, correct, per-person compensation figure — pulled from the HR tree, read aloud in a room that should never have seen it.

Nothing about that agent malfunctioned. It searched the brain it was given and returned the best-grounded answer available. The failure was upstream of the model: we had given it the whole brain. In a company of five, one open brain is not recklessness — it is the fastest way to bootstrap, and it was the right call for us at the start. But the day the agents stopped only reading and started being able to *execute*, "everything is readable by everyone and everything" became the single largest finding on our own audit. This chapter is the fix: **agents should not receive the whole company brain by default.**

## A space is a slice with a membership list

A Brain Space is a slice of the brain that carries its own membership. Concretely, a space is two lists bolted onto a set of documents:

1. **The trees and indexes it contains** — an allowlist of directory subtrees and the domain indexes (see 10v) that point into them. A space is not a copy; it is a view. The same document can belong to more than one space, and no document belongs to a space unless a space explicitly names it.
2. **Who and what can read it, and separately, who and what can write or propose into it.** Membership is by *role* (finance owner, retail lead, any employee) and by *agent* (the retail agent, the finance agent, the command center). Read and write are distinct grants. Plenty of members read a space they may never write; a few may propose into a space they cannot read back in full.

Two rules make the model safe rather than decorative:

- **Deny by default.** If a space does not name a tree, the tree is invisible to that space's members. If a space does not name you, you are not in it. There is no implicit inheritance, no "readable because you can reach the parent folder."
- **Search respects the space.** This is the load-bearing part. Scoping is not a UI filter applied after the fact — it is applied *before* retrieval, so a document outside your spaces cannot surface as a search hit, a citation, or a snippet, no matter how the query is phrased. An agent cannot leak what it was never allowed to retrieve.

That last point is why spaces beat access-control-as-afterthought. Blast radius is bounded at the retrieval layer: a prompt-injected, jailbroken, or simply overeager agent can only expose what its spaces contain.

## The default seven

The reference contract defines seven spaces. They are a starting set, not scripture — but they map cleanly onto how a growing company partitions trust.

| Space | What lives there | Who / what reads |
|---|---|---|
| **company-public** | Handbook, values, product basics, shared playbooks, glossary, non-sensitive process docs | Every employee + every agent |
| **department** (marketing, retail, ops, product…) | Domain playbooks, campaign notes, run docs, team-local decisions | That department's people + that department's agent; leads across departments by grant |
| **exec** | Strategy memos, board-adjacent material, org planning, sensitive decisions in flight | Named execs + the command center agent |
| **finance-sensitive** | Cash position, margins, vendor terms, forecasts, anything that moves money | Finance owner(s) + the finance agent only |
| **legal-sensitive** | Contracts, disputes, counsel notes, compliance matters | Named legal role(s); no general-purpose agent by default |
| **HR-sensitive** | Compensation, reviews, personal records, headcount planning | HR role(s) only; agents excluded unless explicitly granted |
| **demo / client-safe** | A curated, honest slice safe to show an outsider — how the system works, none of the company's private data | Contractors, agencies, demo viewers; the demo agent |

The demo space earns its keep beyond demos. It is the same allowlist you hand a contractor, an agency, or an evaluation harness. When someone outside asks "can we see it," you point them at the space built to be seen — not at a redaction you did by hand and hoped was complete.

## Scoped search: same question, different answers by design

The same query is *supposed* to return different results depending on who asks. Consider "What is our margin on the autumn range?"

- The **marketing agent**, scoped to company-public + marketing, gets the public product notes and the campaign brief. No margin figure surfaces, because the margin document lives in finance-sensitive and finance-sensitive is not in its spaces. The agent does not see a redacted answer — it sees no such document exists to retrieve.
- The **finance owner**, a member of finance-sensitive, gets the full margin breakdown, the vendor cost basis, and the forecast.

Neither result is a bug. Divergence is the feature. A single canonical brain, queried honestly, tells different truths to different callers because the caller's spaces define what "the brain" even is from where they stand. This is also what makes the honesty loop work: people write candidly into HR and finance spaces precisely *because* they know the marketing agent and their colleague in another department cannot read them back out. Remove the scoping and you do not just add risk — you quietly degrade what gets written down at all.

## Crossing spaces on purpose

Isolation would be useless if signal never moved. It moves — deliberately, never implicitly.

A **promotion** is an explicit, reviewed copy of a signal from a tighter space into a broader one. The finance-sensitive space produces a quarterly decision that the whole company should know about; the finance owner writes a company-public summary that states the decision and its rationale *without* the underlying numbers, and publishes that into company-public. The sensitive source stays put. The public artifact is a new document, authored on purpose, reviewed by the role that owns the boundary.

The mechanics we enforce: promotion has a named **target space** and a named **reviewer role**, and it is a write event, not a link. You never "expose" a document across a boundary by referencing it — a reference would drag the sensitive original into a broader search scope. You author a fresh, scoped-appropriate artifact and place it. Leaks are what happen when signal crosses a boundary without a human deciding it should; promotion is the sanctioned opposite, and it should be the *only* way anything moves up the sensitivity ladder.

## When to adopt

Be honest about sequencing, because premature partitioning is its own failure mode — it slows a small team down and buys safety it does not yet need.

- **One open brain is fine while the brain only informs and the readers are all trusted insiders.** At five people, every reader is in the room already. Scoping five people into seven spaces is overhead with no payoff.
- **Spaces become mandatory the moment either of two things is true:** (1) agents can *execute*, not just read — because an executing agent that can read everything can act on everything, and blast radius stops being hypothetical; or (2) *anyone outside the trust boundary* touches the system — a contractor, an agency, a demo viewer, an external MCP caller, a mobile connector. The first outside caller is the deadline.

For us, scoping finance, HR, and legal is not a nice-to-have — it is the *precondition* for broad external retrieval (see 10s). Authentication moved to enforce first to close anonymous access; granular Spaces enforcement is the remaining control-plane rollout. Salary data readable by every employee is a culture decision you can defend; salary data readable by every caller is an incident you are choosing to schedule.

## Porting checklist

- [ ] List every tree in your brain and tag each with a sensitivity: public, department, sensitive (finance/HR/legal), or exec.
- [ ] Define your spaces (start with the default seven; merge or split to fit your org).
- [ ] For each space, write the explicit allowlist of trees and indexes it contains — nothing implicit.
- [ ] For each space, list **read** members and, separately, **write/propose** members, by role and by agent.
- [ ] Set `deny_by_default: true` and confirm no tree is reachable except through a space that names it.
- [ ] Verify scoping is enforced at **retrieval**, not as a post-filter — run the same query as two different members and confirm the sensitive hit never appears for the wrong one.
- [ ] Build the demo / client-safe space before your first external demo, contractor, or agency touch.
- [ ] Define promotion paths: which space can promote into which, and which role reviews each crossing.
- [ ] Map every agent to its minimum viable spaces — the fewest that let it do its job.
- [ ] Re-run the "demo question" test: ask an outside-facing agent something sensitive and confirm it retrieves nothing it shouldn't.

## For Compai readers

If you take one thing from this chapter, take the sequencing: an open brain is the right way to start and the wrong way to scale, and the trigger to scope is not a feeling — it is the day an agent can execute or the day an outsider connects, whichever comes first.

**Scope the sensitive domains before you expose anything — because a leak is signal crossing a boundary nobody chose to open, and a space is how you make every crossing a decision instead of an accident.**
