# Chapter 11i: The Organ Health Control Plane — Monitoring a System That Acts

The dashboard was green. Every tile: green. Capture rate, green. Agent uptime, green. Brain document count, ticking up and to the right — 2,987, 2,991, 3,001. We looked at it most mornings the way you'd glance at a thermostat: everything nominal, nothing to do.

Except one of our capture taps had stopped feeding three weeks earlier. A webhook token on a source system had silently expired, and from that moment the tap sent nothing. No error surfaced, because nothing errored — the source just went quiet, and quiet, on a totals-based dashboard, looks identical to calm. The document count kept rising the whole time, because six other taps were healthy and busy. One organ was half-deaf, and the vital-signs monitor read "all green" because we had built it to count what arrived, not to notice what stopped arriving. We found it by accident, when someone asked why a recurring report hadn't mentioned a whole category of activity in a month.

That is the failure mode this chapter exists to prevent. Once a brain feeds agents that *act* — send messages, move money-adjacent numbers, open tasks — monitoring stops being a nicety and becomes a governance organ in its own right. You are no longer watching a filing cabinet. You are watching a body.

## Nine organs

The reframe that fixed our monitoring: stop thinking "uptime" and start thinking anatomy. A living operating system has organs, each with its own job, its own healthy baseline, and its own way of failing quietly. Here are ours.

| Organ | What it is | Healthy looks like | Degraded looks like |
|---|---|---|---|
| **Disk** | Storage for the brain and the raw archive | Free space with headroom; writes succeed | Disk near full — new captures silently fail to land |
| **Transport** | The connections moving data: APIs, webhooks, sync jobs | Every sync ran on schedule; tokens valid | An expired webhook; a source quietly goes deaf |
| **Memory** | The brain itself: index freshness, promotion queue, canonical docs | Promotion queue shallow; index current; canon fresh | Queue backing up; docs unembedded for days; stale canon |
| **Procedural memory** | The skills, runbooks and prompts the system executes | Skills run; last-tested dates recent | A runbook errors on invocation; last-tested months ago |
| **Sensors** | The capture taps (see 10u) | Every tap has a recent last-capture timestamp | A tap's timestamp is frozen — a sensor has failed |
| **Action control** | The approval and receipt gates (see 10w) | Approval queue drained; every action has a receipt | Approvals piling up; actions executed without matching receipts |
| **Autonomy** | How much runs unattended vs blocked | Jobs flow; provider states nominal (see 10z) | Work stalled on humans; a provider in a failure state |
| **Observability** | The monitoring itself | Health checks run and report freshly | A dead health check that reads as "all green" |
| **Channels** | The human-facing surfaces | Digests arrive; notifications flow; dashboards load | A silent digest; a broken notification path |

Each organ deserves one plain sentence you can say out loud to a non-technical colleague. Disk: if it fills, capture dies without a sound. Transport: connections rot, and a rotted one goes silent, not loud. Memory: a brain that files faster than it indexes slowly stops being able to recall. Procedural memory: skills you never re-test are skills you only *assume* still work. Sensors: a tap that stopped is worse than a tap that errors, because errors get noticed. Action control: an action without a receipt is an action you cannot audit. Autonomy: the useful number is not "is it up" but "how much is running without a human unblocking it." Observability: the watcher can die, and a dead watcher is indistinguishable from perfect health. Channels: the whole system can be healthy and still useless if the report never reaches you.

## Degraded organs become tasks

Here is the one design rule that separates this from every dashboard you have ever ignored: **a degraded organ produces a task in the approval and work queue, not merely a colour on a screen.**

Dashboards get glanced at and forgotten. Queues get drained, because draining a queue is how work gets done in the rest of the system (see 10w). So when an organ crosses a threshold, our health system does not repaint a tile red and hope someone is looking. It opens a work object — the same kind of work object an agent's proposed action produces — and it lands in the same queue a human already checks. The green-dashboard incident could not have run for three weeks in this model, because a frozen sensor timestamp would have opened a task on day one, and that task would have sat unresolved in a queue someone drains daily.

Every degradation task carries four things, no exceptions:

1. **Which organ** — sensors, memory, transport, named plainly.
2. **What threshold tripped** — "tap X last captured 26 hours ago; threshold is 24," not "something's off."
3. **The recovery action** — the specific next step, tied to the recovery actions we defined in 10z. Re-issue the webhook token. Restart the sync. Run the promotion job.
4. **Who can do it** — an owner role, not a name, so the task routes even when a specific person is away.

