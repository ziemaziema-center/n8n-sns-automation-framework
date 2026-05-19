# Design Tradeoffs

## Why This Shape

This exists because content automation becomes unsafe when the generator and publisher are too close together. The uncomfortable bug is not a failed post; it is an accidental successful post.

## Decisions That Were Intentional

- Prefer plain files over hidden state so a reviewer can inspect the operating model.
- Prefer fixture paths before live integrations so a new contributor can reproduce behavior safely.
- Prefer explicit human approval for risky actions over pretending automation can infer intent.

## What Was Intentionally Avoided

A one-click autopublisher, real workflow exports, and credentials in examples. The public version keeps the publisher path stubbed because people copy examples under pressure.

## Why Simpler Alternatives Were Not Enough

A README-only approach explains intent but does not create a repeatable operating loop. A script-only approach can validate structure but cannot capture judgment. The current shape keeps docs, examples, and validation close together because the failure modes usually happen between those layers.

## What Still Feels Messy

n8n exports can hide credential references in places that are easy to miss. Telegram callbacks need defensive parsing. FFmpeg jobs fail for mundane reasons like missing fonts, bad paths, and timing assumptions.

## Where the Architecture May Break

The architecture breaks when approval state is stored loosely, when debug messages go to the same bot as approvals, or when duplicate protection only checks captions and not media identity.

## Scalability Concerns

The first scaling problem is not traffic. It is consistency. As more examples and adapters are added, each one must preserve the same safety boundary, fixture discipline, and validation expectation. Without that, the repo becomes a pile of special cases.

## Human Approval Still Required

Humans still review content risk, platform policy fit, brand tone, and any publish decision.

