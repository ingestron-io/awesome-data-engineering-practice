# Source review — 2026-10-05

The library selects 66 resources. This includes 19 additions from practitioner
sites, consultancy blogs and community repositories: nine articles and ten
projects. A community index links 30 project/practitioner/consultancy references,
including 11 already selected project guides. Six platform and practice pages
put community material before platform references. Four short task guides remain.
Summaries and review recommendations are original; no third-party article or
source tree was copied here.

## What was checked

The earlier 47 catalogue destinations returned HTTP 200 on a bounded GET review. An
unavailable OpenLineage index was replaced with its object-model page. DuckDB’s
old stable paths returned redirect stubs; the catalogue now uses current pages.
The Azure architecture overview redirected to database architecture, so its title
and selection note were narrowed to match that destination.

Twelve linked GitHub repositories were inspected through their READMEs and API
metadata. None was archived at review. The retained README blob identifies the
fetched revision. Licence metadata is recorded; four Databricks repositories use
an upstream Databricks licence rather than an assumed MIT/Apache licence.
These are references, not relicensed code.

The 19 community additions also returned HTTP 200 on a bounded GET. All nine
article bodies and ten project READMEs were inspected. The ten added repositories
were not archived. Review metadata retains each README blob and licence result.
Hypothesis has a file-specific MPL declaration despite unclassified API metadata;
Kevin Chant's README declares MIT but the API reports no licence. Richard
Swinbank's repository has no licence in its inspected tree and is reference only.
Seven article publication dates were visible; two were unstated and remain so.
Article notes distinguish author experience, dated terminology and current
platform facts. Commercial backing is not excluded or inferred from a hostname.

[Source-review record](source-review-2026-10-05.json) retains destination, date,
status and repository metadata. It stores no article copies, account tokens or
third-party source files. The earlier link-only report remains dated historical evidence.
[Community-review record](community-review-2026-10-05.json) retains the additional
19 destinations and the article dates/source labels. Missing reuse terms and
deployment deletion behaviour are stated beside the relevant entries.

## What the checks prove

`python3 scripts/check.py` checks fields, attribution, dates, unique HTTPS links,
source-record coverage, community-index coverage, local destinations and exact
generated-page consistency. It rejects duplicate review URLs and future article
dates. Article entries require an experience/version note.
It performs no live network request. `python3 scripts/render.py` rebuilds the
README, community index and six resource pages from `resources.json` and the
review metadata.

Upstream samples have not been executed or security-audited by this project.
Local Python/DuckDB examples are qualified in the linked recipe repository.
Native Databricks, Fabric and ADF procedures remain subject to their runtime,
permission and capacity requirements. Source availability can change after review.
