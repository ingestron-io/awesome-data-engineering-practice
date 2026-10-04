# Source review — 2026-10-05

The library selects 47 resources: official platform documentation, project-owned
GitHub examples and the original local recipe repository. It now has six platform
and practice pages and four short task guides. Summaries and review recommendations
are original; no third-party article or source tree was copied here.

## What was checked

All 47 catalogue destinations returned HTTP 200 on a bounded GET review. An
unavailable OpenLineage index was replaced with its object-model page. DuckDB’s
old stable paths returned redirect stubs; the catalogue now uses current pages.
The Azure architecture overview redirected to database architecture, so its title
and selection note were narrowed to match that destination.

Twelve linked GitHub repositories were inspected through their READMEs and API
metadata. None was archived at review. The retained README blob identifies the
fetched revision. Licence metadata is recorded; four Databricks repositories use
an upstream Databricks licence rather than an assumed MIT/Apache licence.
These are references, not relicensed code.

[Source-review record](source-review-2026-10-05.json) retains destination, date,
status and repository metadata. It stores no article copies, account tokens or
third-party source files. The earlier link-only report remains dated historical evidence.

## What the checks prove

`python3 scripts/check.py` checks fields, attribution, dates, unique HTTPS links,
source-record coverage, local destinations and exact generated-page consistency.
It performs no live network request. `python3 scripts/render.py` rebuilds the
README and six resource pages from `resources.json` and the review metadata.

Upstream samples have not been executed or security-audited by this project.
Local Python/DuckDB examples are qualified in the linked recipe repository.
Native Databricks, Fabric and ADF procedures remain subject to their runtime,
permission and capacity requirements. Source availability can change after review.
