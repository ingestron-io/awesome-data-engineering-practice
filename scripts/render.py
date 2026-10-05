"""Render short task-focused pages from the attributed resource catalogue."""

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {
    "databricks": (
        "Databricks",
        "Start with a failing data case, then select the platform control. A successful job can still produce the wrong total.",
        [
            "Test one retry and one late update with the local recipes.",
            "Read MERGE matching rules and decide how to handle repeated keys.",
            "Choose whether a quality failure warns, removes rows or stops the load.",
            "Review real reader permissions before promoting the bundle.",
        ],
    ),
    "fabric": (
        "Microsoft Fabric",
        "A notebook release includes its workspace bindings. Correct code pointed at the wrong lakehouse is still a failed release.",
        [
            "Trace source → lakehouse → notebook → consumer for one table.",
            "Check how updates and deletes arrive, and what a retry would repeat.",
            "Review notebook source, environment and lakehouse bindings together.",
            "Check supported items before selecting a Git or deployment route.",
        ],
    ),
    "adf": (
        "Azure Data Factory",
        "Treat the cursor as a record of successfully committed data. A timestamp filter alone does not make a retry safe.",
        [
            "Confirm the integration runtime can reach the source.",
            "Choose watermark or change capture based on updates and deletes.",
            "Define a repeatable sink write and a recovery path before advancing the cursor.",
            "Validate and export the factory; review parameters and triggers before deployment.",
        ],
    ),
    "spark": (
        "Spark and Delta",
        "Debug a small input before tuning a large job. Test key counts and totals, then inspect the query plan.",
        [
            "Run the synthetic replay example and identify the business key.",
            "Test nulls, duplicates, late updates and deletes.",
            "Compare plans and measured runtimes for a single tuning change.",
            "Check Spark/Delta compatibility and managed-runtime differences.",
        ],
    ),
    "local": (
        "Local Python, DuckDB and VS Code",
        "Run a file-sized problem on your own computer. These exercises need no database service, container or cloud trial.",
        [
            "Create a Python environment and install the pinned recipe dependencies.",
            "Select that environment in VS Code and in your notebook kernel.",
            "Read CSV fields deliberately; inspect the accepted Parquet output.",
            "Add rejection and schema-change cases before using your own authorised files.",
        ],
    ),
    "practice": (
        "Quality, governance and project work",
        "Write the expected behaviour in examples that someone else can check. Tool selection comes after the problem is clear.",
        [
            "Define the row meaning, key, freshness and owner with the requester.",
            "Agree what should happen to bad rows and missed deadlines.",
            "Test reader access through each supported query path.",
            "Record the decision, release revision and recovery procedure.",
        ],
    ),
}

SOURCES = {
    "project": "Community project",
    "practitioner": "Practitioner article",
    "consultancy": "Consultancy article",
    "vendor": "Platform or tool publisher",
    "original": "Original recipe",
}
GROUPS = (
    ("Practitioner articles", {"practitioner", "consultancy"}),
    ("Community projects and project guides", {"project"}),
    ("Platform and tool references", {"vendor"}),
    ("Original recipes", {"original"}),
)


def load_evidence():
    records = []
    for path in sorted((ROOT / "docs").glob("*-review-*.json")):
        records.extend(json.loads(path.read_text()))
    urls = [record["url"] for record in records]
    if len(urls) != len(set(urls)):
        raise ValueError("Duplicate source-review URL; keep one current record per URL")
    return {record["url"]: record for record in records}


def entry_lines(item, evidence):
    lines = [
        f"### [{item['title']}]({item['url']})",
        "",
        item["why"],
        "",
        f"**By:** {item['author']}. **Source:** {SOURCES[item['sourceType']]}. **Type:** {item['kind']}.",
        f"**Needs:** {item['requires']}.",
    ]
    if item.get("caution"):
        lines += [f"**Before using it:** {item['caution']}"]
    record = evidence[item["url"]]
    if item["kind"] == "repository":
        licence = record.get("licenceNote") or record.get("licence")
        lines += [
            f"**Upstream licence:** {licence.rstrip('.')}. Linked code keeps its own terms."
        ]
    if record.get("licenceUrl"):
        lines += [f"[Read the upstream terms]({record['licenceUrl']})."]
    if item["kind"] == "article":
        lines += [
            f"**Published:** {item.get('publishedAt', 'Date not shown on the article')}."
        ]
    lines += [f"**Reviewed:** {item['reviewedAt']}.", ""]
    return lines


