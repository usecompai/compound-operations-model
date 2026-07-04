# Chapter 10w: The Context-to-Work Loop — From Signals to Governed Execution

A supplier emails on a Tuesday to say a fabric shipment will land eleven days late. Someone forwards it. The right person eventually reads it, understands what it means, notes that it touches a hero product going into a promotion, and files the note in the right domain index — exactly as our capture spine (10u) and domain shelves (10v) taught them to. The signal is now well-recorded, correctly tagged, provenance intact. A month later we stock out on that product mid-campaign. We paid for ads pointing at a page that said "sold out."

Here is the uncomfortable part: the brain did everything we asked of it. It captured the signal. It promoted it to the right shelf. If you had asked it "are there any supplier risks on hero products right now?" it would have answered brilliantly, with citations. And the stockout happened anyway — because nothing in the system was responsible for turning that answer into an action. We had built a library that knew about the fire. We had not built the thing that pulls the alarm.

That gap is the whole subject of this chapter. A knowledge base answers questions. An execution OS notices what changed and turns it into governed work. The difference is not intelligence — our brain was plenty smart. The difference is a **loop**: a defined path from a signal to a task somebody (or some agent) actually closes, with gates that keep it safe. This is the flagship chapter of "Operate & Compound" because everything before it was preparation. If you record everything (10u) and shelve it well (10v) but never close the loop, you have built the most expensive read-only wiki in your industry.

## The loop, stage by stage

The loop has five stages, and each one is a real object in our brain, not a metaphor.

**Signal.** A promoted, provenance-backed note living in a domain index — the output of 10v. In our worked example: *"Supplier X confirms fabric for [hero product] delayed to the 24th; original was the 13th."* It carries a source (the forwarded email), a timestamp, and a shelf (supply-chain risk).

**Candidate.** The system reads the shelf and proposes: *this looks like it needs action.* A candidate is not yet work — it is a hypothesis about work. It says: "This signal crosses a threshold we care about (a delay on a product with active demand), so a human or agent should decide whether to act." Candidates are cheap and disposable. Most should die here, and that is a feature, not a failure.

**Work object.** If the candidate survives triage, it becomes a scoped task with four required fields: an **owner** (who is accountable), an **authority level** (may this be executed, only proposed, or only flagged?), a **verification plan** (how we will know it worked), and a **terminal condition** (what "done" looks like). In our example the work object reads: *"Propose an inter-warehouse transfer of [hero product] to cover the 11-day gap; authority: propose-only, human approves; verify: available-to-sell quantity covers forecast demand through the 24th; owner: the merchandising agent, approver: head of ops."*

**Execution.** The agent does the reversible part — it drafts the transfer order against the inventory system, calculates the quantities, checks the source warehouse can spare them, and writes up a one-paragraph rationale. Then it **stops**, because the authority level said propose-only. A human reads the proposal, sees the numbers hold, and approves. Only then does the agent (or a person) commit the transfer in the POS/inventory system.

**Record.** The consequential action leaves a receipt: a single audit row capturing who proposed it, who approved it, when, what changed, and a link back to the triggering signal. That receipt goes back into the brain, which means the *next* time a supplier delay appears, the system can see we have handled this exact shape before, and how it turned out.

Run that end to end and the fire alarm rings. The delay email doesn't just sit there being well-filed — within a day it surfaces as a proposed transfer order on someone's approval queue, gets a yes, and executes. The stockout doesn't happen. That is the difference between a brain that knows and an OS that acts.

## The five gates

Every loop passes five gates. Skip one and you have built something that will eventually embarrass you.

### 1. Source gate

Is the triggering signal provenance-backed and from an authorized index? A loop may only fire from a real, promoted signal on a real shelf — never from a hallucination, a stray Slack message nobody vetted, or an index the agent had no business reading. If the signal can't point at its source, the loop never starts. This is what stops the system from inventing work.

### 2. Authority gate

Is this action within what this agent or person may do? Our authority matrix (shipped in the kit as `governance.yml`) draws three lines for every action type: **read**, **propose**, **execute**. The merchandising agent may *propose* a transfer but never *execute* a financial commitment. Reading inventory is fine unattended; moving money is not. The gate is checked before the work object is even created, so an agent never spends effort on work it could never be allowed to finish.

### 3. Verification gate

How will we know it worked — with a check, not a vibe? Every work object must name a verifiable condition *before* execution. "Available-to-sell covers forecast demand through the 24th" is a check: you can query it and get true or false. "The stockout risk is handled" is a vibe. If you cannot write the check, the work is not scoped yet — send it back to triage. Most bad automation we built failed here: it *did* something and declared victory without ever confirming the something worked.

### 4. Record / audit gate

Every consequential action leaves an audit receipt — a row of who, what, when, and evidence, conforming to the kit's `audit-event.schema.json`. Not for bureaucracy; for trust. When a founder asks "why did we move 200 units last Tuesday," the answer is one query, not an archaeology dig through Slack. Actions without receipts are how AI systems quietly lose the confidence of the people who run them.

