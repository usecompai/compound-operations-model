# Chapter 10aa: Truth & Evidence — A Brain That Can Disagree With Itself

## The dangerous version of a smart system

The hardest failure in a company brain is not an empty answer. It is a polished answer built from stale truth.

We learned that the brain can be technically healthy and still lie about its own operating state. A security document said one thing while the live service did another. An old cash figure still said "today." A model-routing note had been superseded, but search kept ranking the older chunk first. Nothing was down. The answers were simply wrong with confidence.

That changed how we define a company brain. It is not enough to store knowledge and retrieve it quickly. The system must know **which evidence wins, how fresh it is, and whether it describes a deployed capability or a target design**.

## The truth stack

Use this order when two sources disagree:

1. **Live source system.** The commerce platform wins on orders. The accounting system wins on booked invoices. The runtime health endpoint wins on auth mode and agent status.
2. **Dated canonical record.** A reviewed contract, policy or decision with owner, source and stale date.
3. **Operational artifact.** A task output, receipt, reconciliation or report tied to its inputs.
4. **Human testimony.** Meetings, email and chat preserve intent and context. Their numbers must still be checked against the source system.
5. **Memory and inference.** Useful for forming the next question, never for upgrading a claim into fact.

The rule is simple: **testimony can tell you what someone meant; it cannot settle a number that a source system can answer.**

## Three labels that prevent overclaiming

Every material capability should carry one of these states:

| State | Meaning | Public language |
|---|---|---|
| **Deployed** | Running now, with current evidence | "Running in production" |
| **Pilot** | Bounded test with a human gate | "In controlled pilot" |
| **Pattern** | Shipped design/template, not universal runtime state | "Available in the playbook and kit" |

This matters most for permissions and autonomy. A Brain Spaces template can be production-quality while fine-grained retrieval scoping is still being rolled out. A context-to-work contract can be shipped while broad autonomous closure remains in pilot. The pattern is real. The deployment state must be stated separately.

## A dated reference snapshot

The reference deployment snapshot used for Compai v5.0 was verified on **12 July 2026**:

- 4,842 documents indexed for retrieval;
- 373 skills available across canonical, installed and vendor/community layers;
- 47 company-authored canonical skills;
- 97 MCP tools;
- seven production agent runtimes;
- authentication in `enforce` mode;
- 15 source connectors passing read-only smoke tests;
- more than 42,000 action-ledger rows;
- strong capture and retrieval, with autonomous closure still in a controlled pilot.

These are dated facts, not permanent copy. A future release must regenerate the snapshot from the live system or keep the old date visible.

## Coverage is a map, not a slogan

"Everything the company knows" is a direction, not a measurable claim. The useful artifact is a coverage map:

| Source class | What good coverage proves | What it does not prove |
|---|---|---|
| Chat | Readable channels are captured and promoted | Private conversations are covered |
| Email | Agreed mailboxes and windows are ingested | Every historical mailbox is complete |
| Meetings | Notes/recordings reach the brain | Every meeting has a verbatim transcript |
| Drive/Notion | Canonical documents are inventoried | Every file is useful or current |
| Source systems | Live reads pass validation | Every write is authorized |

The reference deployment has broad company coverage, but it still publishes its gaps: private meeting-note visibility and native transcript completeness are not universal. That honesty is not a weakness. It tells the operator where the next missing decision may be hiding.

## The evidence card

Every public number or material internal claim should be reproducible from an evidence card:

```yaml
claim: "97 MCP tools available"
state: deployed
source_class: runtime_manifest
verified_at: 2026-07-12T09:30:00Z
owner: platform
fresh_for: 7d
public_safe: true
```

If the card is stale, the interface can keep the last verified number, but it must keep the date too. If the source fails, the state becomes `blocked_source_unavailable`; it does not silently reuse an old number as "live."

## Porting checklist

- [ ] Define which source system wins for each operational fact.
- [ ] Put current state first and historical state underneath it.
- [ ] Give every volatile claim a verification date and freshness window.
- [ ] Label capabilities as deployed, pilot or pattern.
- [ ] Treat meeting/email/chat numbers as testimony until verified.
- [ ] Maintain a source-coverage map with explicit gaps.
- [ ] Re-index after correcting a canonical truth and verify the old answer no longer wins.
- [ ] Generate public facts from an approved manifest instead of hand-editing several pages.

## For Compai readers

A trustworthy brain does not pretend uncertainty disappeared. It makes uncertainty inspectable. The competitive advantage is not "we captured everything." It is **we know what we captured, what we missed, which source wins and when the claim was last true.**

