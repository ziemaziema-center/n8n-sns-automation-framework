# Approval Gate

The approval gate is the boundary between generated content and public publishing.

## Rules

- Generated content is never publishable by default.
- Telegram preview messages must include content ID, risk flags, source context, and approval buttons.
- Only an `approve` event from the configured approval channel can unlock rendering or publishing.
- Debug bot messages cannot approve content.
- Rejected content should be archived for learning, not silently deleted.

