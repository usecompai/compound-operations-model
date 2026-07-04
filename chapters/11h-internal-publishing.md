# Chapter 11h: Governed Internal Publishing — Where AI Work Products Go to Live

There is a graveyard in most companies now, and it fills up faster every month. Ours had five headstones the day we finally looked.

There was a liquidity dashboard, genuinely good, that told our finance lead within thirty seconds whether we could cover next month's supplier run. It lived on a personal preview link under an account nobody could quite name. There was a returns-analysis calculator a merchandiser built in an afternoon — a real tool, used weekly — parked on a free hosting tier tied to her personal email. There was a wholesale-margin report someone published once from a chat session and shared as a link that had already quietly expired. There was an inventory-aging view that lived, and only lived, as an attachment in a thread three hundred messages deep. And there was a hiring-funnel dashboard sitting on a laptop that walked out the door when its author changed jobs.

Five useful tools. Five orphan URLs. Zero of them on infrastructure the company controlled. No versions, no access control, no inventory, no way to answer the simplest possible question — "where's the liquidity dashboard?" — without a Slack archaeology dig. AI had made everyone at the company prolific, and prolific without a place to publish is just a wider mess. The work products were real. The company's ownership of them was fiction.

This chapter is about the fix: treating publication as a controlled runtime action, not as an LLM artifact. The model can generate a dashboard. Where that dashboard *lives* is an infrastructure decision, and it deserves the same governance as any other consequential action the system takes.

## Publication is a runtime action

The instinct is to think of a published dashboard as the *output* of the AI — the last thing that falls out of the session. That framing is the whole problem. It puts the artifact wherever the session happened to be standing, which is nowhere durable.

Reframe it. Publishing is an *action* the runtime takes, on par with sending an email or writing to the brain. And like every consequential action, it runs a fixed pipeline:

**`artifact → protected company URL → versioned publish → audit → brain closeout`**

Step by step:

1. **Artifact.** Someone — a person or an agent — produces the thing: an HTML dashboard, a calculator, a report. At this stage it is just a file. It has no home yet.
2. **Protected company URL.** The artifact deploys to one company-controlled route, behind company sign-on. Not a personal account. Not a preview link. A domain the company owns and can still reach after any single person leaves.
3. **Versioned publish.** Every deploy keeps history. The current version is explicit — you can point at exactly what is live — and rollback is one step, not a reconstruction project.
4. **Audit.** The publish leaves a receipt: who published what, when, to which URL, at which version. Publishing is consequential, so it gets the same treatment as any consequential action in the kit — an audit event.
5. **Brain closeout.** The artifact's existence and location get written back to the brain. This is the step everyone skips and the one that makes the whole thing durable. Without it, the tool exists but nobody can *find* it.

None of these steps is heavy. Together they turn "a link someone made" into "a company asset with a known location, a known owner, and a known history."

## The registry

The brain-closeout step needs somewhere to land. That's the registry: one record per published artifact, so the set of things the company has published is itself a thing you can read, search, and audit.

The minimum record is short. Any longer and nobody keeps it current.

- **Owner** — a role, not just a person. When the person changes, the role still owns the artifact. This is how you avoid the laptop-walks-out-the-door failure.
- **Purpose** — one line on what the thing is for. "Tells finance whether next month's supplier run is covered." Enough that a stranger knows in five seconds whether this is the tool they want.
- **Sensitivity class** — public, internal, confidential, or restricted. This is not decoration; it drives who is allowed to open the URL.
- **Source link** — back into the brain, to the doc or context the artifact was built from. So the artifact is never a dead end; you can always walk back to how it was made.
- **Versions** — current version and the one before it, so rollback and history are legible from the registry alone.

The moment an artifact has a registry entry, it stops being folklore. "Where's the liquidity dashboard?" is now a search, not a séance — the registry is part of the brain, findable like any other memory.

## Access follows spaces

A protected route is only half the control. Behind company sign-on, outsiders never stumble in — that closes the front door. But *inside* the company, not everyone should see every artifact. A confidential liquidity dashboard is not for all forty seats.

So who can *view* a published artifact follows the same Brain Spaces model that governs who sees what everywhere else (Chapter 10x). The artifact's sensitivity class comes from the capture spine (Chapter 10u); its space determines the audience. A `restricted` artifact in the finance space is visible to the finance space, full stop. You do not invent a second, parallel permission system for published pages — you inherit the one you already trust. The publishing surface enforces at the route; the space defines the list.

This is the difference between "behind a login" and "governed." Behind-a-login keeps strangers out. Governed decides, per artifact, which insiders belong.

## The dashboard that outlived its URL

The clearest lesson we have came from that first dashboard.

Our finance lead has no engineering background. That did not stop them from building a genuinely useful liquidity dashboard — the AI handled the code; they handled knowing what mattered. It worked beautifully. And the first version lived on a personal preview URL, because that is where the tool that built it put it by default.

It worked great right up until nobody could remember which account it was under. The dashboard was fine. The *URL* was a single point of failure wearing a person's name. Every day it kept running was luck.

Moving it to a protected company route with versioned publishes changed its category entirely. It stopped being "the finance lead's link" and became company infrastructure — owned by a role, findable in the registry, rollback-able, viewable by exactly the space that should see it. The dashboard outlived the URL it started on. That sentence is the whole point of this chapter. The work products your people build with AI should be more durable than the accidental place they were first published to.

## Anti-patterns

Name these out loud so people can catch themselves:

- **The orphan URL.** Final artifacts living on raw personal hosting, under an account tied to one person. It works until that person, or their memory, is gone.
- **"The link is the only copy."** No versions, no source, no way to rebuild. Lose the link, lose the tool.
- **Publish-from-chat.** Shipping straight out of a session with no registry entry. The artifact exists; the company doesn't know it does.
- **Secrets in the page.** Embedding tokens, keys, or raw customer data in a published artifact. A protected route is not an excuse to inline a credential.

## Porting checklist

- [ ] One protected, company-controlled route exists for internal artifacts, behind company sign-on.
- [ ] Every publish is versioned — history kept, current version explicit, rollback is one step.
- [ ] A registry exists: one entry per artifact with owner (role), purpose, sensitivity, source link, versions.
- [ ] Sensitivity classes reuse the capture-spine set (public / internal / confidential / restricted).
- [ ] View access follows Brain Spaces, not a new hand-rolled permission list.
- [ ] Every publish emits an audit receipt (who, what, when, where, version).
- [ ] Brain closeout is mandatory: the artifact's location is written back so it's findable.
- [ ] No secrets are embedded in published pages; a lint or review step checks for this.
- [ ] Owner is a role, so artifacts survive the person leaving.
- [ ] "Where is X?" is answerable by searching the registry, not by asking around.

## For Compai readers

If your people are building things with AI — and they are, whether you've noticed or not — those things need somewhere governed to live, or they will scatter across personal accounts and expiring links until an offboarding takes five tools down at once.

**Publication is a runtime action, not an LLM artifact: route it through a protected company URL, version it, register it, audit it, and write it back to the brain — so the work product outlives the URL, the session, and the person who made it.**
