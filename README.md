# Awesome data engineering practice

Useful references for a specific job, with one sentence explaining why to open
each one. Start with your problem, then choose a resource. This is a selective
list; linked projects are not endorsements or claims that we ran them.

## Retries And Incremental Loading

- [Incremental copy with ADF](https://learn.microsoft.com/en-us/azure/data-factory/tutorial-incremental-copy-overview) — Microsoft. Compare watermark and change-tracking routes before choosing a cursor.
- [Delta MERGE](https://docs.databricks.com/aws/en/delta/merge) — Databricks. Read duplicate-match and runtime rules before designing an upsert.
- [Structured Streaming programming guide](https://spark.apache.org/docs/latest/streaming/apis-on-dataframes-and-datasets.html) — Apache Spark. Understand state, checkpoints and delivery semantics before claiming safe replay.

## Spark

- [SQL reference](https://spark.apache.org/docs/latest/sql-ref.html) — Apache Spark. Check null, join and expression behaviour against the engine reference.
- [Performance tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html) — Apache Spark. Use plans and runtime evidence to choose a tuning change.

## Quality

- [Lakeflow expectations](https://docs.databricks.com/aws/en/ldp/expectations) — Databricks. Compare warning, drop and failure behaviour for quality rules.

## Governance

- [Row filters and column masks](https://docs.databricks.com/aws/en/data-governance/unity-catalog/filters-and-masks/) — Databricks. Check privileges and limitations; test with the actual reader identity.
- [Fabric security overview](https://learn.microsoft.com/en-us/fabric/security/security-overview) — Microsoft. Separate workspace, item and data permissions before granting access.
- [Unity Catalog access control](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/) — Databricks. Understand ownership and grants instead of assuming workspace membership is sufficient.

## Delivery

- [ADF CI/CD](https://learn.microsoft.com/en-us/azure/data-factory/continuous-integration-delivery) — Microsoft. Plan Git authoring, environment configuration and release steps.
- [Fabric deployment pipelines](https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines) — Microsoft. Review supported items and stage behaviour before designing release automation.
- [Databricks bundles](https://docs.databricks.com/aws/en/dev-tools/bundles/) — Databricks. Keep job configuration and deployment targets under version control.

## Architecture

- [Azure data platform architecture](https://learn.microsoft.com/en-us/azure/architecture/data-guide/) — Microsoft. Compare architecture choices against a defined workload rather than a tool list.

## Project

- [Architecture decision records](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record) — Microsoft. Capture the decision, alternatives and consequences for the next maintainer.

## Examples

- [Fabric samples](https://github.com/microsoft/fabric-samples) — Microsoft contributors. Find platform examples; inspect each sample's prerequisites and licence.
- [Fabric toolbox](https://github.com/microsoft/fabric-toolbox) — Microsoft contributors. Find operational utilities and review each tool before using it.
- [Original engineering recipes](https://github.com/ingestron-io/data-engineering-recipes) — Pipeline Practice. Run small synthetic examples for replay, joins, quarantine and release review.


## Suggest a resource

Explain the task it solves, credit its author and use the canonical link.
Prefer official references and inspect prerequisites, cost and licence. Remove
links that stop being useful. The original list is CC0; linked works keep their
own licences. [Contribution guide](CONTRIBUTING.md).
