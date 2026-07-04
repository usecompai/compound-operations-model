# Chapter 10u: The Capture Spine — Recording the Company as It Happens

## The wall: a brain that rots the day you build it

Here is a scene we lived through. Someone on the team decides the company needs a "second brain." They spend a weekend exporting everything: a dump of the shared drive, a scrape of the wiki, an export of the last year of a few key Slack channels. It lands in one place. It is searchable. For about a week, it feels like magic — you ask a question, you get a real answer grounded in real company documents.

Then it rots. Not slowly. Immediately.

The export was a photograph of one moment. The company kept moving. A pricing decision made in a Slack thread on Tuesday never enters the brain. A supplier change agreed in a meeting on Thursday lives only in one person's memory. The margin correction from Friday's finance review exists as a message that scrolls away. Three months later the brain is confidently wrong about half of what it tells you, because it is answering from a frozen snapshot of a company that no longer exists.

And so the human becomes the courier. Every time an agent or a teammate needs current context, a person has to go fetch it, paste it in, explain what changed. The "brain" is not recording the company. A person is manually feeding it, and that person is the actual system. The moment they stop, the brain dies.

The fix is not a better import. It is a different shape entirely. We call it the **capture spine**: the company records itself as it operates, continuously, so the brain never falls behind. This chapter is how we built ours.

## The spine, piece by piece

A spine has four parts. Get the parts right and everything downstream — the intelligence layer, the domain indexes, the agents — has something true to stand on.

**Sources.** These are the places where the company actually thinks out loud: chat (Slack-style), email, meeting transcripts, documents (Drive/Notion-style), and the source systems that run the business — the commerce platform, the accounting system, the helpdesk, the POS/inventory system, the expense platform. Each is a tap. The spine's job is to keep every tap flowing into one place without a human turning the handle.

**The raw layer.** This is the first landing zone. It is deliberately dumb: append-only, messy, unopinionated. A Slack thread lands as a Slack thread. A meeting transcript lands as a transcript. We do not clean, summarize, or interpret at this stage — we just catch. Append-only matters: nothing here is ever edited or overwritten, so the raw layer doubles as an audit trail. If we ever need to ask "what did we actually know on March 3rd," the answer is here, untouched.

**The promotion boundary.** This is the line between raw and curated. Curated memory is what agents read by default: promoted, deduplicated, indexed, written in clean prose. Raw is the firehose; curated is the library. Promotion is a deliberate act — a model job (or occasionally a human) reads raw items, extracts what matters, deduplicates against what is already known, and writes a curated note into the right index. Agents almost never touch raw. Raw exists to be the audit trail and the re-processing source. When we improve our extraction, we re-run it against raw, not against a fading human memory.

**The three stamps.** Every item, from the moment of capture — never retroactively — carries three pieces of metadata:

- **Source identity.** Where did this come from? Which channel, which mailbox, which meeting, which system? Without this, curated claims are unfalsifiable. With it, every downstream statement can be traced back to its origin.
- **Timestamp.** When did this happen? The company's history only makes sense in order. A decision reverses a prior decision; you need to know which came first.
- **Sensitivity class.** How protected is this? We stamp one of four: `public`, `internal`, `confidential`, `restricted`. This is what lets an agent answer a marketing question from `internal` notes while never surfacing a `restricted` salary discussion. Classify at capture, because classifying a year of history later is a project nobody finishes.

## Capture must outlive interpretation

Here is the insight that took us a real scare to learn: **capture and interpretation are two different stages, and they must be able to fail independently.**

Capture is catching the raw item. Interpretation is the model job that reads it and promotes it. They feel like one pipeline. They are not. If you build them as one pipeline — capture only happens when the model successfully processes the item — then the day the model can't run, the company stops being recorded.

We learned this the hard way. Mid-week, our extraction model got blocked. The specifics do not matter much — a provider-side issue collided with a quota limit and a stale credential, and for the better part of two days the model job that promotes raw into curated simply could not run. Nothing was being interpreted. No new curated notes. No fresh index entries.

In the old shape, this would have been a disaster: two days of company history — decisions, corrections, a supplier renegotiation, a returns-policy change — gone, because the thing that records them was down. But capture was decoupled. The raw layer kept catching everything. Slack threads, emails, meeting transcripts, system events — all of it kept landing in the append-only raw store, each item stamped with its source, time, and sensitivity, waiting. The interpretation queue simply backed up.

When the provider recovered, the queue drained. The model job worked through two days of backlog and promoted it into curated memory as if nothing had happened. We lost zero company history. We lost only the freshness of the curated layer for two days — a nuisance, not a catastrophe.

The lesson is blunt: **the interpretation stage will go down — providers have outages, quotas get hit, credentials expire — and when it does, your capture must keep queuing, not stop.** Build capture so it never depends on the model being up. That single decision is the difference between losing a week of company history and losing nothing.

## What we capture at the company

This is the shape of our deployment's spine. Generic labels, real cadences.

| Source | What it yields | Cadence |
|---|---|---|
| Chat threads (Slack-style) | Decisions, corrections, the "why" behind actions | Continuous |
| Meeting transcripts | Full transcript → decisions and action items | Same-day |
| Email | Threads and attachments, external context | Continuous |
| Documents (Drive/Notion-style) | Specs, policies, plans, living reference docs | On change |
| Commerce system | Orders, returns, catalog events | Scheduled |
| Accounting system | Invoices, cash movements, ledger events | Scheduled |
| Helpdesk | Tickets, customer signals, recurring complaints | Scheduled |
| POS/inventory system | Stock levels, transfers, sell-through | Scheduled |

The pattern: human-conversation sources (chat, email, meetings) are continuous or same-day because that is where decisions are born and where they are easiest to lose. Documents fire on change. Structured source systems run on a schedule because their state is queryable — we can always ask them again, so we pull deltas at a fixed cadence rather than streaming every row.

## Porting checklist

- [ ] List every place your company actually thinks: chat, email, meetings, docs, and each source system that runs the business. That list is your set of taps.
- [ ] Build a raw layer that is append-only and dumb. It catches; it does not interpret. Nothing here is ever edited or deleted.
- [ ] Stamp every captured item at capture time with source identity, timestamp, and sensitivity class. Never plan to add these "later."
- [ ] Pick a fixed sensitivity vocabulary (we use public / internal / confidential / restricted) and apply it from the first item.
- [ ] Physically separate capture from interpretation. Capture writes to raw; a separate job reads raw and promotes.
- [ ] Make interpretation failures queue, not drop. If the model is down, raw keeps filling and the backlog reprocesses on recovery.
- [ ] Define the promotion boundary: how raw becomes curated (dedup, index target, who or what reviews).
- [ ] Point your agents at curated by default; keep raw as audit trail and re-processing source only.
- [ ] Set a retention policy per source and per sensitivity class before you scale, not after.
- [ ] Test the failure mode on purpose: kill interpretation for an hour, confirm raw still fills, confirm the backlog drains clean.

## For Compai readers

The intelligence layer from chapter 10t — the queries, the world model, the "what does the company know right now" surface — is only ever as honest as what flows underneath it. A brilliant intelligence layer on top of a frozen import is a confident liar. The spine is what keeps it fed. **A company brain is not a thing you build once; it is a recording you never stop making — and the spine is the part that never stops.** From here we move to chapter 10v, the domain indexes: how the curated layer gets organized into the shelves each agent actually reads from, so that "promoted into curated memory" becomes "landed in the right place for the finance agent, the CS agent, or the merch agent to find."
