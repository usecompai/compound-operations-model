# Chapter 10v: Domain Intelligence Indexes — From Raw Captures to Promoted Signals

You built the capture spine in the last chapter. Slack threads land in the brain. Email lands. Meeting transcripts land. Drive and Notion documents land. Everything you touch is written down. And then, three weeks in, you hit a wall you did not see coming.

It is a Tuesday. The finance owner asks the finance agent a simple question: "What is our returns policy for wholesale accounts?" The agent searches the brain, and it comes back with seven results. One is the actual policy. Two are Slack threads about a specific customer's return that got resolved and no longer matters. One is a supplier email about returning defective fabric. Two are meeting notes where someone said the word "returns" in passing. One is a logistics message about a return label printer that jammed. The right answer is in there. It is just buried under six pieces of noise that happened to share a word.

This is the second drowning. The capture spine solved "nothing is written down." It created a new problem: everything is written down, and nothing is findable. The pile grows faster than any human can read it. In our deployment we crossed 3,000 documents, and the raw capture rate kept climbing. A pile that big is not memory. It is a landfill you happen to own.

The fix is not more capture. It is a layer on top of capture: promotion into domain intelligence indexes.

## Promotion: the filter between noise and memory

Most of what gets captured is disposable. Scheduling chatter. One-off logistics. "Can you move the call to 3?" "Printer's fixed." "Thanks, sending now." This is the connective tissue of a working day, and next month none of it will matter. It should be captured (the archive is cheap) and it should never reach working memory.

A small fraction is durable. A decision got made. A rule got set. A fact got established that will still be true, and still matter, in thirty days. "We now offer 60-day returns on full-price wholesale, 30 on discounted." "We dropped the supplier in Portugal after the third late shipment." "The new size chart runs half a size small." These are signals. Promotion is the act of lifting a signal out of the raw pile and writing it into the index where the people and agents who need it will actually look.

What makes something durable enough to promote? A working test: would someone in this domain want this surfaced next month without knowing to search for it? If yes, promote. If it only matters to close out today's thread, leave it in the archive.

Every promoted signal carries a provenance stamp: a link back to the exact raw capture it came from. This is non-negotiable. A signal without provenance is a rumor. With the source link, anyone can click back to the original Slack thread or email and see the full context, the date, and who said it. When two signals disagree later, provenance is what lets you adjudicate.

Promotion runs in one of two modes. **Automatic-with-review**: the system proposes a promotion (an agent reads a thread, drafts the signal, files it in the right index) and a human confirms before it becomes canonical. **Manual**: a person decides this matters and writes it in themselves. Early on, run manual. You learn what "durable" means for your business by doing it by hand. Once the pattern is clear, let agents draft and keep a human on the confirm step. Fully automatic promotion with no review is how you poison your own memory with confident nonsense.

## One index per domain

The instinct is to build one big searchable index. Resist it. Build one index per operating domain. Here is the default set an SME should run:

| Index | What lives there | Primary readers |
|---|---|---|
| Strategy | Bets, positioning, annual goals, kill/continue calls | Founder, command center |
| Marketing | Campaign results, channel learnings, brand rules, creative wins | Marketing agent + owner |
| Retail / Sales | Store performance, wholesale terms, sell-through, pricing | Sales/retail agent + owner |
| Finance | Cash rules, margins, payment terms, refund policy, budgets | Finance agent + owner |
| Operations | Fulfillment rules, supplier decisions, logistics SLAs | Ops agent + owner |
| Product | Specs, size charts, materials, quality issues, roadmap | Product agent + owner |
| People | Roles, policies, comp bands, org decisions | People/HR agent + owner |
| Legal | Contracts, NDAs, compliance facts, obligations | Legal reviewer + founder |
| External partners | Agencies, vendors, key accounts, relationship history | Whoever owns the relationship |

Nine indexes, one per domain your company actually runs on. In our deployment, every capture source flows into these — Slack, email, meetings, Drive, Notion each have promoted intelligence layers now, and each promoted signal routes to the right domain index rather than into one undifferentiated heap.

Three reasons per-domain beats one pile:

**Retrieval quality.** The finance agent searching "returns" should hit refund policy, not fabric returns to a supplier. When the index is already scoped to finance, the noise from other domains is gone before the search even runs. This is the single biggest quality lever, and it is free.

