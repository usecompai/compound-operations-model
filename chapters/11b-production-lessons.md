# Checks that make the system usable

## Test the actual caller

A tool working in an admin shell does not prove it works for its employee or agent identity.

## Watch unfinished work

Totals can hide stuck queues. Monitor unprocessed-item age, failed promotion and outcomes awaiting checks.

## Restore the backup

A successful backup job is not recovery. Restore in isolation and check records, permissions and behaviour.

## Retry without duplicating

A timeout may happen after a write was accepted. Read back by idempotency key first.

If the destination cannot establish what happened, stop for reconciliation. Restarting an agent must not reset the attempt budget. [The checked-work example](36-checked-work.md) makes those decisions explicit.

## Keep permissions outside prompts

Enforce identity and scope in tools and source systems. Model instructions are not a security boundary.

## Show missing evidence

Do not turn source failure into a polished old answer. Keep stale and conflicting states visible.

In customer care, bind the draft to the conversation and policy versions used to write it. If either changes, recheck it. Preserve the reviewer's edits.

In product reporting, show the date of the underlying sales and stock records separately from the page refresh. A new export of old data is still old data.

These are engineering methods, not public incident statistics.
