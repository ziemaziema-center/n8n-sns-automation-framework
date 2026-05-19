# Pre-push Validation

## Required Command

```bash
python validation/validate_repo.py
```

## Manual Review

Also run a manual scan for private data before the first public push. Do not rely on automation alone for the initial publication boundary.

## What to Inspect

- `.env.example` contains placeholders only.
- GitHub workflow files do not deploy, publish, or use secrets.
- Examples do not contain private URLs, credential IDs, Telegram chat IDs, account data, or raw execution traces.
- Screenshots and GIFs are redacted.
- The README does not claim production readiness beyond the validated public path.

