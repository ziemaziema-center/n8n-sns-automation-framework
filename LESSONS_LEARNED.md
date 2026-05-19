# Lessons Learned

## The Practical Failure

A realistic failure is a preview that looks harmless in Telegram but maps to the wrong media asset after a retry. That is why content IDs, hashes, and approval timestamps need to travel together.

## Debugging Pain

The painful part of these systems is often not the first error. It is rediscovering the same error after context has moved from a terminal to a chat to a workflow export to a local note. Debugging gets slower when evidence is scattered.

## Context Loss

Context loss shows up as confident repetition: an agent retries an approach that was already rejected, a human forgets why a workflow was disabled, or a later patch removes a guard because the reason for it was never written down.

## Duplicate Execution

Duplicate execution is rarely dramatic at first. It looks like a repeated preview, a second alert, a duplicated render, or a repeated validation run. In public examples, that is annoying. In live systems, it can become reputational or financial risk.

## Approval Failures

Approval has to be attached to the exact artifact being approved. A vague "approved" flag is not enough when retries, regenerated media, changing captions, or multiple channels are involved.

## Orchestration Complexity

Multi-agent and workflow orchestration create coordination overhead. The useful pattern is not "more agents"; it is fewer ambiguous handoffs.

## Telemetry Gaps

Missing telemetry makes a project feel haunted by old decisions. The fix is mundane: write down what worked, what failed, what was validated, and what should not be repeated.

## Why Memory-first Emerged

Memory-first emerged because booting from project facts is cheaper than rebuilding them from conversation every time.

## Why Validation-first Emerged

Validation-first emerged because AI can produce plausible changes faster than humans can inspect every implication. The validation plan gives both the agent and the maintainer a shared finish line.

