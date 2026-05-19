import json
from pathlib import Path

root = Path(__file__).resolve().parent
events = json.loads((root / "examples" / "approval_events.json").read_text(encoding="utf-8"))
seen = set()
results = []
for event in events:
    key = (event["content_id"], event["media_hash"])
    if key in seen:
        results.append({"content_id": event["content_id"], "decision": "duplicate_ignored"})
        continue
    seen.add(key)
    if event["event"] == "approve":
        results.append({"content_id": event["content_id"], "decision": "approved_for_stub_publish", "publisher": "disabled_stub"})
    else:
        results.append({"content_id": event["content_id"], "decision": "rejected"})
out = root / "examples" / "approval_simulation_result.json"
out.write_text(json.dumps(results, indent=2), encoding="utf-8")
assert any(item["decision"] == "duplicate_ignored" for item in results)
assert all(item.get("publisher") != "live" for item in results)
print("PASS: approval simulator kept publishing stubbed and ignored duplicate approval")
