# Architecture

## System Intent

Keep creative automation fast while making publishing deliberate, observable, and reversible.

## Main Components

- `clean_01_generator`: creates candidate reel/carousel payloads.
- `clean_02_approval`: sends Telegram previews and stores approval decisions.
- `clean_03_reel_renderer`: renders FFmpeg video assets from safe inputs.
- `clean_04_carousel_publisher_v2`: publishes only approved payloads.
- Debug bot: receives diagnostics, never user-facing approvals.

## Data Flow

Generated candidates become preview cards, approval callbacks write immutable decisions, render jobs create assets, and the publisher consumes only approved, deduped items.

## Trust Boundaries

- Local operator workspace.
- Sanitized public fixtures.
- Optional external APIs, which are disabled or stubbed in public examples.
- Telemetry and logs, which must never contain secrets.

## Failure Handling

- Prefer fail-closed behavior.
- Preserve append-only audit context for decisions.
- Use validation before mutation.
- Escalate ambiguous states to human review.

## Extension Points

- Add platform adapters for Instagram, Threads, TikTok, or YouTube Shorts.
- Add content scoring modules.
- Add richer preview formats.
- Add fixture-backed n8n workflow tests.

## Public Publisher Boundary

The public package contains a disabled/stub publisher path only. Any real platform publisher belongs in a private adapter until credentials, platform policy, rollback behavior, and approval state are reviewed.

