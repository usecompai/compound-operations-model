# Finishing work safely

An agent can lose its connection after asking another system to do something. That is not the same as knowing nothing happened.

## Check before repeating

Keep a record of each attempt outside the conversation. Distinguish work that never started, work with an unknown result and a result verified in the destination system. If the result is unknown, read the destination before trying again. Stop when the attempt budget is exhausted.

This reduces duplicate actions; it does not promise exactly-once delivery. The application still needs durable storage, authentication and a way to match the original request to its result.

## Check the evidence again

A draft refers to particular source versions. Before presenting it, check whether the conversation, policy or related record changed. Preserve a person's edits and flag them for review instead of replacing them with a fresh generation. If access was revoked, stop serving the content.

## Check as the actual user

A connector working for an administrator does not prove it works for the employee or agent who needs it. Test with that identity, in its workspace, and read the result back. A successful tool response alone does not establish that the business task is finished.

Applications also need their own restricted operating-system users. Moving a service away from administrator access is not finished until its real readers and writers still work with the intended file permissions. A passing health check cannot establish that.

## Check the handoff to the person

For an agent working through chat, keep the incoming request, completed task, final answer and destination linked. Check that the intended answer was accepted by the delivery service. That is not proof that the person read it, and an internal audit record is not a substitute for the answer.

## Try the checks

[The checked-work example](../kit/patterns/checked-work/README.md) includes executable tests for source changes, revoked access, uncertain attempts and hiring handoffs. It is deliberately a small decision layer, not a production queue or permission system.

The tests use fictional inputs. They illustrate checks used in private workflows without distributing those applications or their data.
