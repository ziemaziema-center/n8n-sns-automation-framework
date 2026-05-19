from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "ARCHITECTURE.md",
    "QUICKSTART.md",
    "SECURITY.md",
    "ROADMAP.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "LICENSE.md",
    ".env.example",
    "diagrams/pipeline.md",
]
SECRET_PATTERNS = [
    re.compile(r"sk-(?!or-REPLACE_ME)[A-Za-z0-9_\-]{16,}"),
    re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
    re.compile(r"xox[baprs]-[A-Za-z0-9\-]{16,}"),
    re.compile(r"-----BEGIN [A-Z ]+PRIVATE KEY-----"),
    re.compile(r"(?i)(authorization:\s*bearer\s+)(?!REPLACE_ME)[A-Za-z0-9._\-]{16,}"),
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


for rel in REQUIRED:
    path = ROOT / rel
    if not path.exists():
        fail(f"missing {rel}")
    if path.suffix == ".md" and len(path.read_text(encoding="utf-8", errors="ignore")) < 300:
        fail(f"{rel} needs more detail")

for folder in ["docs", "examples", "diagrams", "validation"]:
    if not (ROOT / folder).exists():
        fail(f"missing {folder}/")

for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    if path.name == ".env" or path.suffix.lower() in {".pem", ".key", ".log"}:
        fail(f"forbidden public artifact: {path.relative_to(ROOT)}")
    text = path.read_text(encoding="utf-8", errors="ignore")
    if ("github.com/" + "agent-hq/") in text:
        fail(f"stale clone URL in {path.relative_to(ROOT)}")
    if ("C:\\" + "Users") in text or ("43.201" + ".227.194") in text:
        fail(f"local/private reference in {path.relative_to(ROOT)}")
    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            fail(f"secret-like value in {path.relative_to(ROOT)}")

joined = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in ROOT.rglob("*.md") if ".git" not in p.parts)
for phrase in ["approval", "safety", "Telegram", "workflow"]:
    if phrase not in joined:
        fail(f"missing expected term: {phrase}")
if "```mermaid" not in joined:
    fail("missing Mermaid diagram")

print("PASS: repo validation passed")
