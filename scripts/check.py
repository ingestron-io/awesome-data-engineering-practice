"""Check attribution, review evidence, generated pages and local navigation."""

from datetime import date
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlparse

from render import load_evidence, SOURCES

ROOT = Path(__file__).resolve().parents[1]
items = json.loads((ROOT / "resources.json").read_text())
evidence = load_evidence()
assert len(items) >= 12
seen = set()
for item in items:
    required = {
        "category",
        "title",
        "author",
        "url",
        "why",
        "requires",
        "kind",
        "reviewedAt",
        "sourceType",
    }
    assert required <= set(item) <= required | {"caution", "publishedAt"}
    assert all(isinstance(value, str) and value.strip() for value in item.values())
    date.fromisoformat(item["reviewedAt"])
    assert item["category"] in (
        "databricks",
        "fabric",
        "adf",
        "spark",
        "local",
        "practice",
    )
    assert item["kind"] in ("guide", "repository", "article")
    assert item["sourceType"] in SOURCES
    if item["kind"] == "article":
        assert item["sourceType"] in ("practitioner", "consultancy")
        assert item.get("caution"), "Articles need an experience/version boundary"
    if item.get("publishedAt"):
        assert item["kind"] == "article"
        assert date.fromisoformat(item["publishedAt"]) <= date.fromisoformat(
            item["reviewedAt"]
        )
    url = urlparse(item["url"])
    assert (
        url.scheme == "https" and url.hostname and not url.username and not url.password
    )
    assert item["url"] not in seen, f"Duplicate {item['url']}"
    seen.add(item["url"])
    assert (
        f"]({item['url']})"
        in (ROOT / "resources" / f"{item['category']}.md").read_text()
    )
    record = evidence[item["url"]]
    assert record["status"] == 200 and "error" not in record, item["url"]
    assert record["checkedAt"] == item["reviewedAt"]
    if item["sourceType"] in ("project", "practitioner", "consultancy"):
        assert f"]({item['url']})" in (ROOT / "community.md").read_text()
    if item["kind"] == "article":
        assert record.get("publishedAt") == item.get("publishedAt")
        assert record["sourceType"] == item["sourceType"]
    if item["kind"] == "repository":
        assert record["archived"] is False
        assert re.fullmatch("[a-f0-9]{40}", record["readmeBlob"])
        assert record.get("licence") not in (None, "NOASSERTION") or record.get(
            "licenceNote"
        )
subprocess.run([sys.executable, str(ROOT / "scripts/render.py"), "--check"], check=True)
for page in ROOT.rglob("*.md"):
    if ".git" in page.parts:
        continue
    text = re.sub(r"```.*?```", "", page.read_text(), flags=re.S)
    assert len(re.findall(r"^# ", text, re.M)) == 1, f"{page}: expected one title"
    for destination in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        url = urlparse(destination)
        if url.scheme or not url.path:
            continue
        target = (page.parent / unquote(url.path)).resolve()
        assert target.is_relative_to(ROOT) and target.exists(), (
            f"{page}: missing {destination}"
        )
print(
    f"Checked {len(items)} attributed resources, dated evidence and generated navigation. No live fetch or upstream execution is implied."
)