A degradation task that says "memory: degraded" is a dashboard tile wearing a costume. A task that says "memory degraded — promotion queue at 2,000 docs, threshold 200; run the promotion job; owner: brain maintainer" is something a person can pick up and finish. The difference is whether the alert is *actionable at the moment it arrives*.

Two of our own scars are baked into these thresholds. The first: we once let 2,000 documents sit unembedded and unpromoted for weeks. The memory organ was degraded the entire time, and every dashboard was green — because we tracked the *total* document count, which looked magnificent, instead of the *promotion queue depth*, which was screaming. Green dashboards lie when you track totals instead of queues (see 10s, 10v). The second: we had a backup we had never once restored. It ran nightly, it reported success nightly, and it was, functionally, a rumour. A backup you have never restored is a hypothesis, not a backup — so the disk organ's health check now includes a periodic test-restore, and until that restore passes, the backup counts as unverified, not healthy.

## Watching the watcher

The observability organ is the one people forget, and it is the one that makes every other organ trustworthy. If the health system itself dies, every other check stops updating — and a check that stops updating, on most dashboards, still shows its last value: green. A dead monitor is the most dangerous state in the whole body, because it actively impersonates good health.

So the watcher needs watching. The mechanism is embarrassingly simple: the health system must emit a fresh heartbeat every cycle, and a *separate*, dumber process checks only one thing — did that heartbeat arrive on time? If the heartbeat is stale, that itself opens a task: "observability: no health report in N hours." We treat "no news" as bad news by default. A health report that is silent is not reassuring; it is the single loudest alarm we have, because it means we have gone blind and don't yet know to what.

## Cadence

Organs do not all beat at the same speed, so we do not check them all on the same schedule. Forcing a weekly rhythm onto disk means learning about a full disk six days late; forcing an hourly rhythm onto every skill test is just noise.

- **Hourly:** disk, transport, sensors — the fast-failing, silent-dying organs where a day's delay means a day of lost capture.
- **Daily:** memory (promotion-queue depth, index freshness), action control (approval-queue depth, receipt matching), autonomy, channels.
- **Weekly:** procedural memory — a rotating test-run of skills and runbooks to confirm they still execute, plus the periodic backup test-restore.

On top of the per-organ schedules sits one human-facing artefact: a **weekly organ-health report** that lands in the founder's digest (see 10w, Channels). It is a one-glance summary — nine organs, nine statuses, and any task references already opened. Crucially, the weekly report is a *summary*, not the alerting mechanism. Anything red does not wait for the weekly cadence; it opens a task the moment the threshold trips. The report exists so a healthy week is visibly, boringly healthy — and so the week the green dashboard would have lied to you, the report instead points at an open task with your role's name on it.

## Porting checklist

- [ ] Name your organs. Start with these nine; add any your stack has that these miss.
- [ ] For each organ, write the healthy baseline and the degraded signature in one plain sentence each.
- [ ] Track **queue depths and last-success timestamps, never totals.** Totals go green while queues drown.
- [ ] Wire each degradation to **open a task** in your existing work/approval queue — not to paint a dashboard tile.
- [ ] Put four fields on every degradation task: organ, threshold tripped, recovery action, owner role.
- [ ] Add a heartbeat for the health system itself, checked by a separate process. Treat "no report" as red.
- [ ] Set per-organ cadences (fast-silent organs hourly; queue organs daily; skills/backups weekly).
- [ ] Include a **test-restore** in the disk/backup check. An untested backup is unverified, not healthy.
- [ ] Route a weekly organ-health summary into the human digest — as a summary, not as the alert path.
- [ ] Pick real thresholds from your own incidents, not round numbers you like the look of.

## For Compai readers

This closes the Governance section, and it closes it on purpose. Everything earlier was an organ of one body. Capture (10u) is the sensors. The indexes and promotion queue (10v) are the memory. The work objects and approval queue (10w) are the action control. Provider failure states (10z) are the autonomy. Backups and anomalous-change alerts (10s) are the disk and the immune response. Publishing and digests are the channels. This chapter is the nervous system laid over all of it — the thing that notices when any organ goes quiet and turns that silence into a task a human will actually drain.

The temptation, once you have a brain that captures and agents that act, is to prove it is healthy with a wall of green tiles. Resist it. Green tiles measure what showed up; they are structurally blind to what stopped. **A monitoring system that counts what arrives will always look healthy while a source goes silent — so measure the queues and the last-success timestamps, and make every degradation open a task, because dashboards get ignored and queues get drained.** That single inversion — from colours to tasks, from totals to queues — is the whole difference between a system you *hope* is healthy and one that tells you, in writing, in a queue, the day it isn't.
