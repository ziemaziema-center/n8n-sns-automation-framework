# Quickstart

## What This Quickstart Proves

This quickstart verifies the public, local-only path for n8n SNS Automation Framework. It does not require real credentials and does not call external services.

## Prerequisites

- Python 3.10+.
- Git.
- A terminal.

## 1. Clone

```bash
git clone https://github.com/ziemaziema-center/n8n-sns-automation-framework.git
cd n8n-sns-automation-framework
```

`agent-hq` is a placeholder until the public organization is created.

## 2. Run Validation

```bash
python validation/validate_repo.py
```

Expected output:

```text
PASS: repo validation passed
```

## 3. Run the Local Demo

```bash
python demo_approval_simulator.py
```

Expected output:

```text
PASS: approval simulator kept publishing stubbed and ignored duplicate approval
```

## Current Maturity

Status: fixture-backed preview.

If this is an applied automation repo, treat the demo as a fixture path. It proves the safety boundary and basic behavior; it is not a production integration.

