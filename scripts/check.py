import json
from pathlib import Path
from urllib.parse import urlparse
root=Path(__file__).resolve().parents[1]
items=json.loads((root/"resources.json").read_text())
assert len(items)>=12
seen=set()
for item in items:
    assert set(item)=={"category","title","author","url","why"}
    assert all(isinstance(v,str) and v.strip() for v in item.values())
    url=urlparse(item["url"]);assert url.scheme=="https" and url.hostname and not url.username
    assert item["url"] not in seen;seen.add(item["url"])
    assert f']({item["url"]})' in (root/"README.md").read_text()
print(f"Checked {len(items)} unique attributed resources; this is a structural check, not a live link check.")
