# Checks before work is called done

Small, executable reference checks drawn from supervised customer care and people workflows. They contain no production adapters, secrets or company records.

Run from this directory:

```sh
python3 -m unittest -v
```

`draft_state` binds a draft to the exact sources used. A changed policy, changed order, incomplete conversation or expired check prevents presenting an old AI draft as current. Human edits are preserved for rechecking; revoked access still blocks presentation.

`next_attempt` separates a request known not to have started from an uncertain outcome. A timeout after a write requires reading the destination before another attempt. The example does not implement a queue or promise exactly-once execution.

`onboarding_state` keeps document review, human approval, assigned tasks and first access separate. An invitation alone cannot close the process.

These functions make decisions from facts supplied by trusted application code. They do not authenticate anyone, verify a signature, grant permission, send a message or create an account. Production needs authenticated source reads, durable storage, atomic updates, a destination-specific retry contract and tests under the actual employee and agent identities. Never take approval or evidence booleans from an LLM or a browser request without validation.
