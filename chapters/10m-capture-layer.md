# Capture company context

Capture approved chat, email, meeting notes and documents. Keep a durable source identifier, capture time, permitted author information, audience and original reference.

## The path

Discover changed items through an authorised connector. Deduplicate by source identifier and revision. Keep the raw reference in its private location. Extract useful context into a draft, then validate its promotion into shared memory. Advance the cursor only after the durable write succeeds.

Binary files belong in the document store; memory holds a digest and a link. A meeting note is not necessarily a verbatim transcript.

## Checks

Track backlog age, failed items and promotion status, not total volume. Replay a batch to prove idempotency. Test expired credentials, revoked access, deleted documents and malformed attachments. A failed capture must remain retryable without widening the audience.
