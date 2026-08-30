# Chapter 23: The Company Operating Layer

A Company Brain is not a folder of documents and it is not a chat interface. It is the operating layer between what a company knows, what its systems show and what its people or agents are allowed to do.

```text
Slack / Gmail / Drive / Notion / meetings
                    |
              capture and digest
                    |
                    v
        operational memory and context
                    |
           compile for this job
                    |
                    v
      humans / models / agents + capabilities
                    |
                    v
       ERP / commerce / finance / CRM / etc.
                    |
                    v
        verify, record, learn or roll back
```

The model is intentionally replaceable. Company context, permissions, capabilities, evidence and execution history live outside it.

## The six runtime contracts

1. **ContextPack** — the minimum sourced, permission-aware context needed for one job.
2. **Capability Registry** — what the system can actually read, prepare or change, with a harmless smoke test.
3. **Policy engine** — who may use each capability, against which accounts and under which conditions.
4. **Run ledger** — what was requested, routed, attempted, blocked, verified and stored.
5. **Outcome Receipt** — what changed after an approved action and how that outcome was measured.
6. **Human review queue** — the explicit boundary for consequential decisions and ambiguous work.

A skill is a procedure. A capability is a procedure whose dependencies work now. An agent is a bounded operator over those capabilities. These are different objects and should not be marketed as one number.

## The execution state machine

```text
observed -> proposed -> approved / rejected -> applied
         -> impact_pending -> closed
```

Every state must have an owner, evidence and a terminal condition. A recommendation is not closed work. An action is not closed until the result is verified or the system records why verification was impossible.

## Ship it

- [ ] One real job produces a ContextPack with source references and known gaps.
- [ ] Every capability used by the job is `ready` in the registry.
- [ ] The actor's identity and authority are evaluated server-side.
- [ ] The run ends with a receipt, a human review item or an explicit blocked state.
- [ ] Any external effect is verified against the source system.
