# Chapter 10y: The Structured Data Sidecar — When Markdown Is the Wrong Container

Someone on our finance side wanted to know why one bank account looked light for the month. Reasonable question. To answer it, they did the obvious thing: exported the month's movements — about 40,000 rows — and pasted the table straight into a markdown doc in the brain, so the AI could "just read it." The commit landed. And everything downstream got a little worse. Search started surfacing that one monster file for half-related queries. Git diffs on the folder turned into walls of pipe characters. The agent, asked a simple "what was the total for vendor X," dutifully loaded the whole thing into context, chewed through tokens, and gave an answer that was *close* — off by a rounding error it introduced somewhere in row 12,000, because reading a 40,000-row table is not the same as summing it. We had taken a structured-data question and forced it through a semantic-memory container. The container held, technically. The answer didn't.

That is the whole lesson of this chapter, and it closes THE BRAIN section on purpose. Everything before this taught you to put meaning into markdown. This one draws the boundary: **markdown is the right container for decisions, rules, and narrative memory, and the wrong container for 100,000 order rows.** The brain is semantic context. Big tabular data belongs in a structured data sidecar that sits next to it.

## Two containers, one system

Think of it as two containers serving one brain. The brain holds *meaning* — what a thing is, why it matters, what decision it feeds, who owns it. The sidecar holds *rows* — the actual movements, orders, line items, snapshots. They are different kinds of information and they fail in different ways when you cram them into the wrong place. Prose stuffed into a database becomes unsearchable and lifeless. Tables stuffed into prose files bloat the repo, poison search, and make the model squint at numbers it should be computing.

The join between the two is a small markdown file we call a **dataset card**. One card per dataset, living in the brain, written in plain language: what this dataset is, where it came from (which capture source), what decisions it feeds, how sensitive it is, and where the actual rows live in the sidecar. The card is the meaning; the sidecar rows are the substance. An agent answering a question reads the card first — *what am I even looking at, and am I allowed to?* — and only then runs a query against the sidecar for the numbers. Provenance flows both ways: the card points to the data, and the data traces back to a documented source and owner. Nobody, human or agent, queries a pile of rows they can't explain.

## DuckDB for questions, DuckLake for history

The sidecar is a local analytical database. We use two open tools, and the choice between them is genuinely simple.

**DuckDB is for questions.** It reads CSV, JSON, Parquet, and Excel exports directly and fast, with no server to run and no ceremony. You point it at a file — or a folder of files with the same shape — and ask SQL questions. This is the right tool for ad-hoc analysis and for imports you'll refresh and overwrite: "load this export, tell me the total, the outliers, the top 20." Most sidecar work is DuckDB work.

**DuckLake is for history.** When a dataset needs to be *durable and versioned* — snapshots you can compare over time, reconciliations you have to reproduce months later, tables that back a dashboard people trust — you want more than a file you overwrite each week. DuckLake gives you versioned datasets: point-in-time snapshots so that "how did stock cover look in March?" is still answerable in April, because March's numbers were never overwritten. Rule of thumb: if you'd be upset to lose last month's version of the numbers, it belongs in DuckLake, not a re-run of DuckDB.

## The thresholds

You don't need a committee to decide what goes in the sidecar. If a dataset trips any one of these, it's sidecar data, not brain data:

- **More than ~10,000 rows.** Below that, a markdown table is often fine. Above it, search and diffs start to hurt.
- **More than ~50MB.** Large files bloat the repo and slow every clone and sync.
- **Multiple files of the same shape.** Monthly exports, per-store dumps — anything you'd want to stack and query together.
- **Schema drift over time.** Columns that get added, renamed, or reordered across exports. The sidecar tracks this; markdown just accumulates the mess.
- **Any recurring reconciliation.** Bank versus accounting versus commerce platform — if you compare the same sources on a cadence, the numbers live in the sidecar and the *conclusion* lives in the brain.

## Worked examples

**Reconciling cash across six accounts.** We pull movement exports from six bank accounts and the accounting system's ledger, load them all into the sidecar, and run one SQL query that flags where they disagree. Doing this by reading exports into the model was slow and error-prone; as a join across loaded tables it's a few seconds and it's *exact*. The brain holds the dataset cards and the standing rule for what counts as a real discrepancy; the sidecar holds every line and does the matching.

**Multi-store sell-through.** To see how a product actually moved across five stores plus online, we join the POS/inventory system's export against the commerce platform's export in the sidecar — two systems that never talk to each other natively. One query gives sell-through per SKU per location. That join is impossible inside markdown and painful against two live APIs; in the sidecar it's routine, and the resulting read ("these three styles are dead in two stores") goes back to the brain as a note that feeds a buying decision.

**Historical snapshots.** Because we snapshot certain datasets into DuckLake on a cadence, questions with a *when* in them become answerable. "How did stock cover look in March?" asked in April isn't a shrug — March's snapshot is right there, untouched. The brain records what the snapshot means and why we keep it; DuckLake keeps the frozen rows.

Honest note: our first instinct was to make the model read the giant CSVs directly. Context windows made it lossy and expensive — the answers drifted and the bill didn't. Moving the same questions into the sidecar made them cheap, exact, and repeatable. SQL beats squinting. We wish we'd drawn this line on day one instead of after the first 40,000-row commit.

## Porting checklist

- [ ] Any dataset over ~10k rows or ~50MB is **out** of markdown and into the sidecar.
- [ ] A local DuckDB database exists next to the brain for ad-hoc imports and analysis.
- [ ] DuckLake (or equivalent versioned store) is set up for datasets that need durable snapshots.
- [ ] Every sidecar dataset has a **dataset card** in the brain (meaning, source, decisions, sensitivity, location).
- [ ] Each card names its **capture source**, so provenance traces both directions.
- [ ] A sensitivity class is assigned to every dataset and honored by whoever (or whatever) queries it.
- [ ] Recurring reconciliations (bank vs accounting vs commerce) run as SQL joins, not as model reading.
- [ ] Refresh cadence is written down per dataset — nobody guesses whether the numbers are current.
- [ ] Snapshots are taken on a defined cadence for anything you'd hate to lose a prior version of.
- [ ] A retention rule exists so the sidecar doesn't grow without bound.

## For Compai readers

This is where the capture spine (Chapter 10u) lands its heavy end. Semantic captures — decisions, rules, notes — flow into the brain as markdown. Structured captures — the exports, the ledgers, the dumps — flow into the sidecar, and each one gets a dataset card in the brain so meaning and rows stay wired together. The two spines share one nervous system; they just terminate in different containers.

It also feeds the context-to-work loop. A reconciliation that flags a real discrepancy isn't a curiosity — it's a work object. The sidecar surfaces the anomaly with numbers behind it; the brain turns that anomaly into a task with an owner, and the dataset card is the receipt that lets anyone re-run the exact query later. **Meaning lives in the brain, rows live in the sidecar, and a one-page dataset card is the contract that keeps an AI from ever answering a number it can't trace.**
