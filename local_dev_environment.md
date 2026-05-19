# Local Development Environment

## Requirements

- Git.
- Python 3.10+ for validation scripts.
- A Markdown editor.
- Optional: a Mermaid renderer for diagrams.

## Local Setup

```bash
git clone https://github.com/ziemaziema-center/n8n-sns-automation-framework.git
cd n8n-sns-automation-framework
python validation/validate_repo.py
```

## Configuration

Use `.env.example` as a shape reference only. Keep real `.env` files local and untracked.

## Expected Output

A healthy local check prints `PASS: repo validation passed`.