def render(items, evidence):
    documents = {}
    index = [
        "# Awesome data engineering practice",
        "",
        "Useful references for the problems you meet while building and running data pipelines.",
        "Choose a task, run a small example, then check the platform-specific behaviour.",
        "",
        "## Start with a problem",
        "",
        "| You need to… | Start here |",
        "| --- | --- |",
        "| Retry a load without duplicate totals | [Safe incremental loads](guides/safe-incremental-loads.md) |",
        "| Review a notebook or pipeline release | [Review a data release](guides/review-a-data-release.md) |",
        "| Check who can see sensitive values | [Test reader access](guides/test-reader-access.md) |",
        "| Turn a request into a checkable delivery | [Scope a data project](guides/scope-a-data-project.md) |",
        "| Run SQL and file checks in VS Code | [Local development](resources/local.md) |",
        "",
        "## Learn from the community",
        "",
        "[Browse community projects and field notes](community.md) for worked examples, debugging stories and engineering trade-offs.",
        "Start with Spark assertion failures, ADF testing, Fabric releases or shared Databricks development.",
        "Author experience, consultancy advice and project documentation are labelled on every entry.",
        "",
        "## Browse by platform",
        "",
        "| Platform or practice | Resources |",
        "| --- | --- |",
    ]
    for key, (title, intro, steps) in CATEGORIES.items():
        group = [item for item in items if item["category"] == key]
        index.append(f"| [{title}](resources/{key}.md) | {len(group)} |")
        lines = [
            f"# {title}",
            "",
            "[Library home](../README.md)",
            "",
            intro,
            "",
            "## A useful order",
            "",
        ]
        lines.extend(f"{number}. {step}" for number, step in enumerate(steps, 1))
        lines += [
            "",
            "Try the [original local recipes](https://github.com/ingestron-io/data-engineering-recipes) before adapting them to a workspace.",
            "",
        ]
        available = [
            (title, sources)
            for title, sources in GROUPS
            if any(item["sourceType"] in sources for item in group)
        ]
        lines += [
            "Jump to: "
            + " · ".join(
                f"[{title}](#{title.lower().replace(' ', '-')})"
                for title, _ in available
            ),
            "",
        ]
        for heading, sources in available:
            lines += [f"## {heading}", ""]
            for item in group:
                if item["sourceType"] in sources:
                    lines += entry_lines(item, evidence)
        documents[f"resources/{key}.md"] = "\n".join(lines).rstrip() + "\n"
    index += [
        "",
        f"{len(items)} attributed resources. Cloud references can require paid capacity or compute; the local recipes run on your computer.",
        "",
        "## How this list stays useful",
        "",
        "Each entry explains when it helps, who maintains it and what it needs.",
        "These are original selection notes, not copied articles or endorsements.",
        "Community sources include practitioner sites, consultancy blogs and project-maintained references; projects can have commercial backing.",
        "Dated experience is useful context. Check current platform documentation before treating it as present-day behaviour.",
        "GitHub projects are checked for repository status and licence metadata.",
        "An accessible link does not prove its sample has been executed.",
        "",
        "[Review evidence](docs/verification.md) · [Suggest a resource](CONTRIBUTING.md) · [Report a security issue](SECURITY.md)",
        "",
        "The original list is CC0. Linked articles and code retain their authors’ licences and service terms.",
        "",
    ]
    documents["README.md"] = "\n".join(index)
    community = [
        "# Community projects and field notes",
        "",
        "[Library home](README.md)",
        "",
        "Learn from people who explain a failure, show their code or describe a trade-off.",
        "This page brings together practitioner articles, consultancy walkthroughs and community projects.",
        "Some projects have commercial backing. Source labels describe who publishes the material, not financial independence.",
        "",
        "Each platform page includes prerequisites, publication/review dates and reuse notes.",
        "Article experience is attributed to its author; upstream samples have not been run by this library.",
        "",
    ]
    for key, (title, _, _) in CATEGORIES.items():
        selected = [
            item
            for item in items
            if item["category"] == key
            and item["sourceType"] in {"project", "practitioner", "consultancy"}
        ]
        if not selected:
            continue
        community += [
            f"## {title}",
            "",
            f"[Read the prerequisites and review notes](resources/{key}.md).",
            "",
        ]
        for item in selected:
            community += [
                f"- [{item['title']}]({item['url']}) — {item['why']} By {item['author']}."
            ]
        community += [""]
    community += ["[Suggest another worked example](CONTRIBUTING.md).", ""]
    documents["community.md"] = "\n".join(community)
    return documents


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="Fail if a generated page is stale"
    )
    args = parser.parse_args()
    items = json.loads((ROOT / "resources.json").read_text())
    evidence = load_evidence()
    for path, text in render(items, evidence).items():
        target = ROOT / path
        if args.check:
            if not target.exists() or target.read_text() != text:
                raise SystemExit(f"Stale {path}; run python3 scripts/render.py")
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text)


if __name__ == "__main__":
    main()
