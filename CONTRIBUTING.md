# Contributing

Thanks for considering a contribution. This ecosystem is built around safe automation, reproducible validation, and explicit operator control.

## Contribution Principles

- Prefer small, reviewable pull requests.
- Add or update validation for behavioral changes.
- Keep public examples sanitized and runnable without private services.
- Never include real `.env` files, tokens, API keys, PEM files, n8n credential exports, execution logs containing secrets, or private webhook URLs.
- Treat social publishing, messaging, affiliate links, and finance workflows as safety-sensitive surfaces.

## Local Workflow

1. Fork and clone the repository.
2. Copy `.env.example` to `.env` only in your local environment.
3. Run the documented validation command before opening a pull request.
4. Use the pull request checklist to document safety impact.

## Review Standard

Maintainers should prioritize correctness, safe defaults, clear operator intent, and traceable telemetry over feature velocity.

## Exact Validation Commands

Run the structural validator:

```bash
python validation/validate_repo.py
```

Then run the repo-specific demo command from `QUICKSTART.md`.

## Pull Request Expectations

- Prefer issue-first discussion for new features.
- Keep first PRs small.
- Include validation output.
- Update memory or telemetry docs only when the change teaches a reusable lesson.
- Do not include private operational context.

