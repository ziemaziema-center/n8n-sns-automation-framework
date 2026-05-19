# Operational Notes

## Manual Review Still Required

Humans still review content risk, platform policy fit, brand tone, and any publish decision.

## What AI Should Not Automate Blindly

- Publishing, messaging, trading, or infrastructure mutation.
- Secret handling and credential rotation.
- Legal, compliance, platform policy, or financial risk decisions.
- Final public claims about readiness or adoption.

## Common Workflow Failures

- Skipping boot files because the task feels small.
- Treating a generated example as production-ready.
- Letting validation drift behind implementation.
- Recording telemetry that is too vague to help the next session.

## Onboarding Pain Points

New contributors may wonder why there are so many safety notes. The short answer is that these repos touch domains where a small automation mistake can escape the local machine.

## Brittle Areas

n8n exports can hide credential references in places that are easy to miss. Telegram callbacks need defensive parsing. FFmpeg jobs fail for mundane reasons like missing fonts, bad paths, and timing assumptions.

## Expected Learning Curve

Expect the first session to feel slower than a normal prompt. The payoff appears on the second and third sessions, when the project stops forgetting what it already learned.

