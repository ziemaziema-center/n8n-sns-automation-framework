# Validation

Required checks: duplicate IDs are rejected, unapproved payloads cannot publish, debug bot destination differs from approval bot destination, and render jobs reference local fixture files only.

## Repo-specific Demo Validation

Run:

```bash
python demo_approval_simulator.py
```

This is the repo-specific fixture path. It is intentionally local-only.

