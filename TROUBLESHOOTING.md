# Troubleshooting

## First Checks

- Confirm you are using the public fixture path, not private production files.
- Confirm `.env.example` still contains placeholders only.
- Run `python validation/validate_repo.py` from the repository root.
- Read `KNOWN_LIMITATIONS.md` before opening an issue.

## Common Mistakes

- Treating examples as production-ready integrations.
- Adding private credentials to public examples.
- Skipping validation because the change is "docs only".
- Confusing planned screenshots or demos with completed assets.

## Repo-specific Guidance

Best for teams separating content generation, preview, approval, rendering, and publishing.

Expected safe output: A safe demo should generate a fixture preview, block publish until approval, and record rejected items.

## When to Open an Issue

Open an issue when a fixture path is unclear, validation output is ambiguous, or the public/private boundary is hard to understand. Do not paste secrets, private URLs, raw logs, or credential-bearing exports into issues.

