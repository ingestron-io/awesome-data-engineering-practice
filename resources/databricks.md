# Databricks

[Library home](../README.md)

Start with a failing data case, then select the platform control. A successful job can still produce the wrong total.

## A useful order

1. Test one retry and one late update with the local recipes.
2. Read MERGE matching rules and decide how to handle repeated keys.
3. Choose whether a quality failure warns, removes rows or stops the load.
4. Review real reader permissions before promoting the bundle.

Try the [original local recipes](https://github.com/ingestron-io/data-engineering-recipes) before adapting them to a workspace.

Jump to: [Practitioner articles](#practitioner-articles) · [Platform and tool references](#platform-and-tool-references)

## Practitioner articles

### [Up your CI/CD game with Databricks Asset Bundles and Automated Testing](https://www.advancinganalytics.co.uk/blog/up-your-ci/cd-game-with-databricks-asset-bundles-and-automated-testing)

Separate valid configuration from a tested workload. Follow the author’s validate, deploy-to-test and run-tests sequence.

**By:** Connor Quinn · Advancing Analytics. **Source:** Consultancy article. **Type:** article.
**Needs:** Databricks workspace, CLI and compute; native tests can cost money.
**Before using it:** Uses the former Asset Bundles name; check current bundle documentation and your runtime.
**Published:** 2024-10-01.
**Reviewed:** 2026-10-05.

### [Avoid Delta Live Table Pipeline Conflicts with Parameterised Databricks Asset Bundles](https://www.advancinganalytics.co.uk/blog/avoid-delta-live-table-conflicts-with-databricks-asset-bundles)

See why two developers can collide on the same target tables. Review a separate user target and schema naming.

**By:** Jordan Witcombe · Advancing Analytics. **Source:** Consultancy article. **Type:** article.
**Needs:** Databricks bundles, a workspace and pipeline compute; cloud costs apply.
**Before using it:** Historical DLT terminology and example settings; verify current pipeline behaviour before adopting them.
**Published:** 2025-01-24.
**Reviewed:** 2026-10-05.

## Platform and tool references

### [Handle duplicate matches before MERGE](https://learn.microsoft.com/en-us/azure/databricks/delta/merge)

Use when a replay or multiple source rows can update the same business key. Compare runtime-specific matching rules.

**By:** Databricks. **Source:** Platform or tool publisher. **Type:** guide.
**Needs:** Databricks and Delta tables.
**Reviewed:** 2026-10-05.

### [Choose a reaction to failed quality checks](https://learn.microsoft.com/en-us/azure/databricks/ldp/expectations)

Compare retain, drop and stop behaviour before deciding what happens to a bad row.

**By:** Databricks. **Source:** Platform or tool publisher. **Type:** guide.
**Needs:** Lakeflow pipeline and supported runtime.
**Reviewed:** 2026-10-05.

### [Apply row filters and column masks](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/filters-and-masks/)

Use for reader-specific access. Check compute limitations and test an actual reader identity.

**By:** Databricks. **Source:** Platform or tool publisher. **Type:** guide.
**Needs:** Unity Catalog, supported compute and policy permissions.
**Reviewed:** 2026-10-05.

### [Review Unity Catalog grants](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/manage-privileges/)

Trace ownership and grants when a user can open a workspace but cannot query a table.

**By:** Databricks. **Source:** Platform or tool publisher. **Type:** guide.
**Needs:** Unity Catalog and authorised identities.
**Reviewed:** 2026-10-05.

### [Version jobs with Declarative Automation Bundles](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/bundles/)

Keep job definitions, code and environment targets together. Older material calls these Asset Bundles.

**By:** Databricks. **Source:** Platform or tool publisher. **Type:** guide.
**Needs:** Databricks CLI; authenticated workspace for validation/deployment.
**Reviewed:** 2026-10-05.

### [Bundle examples](https://github.com/databricks/bundle-examples)

Start from a relevant job example and inspect its resources before deployment.

**By:** Databricks contributors. **Source:** Platform or tool publisher. **Type:** repository.
**Needs:** Databricks workspace; individual examples can provision services.
**Upstream licence:** Databricks licence; inspect upstream LICENSE and service terms before reuse. Linked code keeps its own terms.
[Read the upstream terms](https://github.com/databricks/bundle-examples/blob/main/LICENSE).
**Reviewed:** 2026-10-05.

### [Databricks CLI](https://github.com/databricks/cli)

Use local commands to inspect workspace resources and work with bundles.

**By:** Databricks contributors. **Source:** Platform or tool publisher. **Type:** repository.
**Needs:** Local binary; workspace authentication for remote commands.
**Upstream licence:** Databricks licence; inspect upstream LICENSE and service terms before reuse. Linked code keeps its own terms.
[Read the upstream terms](https://github.com/databricks/cli/blob/main/LICENSE).
**Reviewed:** 2026-10-05.

### [Databricks SDK for Python](https://github.com/databricks/databricks-sdk-py)

Inspect API examples for repeatable inventory and job automation instead of browser clicking.

**By:** Databricks contributors. **Source:** Platform or tool publisher. **Type:** repository.
**Needs:** Python; workspace authentication and API permissions.
**Upstream licence:** Apache-2.0. Linked code keeps its own terms.
**Reviewed:** 2026-10-05.

### [DQX quality rules](https://github.com/databrickslabs/dqx)

Explore rule definitions and good/bad row splits. Labs publishes this without a support SLA.

**By:** Databricks Labs contributors. **Source:** Platform or tool publisher. **Type:** repository.
**Needs:** PySpark; check each example runtime and optional cloud dependencies.
**Upstream licence:** Databricks licence; inspect upstream LICENSE and service terms before reuse. Linked code keeps its own terms.
[Read the upstream terms](https://github.com/databrickslabs/dqx/blob/main/LICENSE).
**Reviewed:** 2026-10-05.

### [Unity Catalog migration assessment](https://github.com/databrickslabs/ucx)

Inspect assessment reports before planning a legacy metastore migration. Review permissions before running.

**By:** Databricks Labs contributors. **Source:** Platform or tool publisher. **Type:** repository.
**Needs:** Authorised Databricks workspace; Labs support limitations.
**Upstream licence:** Databricks licence; inspect upstream LICENSE and service terms before reuse. Linked code keeps its own terms.
[Read the upstream terms](https://github.com/databrickslabs/ucx/blob/main/LICENSE).
**Reviewed:** 2026-10-05.

### [Validate a bundle before deployment](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/bundles/work-tasks)

Separate configuration validation from deployment and workload tests; choose the target explicitly.

**By:** Databricks. **Source:** Platform or tool publisher. **Type:** guide.
**Needs:** Databricks CLI, a bundle project and authorised workspace.
**Reviewed:** 2026-10-05.