### 5. Terminal state

Every loop **ends**. Done, rejected, escalated, or expired — but never open forever. A candidate that nobody triages within its window expires. A proposal that nobody approves in three days escalates or closes. The single worst failure mode of an execution OS is the **zombie loop**: work objects that accumulate, nag, and rot because nothing was allowed to declare them dead. A loop with no terminal state is a memory leak with a to-do list.

These five gates are the narrative behind the kit's `loop.yml` contract — *observe → choose → act → verify → record → stop.* The YAML is the skeleton; the gates are why each bone is there.

## Generation is cheap, closure is expensive

Here is the mistake we made, told plainly so you can skip it.

When we first wired signals to tasks, we were thrilled that it worked, so we ran the generator often — every hour, 24 times a day. It dutifully scanned the shelves and produced candidates. Within a week the team was drowning. The queue had dozens of items, most of them low-stakes ("a review mentioned sizing," "traffic dipped 4%"), and the genuinely urgent ones were buried among them. People started ignoring the queue entirely — which is worse than not having one, because now the urgent transfer order is *also* being ignored, sitting in a list everyone has learned to skip.

The lesson: **more tasks created is not more work done.** Generation is nearly free; a model can propose a hundred candidates before lunch. Closure — a human reading, deciding, verifying, recording — is the scarce resource. Optimizing the free thing while starving the scarce thing is how you build an anxiety machine.

We fixed it with two throttles. First, we dropped the generator to **twice a day** — a morning and an afternoon pass. Nothing important decays in twelve hours that a delay email hadn't already been sitting on for a week. Second, we capped the human digest at **ten items**, scored by impact, and let the rest wait or expire. If eleven things matter today, the eleventh is almost certainly not urgent, and forcing a human to triage it steals attention from the ten that are. A short, ruthless queue gets worked. An exhaustive one gets abandoned.

## Where the human sits

The instinct with agents is to chase autonomy — to measure success by how much runs without a person. That is the wrong target. In our deployment, the approval queue is not a limitation we are trying to engineer away; it is the **product**.

Four categories always stop at a human, by design: anything **customer-facing** (a message, a refund, a public change), anything **financial** (a payment, a commitment, a discount), anything touching **people/HR**, and anything **irreversible** (you cannot un-send, un-charge, or un-delete). For these, the agent does all the reversible preparation — the research, the draft, the calculation, the rationale — and then stops. The human's job shrinks from "do the work" to "check the argument and say yes or no."

That is the trade we want. The agent turns a founder's scarce judgment into the *only* thing they spend it on. A good approval queue is short, each item is well-argued, and a yes takes ten seconds because the verification check is right there. What we are explicitly *not* building is autonomy theater — agents executing financial or customer-facing actions unattended so we can claim a higher automation number in a deck. The number we optimize is not "percent autonomous." It is "how little human judgment does each good outcome require, and is that judgment spent on the things that actually need it."

## Porting checklist

- [ ] Pick one domain index (from 10v) and define what a *candidate* means there — the threshold that says "this signal might need action."
- [ ] Write your authority matrix: for each action type, mark read / propose / execute per agent and per human. Start restrictive.
- [ ] For each work-object type, require a **verification check** you can query for true/false — no vibes.
- [ ] Wire the audit receipt: one row per consequential action, who/what/when/evidence, linked to the source signal.
- [ ] Define terminal states and expiry windows so no loop can live forever.
- [ ] Set the four hard-stop categories (customer-facing, financial, HR, irreversible) to always route to a human.
- [ ] Throttle the generator (start slow — once or twice a day) and cap the human digest (start at ten, scored by impact).
- [ ] Adopt the kit's `loop.yml`, `governance.yml`, and `audit-event.schema.json` as your starting contracts, not blank files.
- [ ] Run it read-only for a week: generate candidates, but let humans do every action, and watch which candidates were noise.
- [ ] Only after the queue feels *trustworthy* should you let agents execute the reversible, low-authority steps.

## For Compai readers

Three chapters, one machine. **10u** taught the system to record everything — the capture spine that ensures nothing is lost. **10v** taught it to promote the signal that matters onto the right shelf — turning a pile of records into an index you can reason over. **10w**, this chapter, closes the circuit: it turns a shelved signal into governed work, with five gates that keep the work honest and a human sitting exactly where irreversibility begins.

**A brain that only answers is a cost; a brain that closes governed loops is the company running itself — carefully, on rails, with a person at every door that matters.**

The gates in this chapter are deliberately strict, and strictness raises a question we have so far answered with hand-waving: *who decides what an agent may do, and how do we change it safely as trust grows?* That is governance, and it is the next section. The `governance.yml` you adopted here is a single file today; next we make it a living system — authority that expands as agents earn it and contracts the moment they don't.
