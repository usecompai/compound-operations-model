# Chapter 10z: Provider Failure Semantics — Jobs That Say Why They Stopped

For six days, one of our scheduled jobs "ran" every morning. The cron fired at 06:00. The process started, logged a line, and exited zero. Green check. No error in any dashboard. And every one of those six mornings, it produced nothing — an empty brief where a filled one should have been.

We didn't notice because nothing looked wrong. The job wasn't crashing. It wasn't throwing. It was calling a model provider, getting an error back from that call, catching it, writing "no output today" into a file nobody reads at 06:00, and exiting cleanly. Six clean exits. Six blank briefs. The failure was real from day one; the *signal* of the failure took a week to arrive, and only arrived because a human happened to go looking for a brief that was never there.

That is the shape of almost every home-built AI automation failure we've seen: not a loud crash, but a quiet, well-behaved job that has stopped doing its job and doesn't tell you. The outage isn't the damage. The **silence** is the damage. A provider goes down for two hours and you lose two hours of work; a provider goes down for two hours and your job hides it, and you lose six days before anyone asks the right question.

This chapter is the operational completion of a thesis this book keeps returning to: the model is rented, the brain is owned (Chapter 18). If the model is rented, then the landlord can lock the door on you at any time — expected, routine, no malice. **Provider failure is a normal operating state, not an exception.** So every AI job has to be built to say, out loud, *why it is not running* — not just *that* it stopped.

## Four states, not two

The trap is thinking a job is either `ok` or `failed`. Two states can't tell you what to do next. We run four, and every scheduled AI job reports exactly one of them each time it runs:

| State | What it means | Who acts | Typical fix |
|---|---|---|---|
| `ok` | Ran, produced valid output | Nobody | — |
| `blocked_provider_unavailable` | The provider is down or degraded upstream; the job is healthy and waiting | The system (auto) | Wait, retry with backoff, or reroute to another provider |
| `blocked_reauth_required` | A credential or session was invalidated; the provider won't answer until a human re-authenticates | **A human** | Re-authenticate provider X on host Y — 5 minutes |
| `failed_validation` | The provider answered, but the output failed our checks | A human (investigate) | Open a work object; the input or the check is wrong |

The two `blocked` states and the one `failed` state are the whole point. `ok` is easy. The other three are where a home-built system either saves you or quietly betrays you.

## Blocked is not failed

This is the distinction most systems collapse, and collapsing it is expensive.

**Blocked means the job is healthy and waiting on the world.** Nothing is wrong with your prompt, your input, your logic, or your output. The provider isn't answering — an outage, a rate limit, an invalidated session. The correct response is to *wait, retry, or reroute*. There is nothing for you to fix in the job itself. If you page an engineer at 3 a.m. for a `blocked_provider_unavailable`, you've trained your team to ignore alerts.

**Failed means the job produced something wrong.** The provider answered, the pipeline completed, and the result didn't pass validation — a malformed number, an empty section, a hallucinated field, a schema mismatch. The correct response is to *investigate and fix*. Something in your system, or your checks, needs a human's judgment.

These demand opposite reflexes. Blocked says *be patient, or route around*. Failed says *stop and look*. A single "error" state forces you to reverse-engineer which reflex applies every single time — and under pressure, people guess wrong. Naming the states up front is how the job tells you which reflex to bring before you've even opened it.

## Our reauth story

Here is the honest version, anonymized. For several weeks, one of our providers kept invalidating its refresh sessions. Not an outage — the provider was up. But every so often the stored session went stale, and any job depending on that provider would get an auth error the moment it called out.

At first, those jobs looked *idle*. They weren't erroring loudly; they were catching the auth failure and exiting like our six-day cron above. From the outside, a blocked job and a job with nothing to do are indistinguishable — both just... don't produce anything. We lost real days this way, repeatedly, because "quietly produced nothing" reads as "nothing to do" until you prove otherwise.

The fix was not a better retry loop. Credentials do not self-heal — no amount of backoff re-authenticates a dead session; only a human logging in does that. The fix was to make the state **loud and specific**. We taught those jobs to distinguish "the provider is down" from "the provider rejected my credentials," and to surface the second one in the daily digest with the exact human action attached: *re-authenticate provider X on host Y.* Not "job failed." Not "check the logs." The person, the host, the action — in the one place a human already looks every morning.

