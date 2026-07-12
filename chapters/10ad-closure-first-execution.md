# Chapter 10ad: Closure-First Execution — Automate the Finish, Not the Backlog

## We built a task generator and called it execution

The first context-to-work system looked productive. It watched the brain, found signals, created tasks and generated outputs. The counters climbed every day.

Then we measured terminal states.

The historical run had created **679 tasks, 357 signals and 356 proactive outputs**. Roughly **0.3%** of the work reached verified closure. The system had automated the cheapest part — proposing more work — while leaving selection, verification and finishing to humans.

So we paused it.

That decision improved the architecture more than another model upgrade would have. It gave us the correct unit of autonomous work: **one approved task that becomes one verified artifact and advances to a terminal state.**

## Generation is not progress

A candidate, a task and an output are different objects:

```text
signal -> candidate -> approved task -> artifact -> verification -> terminal state
```

- A **signal** says something may matter.
- A **candidate** explains what could be done.
- An **approved task** has owner, sources, authority, acceptance criteria and stop condition.
- An **artifact** is the work product.
- **Verification** compares the artifact with the source and acceptance criteria.
- A **terminal state** is done, clean no-op, blocked, approval-required or failed validation.

Only the last transition counts as closure.

## The bounded pilot

The next autonomy stage in the reference deployment is intentionally small:

1. Observe the existing approved queue.
2. Select at most one task that meets every input gate.
3. Execute one bounded, reversible action or artifact.
4. Verify it against the source system and acceptance criteria.
5. Link the artifact and advance the task lifecycle.
6. Record the outcome and stop.

The loop does not invent unlimited tasks. It does not keep going because it still has tokens. It stops after one completed unit or enters a named blocked state.

## Promotion gates

Before increasing authority or throughput:

- ten consecutive reviewed runs;
- at least 80% accepted outputs;
- zero unauthorized actions;
- every successful run creates a linked artifact;
- every run advances a lifecycle state;
- no customer-facing, financial, people, legal or irreversible mutation without explicit approval.

These thresholds are not a universal standard. They are the reference deployment's current pilot contract. The portable principle is that autonomy expands only after reviewed evidence, never from a demo or a confidence score.

## Market autonomy by capability

An organization does not have one autonomy percentage. A support classification may be L4 while refunds remain L2. Invoice extraction may be L3 while payments remain L0. A weekly report may run unattended while the recommendation it contains still needs approval.

Report the capability and authority boundary:

| Capability | Current state | Human boundary |
|---|---|---|
| Capture and indexing | Deployed | Review gaps and sensitive sources |
| Retrieval and source checks | Deployed | Resolve conflicts |
| On-demand analysis | Deployed | Approve consequential decisions |
| Drafting and proposals | Deployed | Approve external or risky actions |
| Autonomous closure | Controlled pilot | One approved task per run |

That is more credible than "91% autonomous," and more useful to someone building the same system.

## The receipt

Every run should leave a compact record:

```yaml
task_id: task-2026-0712-0042
source_refs:
  - source-system://record/123
authority: draft_only
artifact: outputs/weekly-reconciliation.md
verification: passed
terminal_state: review
stop_reason: one_task_completed
```

The receipt is how the brain learns what actually happened. Without it, the next agent sees prose but not state.

## Porting checklist

- [ ] Measure closure, not tasks or outputs created.
- [ ] Consume an approved queue before generating new work.
- [ ] Require owner, sources, acceptance criteria and stop condition.
- [ ] Execute one bounded unit per pilot run.
- [ ] Verify against source systems, not the model's confidence.
- [ ] Record the artifact and advance lifecycle state.
- [ ] Name blocked and approval-required outcomes.
- [ ] Expand authority only after reviewed consecutive runs.

## For Compai readers

The most autonomous-looking system is not always the most useful. The winning system is the one that finishes a small number of real things, proves them and stops cleanly. **Automate closure before you automate volume.**