**Scoping and permissions.** An index is the natural unit for who and what can read. Comp bands live in the People index; the marketing agent has no business there. One big pile forces you to choose between "everyone sees everything" and building a permission system on top of an unstructured mess. Per-domain indexes give you the boundary for free.

**Honest curation load.** A domain owner can actually review their own index — a few dozen to a few hundred signals is a readable, correctable body of knowledge. Nobody, human or agent, can review "everything." When curation is impossible, quality decays silently. Per-domain makes the review a real, assignable job.

## Reconciliation: when a new signal contradicts memory

Here is where it gets interesting. A new signal arrives to be promoted, and it contradicts a fact already in the index. Last month the finance index said "wholesale returns: 30 days." A meeting this week established "wholesale returns: 60 days on full-price." You cannot have both.

The moment a promotion candidate conflicts with an indexed fact, it does not silently overwrite and it does not silently get dropped. It triggers reconciliation. This ties directly back to the source-of-truth layer from Chapter 10t (layer 3). The question reconciliation asks is: which source wins?

The flow: the conflict is flagged, both signals shown side by side with their provenance stamps and dates. A human (usually the domain owner) decides. Newer does not automatically win — a formal policy doc outranks an offhand Slack comment even if the comment is more recent. The winning fact stays canonical in the index; the losing one is marked superseded, not deleted, with a link to what replaced it. Now the index carries not just the current truth but the history of how it changed. When the finance agent answers a returns question next quarter, it gives one answer, and it can show you when and why it changed.

Without reconciliation, contradictory facts pile up and your index quietly becomes as untrustworthy as the raw pile it was supposed to fix.

## An honest note from our deployment: watch the queue, not the count

We learned this one the embarrassing way. Our dashboards showed healthy numbers — total documents climbing, capture rate strong, everything green. What the dashboards did not show was the promotion queue. One day we actually looked and found roughly 2,000 captures sitting unpromoted, waiting for a review step that had quietly stalled. The archive was fat. The working memory was starving. Agents were answering from a stale index while three weeks of real decisions sat unpromoted in a queue nobody was watching.

Document count is a vanity metric. It only measures that capture works, which you already knew. The number that tells you whether your brain is alive is **promotion-queue depth**: how many captures are waiting to be triaged, and how long the oldest one has waited. A queue that grows without draining means your working memory is falling behind reality, no matter how green the totals look. Put queue depth and oldest-item age on the dashboard. Alert when either crosses a threshold. Assign the drain to a named owner per domain.

## Porting checklist

- [ ] Define your domain set (start from the nine defaults; cut or merge to match how your company is actually run).
- [ ] Create one index per domain with a named human owner accountable for its quality.
- [ ] Write the durability test in one sentence your team agrees on ("would someone want this next month without searching?").
- [ ] Route every capture source (chat, email, meetings, docs) into the domain indexes, not one shared pile.
- [ ] Make the provenance stamp mandatory — no signal enters an index without a link to its raw source.
- [ ] Start promotion in manual mode; graduate to automatic-with-review only once the durability pattern is clear.
- [ ] Define your source-of-truth hierarchy per domain (which document type outranks which) before you hit your first conflict.
- [ ] Wire reconciliation: conflicts flag, both sides shown with provenance, owner decides, loser marked superseded (never deleted).
- [ ] Put promotion-queue depth and oldest-item age on your dashboard; alert on both. Ignore raw document count as a health metric.
- [ ] Set a review cadence per index (weekly for fast domains, monthly for slow) and hold the owner to it.

## For Compai readers

Chapter 10u gave you the capture spine — the pipes that get every signal into the brain. This chapter gave you the filter and the shelves — promotion turns raw captures into durable signals, and domain indexes put each signal where its readers will actually find it. Together they close the gap between "we wrote it down" and "we can use it."

**Raw is the archive; the index is the working memory — and your agents read the index, not the pile.** That single distinction is what separates a company brain that gets sharper every week from a landfill that grows every day.

Next in the playbook we close the loop: how promoted signals in these indexes actually drive work — the context-to-work loop, where an agent reads its domain index, notices what changed, and turns a promoted signal into a task, a draft, or an action waiting for your approval. Capture feeds promotion; promotion feeds the indexes; the indexes feed the work. That is the whole machine.
