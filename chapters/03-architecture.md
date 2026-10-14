# The architecture

The Brain holds context. Connected systems hold current operational data. People and AI agents use both through permissions that live outside the model.

```text
Chat / email / meetings / documents
                 |
          capture and organise
                 |
    shared memory: decisions, rules, history
                 |
        people + AI agents + skills
                 |
    sales / stock / accounting / other tools
                 |
          verify and keep the result
```

## Keep the boundaries clear

- Capture stores a source reference and its access scope. It does not make every message a fact.
- Retrieval assembles relevant context and reports missing, stale or conflicting evidence.
- A skill describes a method. A capability provides a tested, authorised way to act.
- The source system decides the current value of an order, stock position or invoice.
- A result is complete only after checking its destination and keeping the evidence.

The client and model can change without moving company memory or changing permission rules. A dashboard and an AI conversation can use the same foundation.

## First integration test

Use a fictional record. Retrieve permitted context, read the source, prepare a change, stop for approval, apply only after approval and read back the result. Repeat with an unauthorised identity and a failed source. Both must fail explicitly, not fall back to old values.
