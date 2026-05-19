# n8n SNS Automation Framework

A sanitized n8n framework for approval-first social automation.

## What This Project Is

This repo documents a safe reference architecture for generating, previewing, approving, rendering, and publishing social content through n8n-style workflows.

## Why It Exists

Social automation is risky when generation and publishing are coupled. The framework separates preview, approval, debug telemetry, rendering, and publish control.

## Who It Helps

Creators, small teams, automation engineers, and agencies who need repeatable SNS pipelines without accidental posts or credential leakage.

## Problem It Solves

It solves the gap between experimental AI content generation and controlled production publishing by making approval the default boundary.

## Core Architecture

The framework uses a generator workflow, Telegram preview/approval workflow, FFmpeg rendering stage, debug bot separation, publisher workflow, dedupe guard, and rollback playbook.

See [`ARCHITECTURE.md`](ARCHITECTURE.md) and [`diagrams/pipeline.md`](diagrams/pipeline.md) for the full system view.

## Safety Model

Approval-first publishing, debug bot separation, duplicate suppression, rollback docs, and fake `.env.example` values. No real n8n credentials or private workflow exports are included.

## Install and Setup

```bash
git clone https://github.com/ziemaziema-center/n8n-sns-automation-framework.git
cd n8n-sns-automation-framework
cp .env.example .env
```

Then keep fake values until you have reviewed [`SECURITY.md`](SECURITY.md) and the relevant quickstart.

## Example Usage

Use `examples/sanitized_workflow_placeholder.json` as the shape of a workflow export, then connect local stubs before using any real bot or social account.

## Production Ready vs Experimental

Production-ready:

- Documentation structure, safety model, and validation-first workflow.
- Sanitized examples and fixtures that are safe to publish.
- Issue and pull request templates for public collaboration.

Experimental:

- Any live connector, publisher, trading, or messaging integration.
- Any automation that depends on private credentials, private endpoints, or account-specific business rules.

## Screenshots and Diagrams

- Add screenshots under `docs/screenshots/` after public redaction.
- Start with the Mermaid diagrams in `diagrams/`.

## Roadmap

The first milestone is a fully reproducible local demo. Later milestones add optional integrations, richer fixtures, and community-maintained adapters.

## Contributing

Read [`CONTRIBUTING.md`](CONTRIBUTING.md), open an issue before large changes, and include validation evidence in every pull request.

## Disclaimer

Social automation can violate platform rules or create reputational risk. This public version is approval-first and uses fake credentials only.