The moment that surfaced, the failure changed size. What had been a silent multi-day gap became a five-minute fix: read the digest, log in on host Y, done. When the session recovered, the queue drained on its own and the backlog cleared (Chapter 10u — capture outlives interpretation; the work waiting to be done was still sitting there intact). Nothing about the provider got more reliable. Our *relationship to its failure* did.

## Design rules for provider-resilient jobs

Six rules, learned the expensive way:

1. **Every scheduled AI job declares its provider dependency and reports its current state.** No job is allowed to be a black box. If it calls a model, it names which one and says which of the four states it's in.
2. **Blocked states carry the recovery action and who can perform it.** A state without a next step is just a nicer-looking silence. "Blocked" means nothing; "re-authenticate provider X on host Y — ops can do it" means everything.
3. **`blocked_reauth_required` always pages a human.** Credentials never self-heal. This is the one blocked state that is never patient — it waits on a person, so it must reach a person.
4. **`failed_validation` never retries blindly.** Same input plus same model equals the same bad output. Retrying a validation failure just burns tokens to reproduce the problem. Instead it opens a work object for a human (Chapter 10w) — the failure becomes a task, not a loop.
5. **States are visible on one surface, not buried in logs.** Nobody greps logs at 06:00. Job states live on the organ-health surface (next chapters) and roll up into the daily digest. If a human has to go looking, you've already lost the days.
6. **Provider health informs where you route work.** When you run more than one provider, a `blocked_provider_unavailable` on one isn't a wait — it's a signal to route to the other. This is the practical cash value of model-agnosticism: reroute, don't wait.

These states don't need a new template — they belong in the loop contract the kit already gives you (the `loop.yml` covered earlier). Add a `provider_states` block:

```yaml
provider_states:
  ok: run produced valid output
  blocked_provider_unavailable: { action: retry_or_reroute, actor: system }
  blocked_reauth_required: { action: reauthenticate_on_host, actor: human }
  failed_validation: { action: open_work_object, actor: human }
```

Six lines. Now every job that inherits the contract inherits the vocabulary.

## The payoff of owning the brain

Here is where the whole thesis pays off at the operations level.

If your context lived *inside* one provider — its memory, its threads, its proprietary state — then that provider going down or locking you out would mean your work stops until *it* comes back. You'd have no choice but to wait. Your resilience would be capped at your least-reliable vendor's uptime.

But the brain lives outside every provider. The context, the history, the work-in-progress — all of it is in markdown and git, owned by you, readable by any model. So when one provider throws `blocked_provider_unavailable`, the job doesn't have to wait for that specific landlord to unlock the door. It can hand the exact same context to a different provider and keep going. **Reroute, don't wait** is only possible because nothing important was trapped inside the thing that failed.

That's the quiet superpower of "the model is rented, the brain is owned." It's not just a philosophical stance about lock-in. At 06:00 on a morning when one provider is degraded, it's the difference between a blank brief and a brief that got written by a different model against the same owned context — and a state line that tells you, plainly, which one happened and why.

## Porting checklist

- [ ] Every scheduled AI job reports one of four states — `ok`, `blocked_provider_unavailable`, `blocked_reauth_required`, `failed_validation` — never a bare pass/fail.
- [ ] Each job names the provider(s) it depends on.
- [ ] `blocked` states carry a recovery action and the actor who can perform it.
- [ ] `blocked_reauth_required` pages a human every time; it is never retried silently.
- [ ] `failed_validation` opens a work object instead of retrying blindly.
- [ ] All job states surface on one shared surface and roll into the daily digest — not the logs.
- [ ] A `provider_states` block is added to your `loop.yml` contract.
- [ ] If you run more than one provider, degraded-provider state triggers a reroute, not a wait.
- [ ] You have tested it: kill a credential on purpose and confirm the right human gets the right action within one digest cycle.

## For Compai readers

Most AI-automation advice obsesses over making the model call succeed. The harder, more valuable work is making the *failure* legible — because in production, failure is not rare, it's Tuesday. Providers go down, sessions expire, outputs come back malformed; none of that is avoidable and all of it is survivable, *if the job tells you what happened and what to do about it*.

**The outage never costs you much; the silence does. A job that fails loudly and names the fix is worth more than a job that succeeds quietly, because you can only trust automation you can see stop.** Build the four states, attach the recovery action, put it where a human already looks, and keep your context out of any single provider so you can reroute instead of wait. That's the whole discipline: not preventing provider failure, which you can't, but refusing to let it happen in the dark.
