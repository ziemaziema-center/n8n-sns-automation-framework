# Publish Safety

## Required Controls

- Dedupe by content ID and platform asset hash.
- Verify approval timestamp and approver identity.
- Confirm target platform and account.
- Support dry-run mode.
- Keep rollback notes for every platform action.

## Rollback Pattern

Record post ID, asset ID, caption hash, publish time, and operator decision. If rollback is needed, manual operator confirmation is required.

