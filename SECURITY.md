# Security Policy

## Supported Model

This repository is designed for public, sanitized use. Examples must run in dry-run, offline, preview, read-only, or stub mode unless a maintainer explicitly documents otherwise.

## Never Commit

- API keys, bot tokens, OAuth refresh tokens, PEM files, private webhook URLs, browser cookies, or `.env` files.
- n8n credential exports or execution exports containing private values.
- Live trading keys or live order execution payloads.
- Private Telegram chat IDs, Instagram tokens, Travelpayouts markers, OpenRouter keys, Anthropic keys, Upbit keys, or service account JSON.

## Reporting a Vulnerability

Open a private security advisory if available, or contact the maintainer privately. Do not post exploit details, secrets, or live endpoint values in public issues.

## Public Demo Boundary

Public demos should use fake data, fixtures, screenshots with redactions, or stub services. Any live integration should be opt-in and documented separately from the public default path.

