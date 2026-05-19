# Known Limitations

        n8n SNS Automation Framework is intentionally conservative. Public trust matters more than pretending the project is a complete hosted product.

        ## Current Limits

        - The public repo does not include real platform credentials or live workflow exports.
- FFmpeg examples are fixture-oriented and not a full rendering product.
- Platform policy checks still require human review.

        ## Architecture Tradeoffs

        - Fixture-first onboarding is safer than live demos, but less visually exciting.
        - Markdown-first structure works across agent tools, but does not enforce behavior unless teams run validation.
        - Approval gates slow down automation, but they make publishing, messaging, and finance workflows reviewable.

        ## Known Issues

        - Raw n8n exports often contain credential references and must be sanitized before publication.
- Telegram callback payloads should be treated as untrusted until verified.

        ## Future Work

        - Import-safe demo workflow with all publisher nodes disabled.
- Fixture-based callback simulator.
- Caption/media duplicate hash validator.

