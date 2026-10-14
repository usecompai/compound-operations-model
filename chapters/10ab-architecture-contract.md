# Architecture contracts

Define boundaries before connecting components.

- Identity comes from authentication, not a prompt.
- Context includes sources, audience, freshness and gaps.
- Capabilities specify inputs, permitted actions, outputs and failures.
- Execution specifies idempotency, timeouts, approval and retry rules.
- Results specify the destination, verification and remaining owner.

Use versioned machine-readable schemas. Validate inputs before side effects and outputs before marking work complete.

Test compatibility before changing a shared contract. Consumers must understand a new version or fail explicitly. Never discard an unknown permission field and continue with broader access. Record migration and rollback before a breaking change.
