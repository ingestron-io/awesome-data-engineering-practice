# Azure Data Factory

[Library home](../README.md)

Treat the cursor as a record of successfully committed data. A timestamp filter alone does not make a retry safe.

## A useful order

1. Confirm the integration runtime can reach the source.
2. Choose watermark or change capture based on updates and deletes.
3. Define a repeatable sink write and a recovery path before advancing the cursor.
4. Validate and export the factory; review parameters and triggers before deployment.

Try the [original local recipes](https://github.com/ingestron-io/data-engineering-recipes) before adapting them to a workspace.

Jump to: [Practitioner articles](#practitioner-articles) · [Community projects and project guides](#community-projects-and-project-guides) · [Platform and tool references](#platform-and-tool-references)

## Practitioner articles

### [Testing Azure Data Factory in your CI/CD pipeline](https://richardswinbank.net/adf/testing_azure_data_factory_in_your_cicd_pipeline)

Connect pipeline changes to functional tests. The article explains deployment, test-project build and isolated test configuration.

**By:** Richard Swinbank. **Source:** Practitioner article. **Type:** article.
**Needs:** ADF, Azure DevOps, .NET/NUnit and Azure SQL test fixtures; cloud costs apply.
**Before using it:** Older SDK, identity and runner examples. Use current authentication guidance; publication date is not shown on the article.
**Published:** Date not shown on the article.
**Reviewed:** 2026-10-05.

## Community projects and project guides

### [azure.datafactory.tools](https://github.com/Azure-Player/azure.datafactory.tools)

Review factory dependencies, environment substitutions and trigger handling when deploying ADF JSON from Git.

**By:** Kamil Nowinski and contributors. **Source:** Community project. **Type:** repository.
**Needs:** PowerShell; Azure identity and ADF for deployment; cloud activity can cost money.
**Before using it:** Inspect deletion, factory-creation and trigger options before running a deployment.
**Upstream licence:** MIT. Linked code keeps its own terms.
**Reviewed:** 2026-10-05.

### [ADF testing series — companion code](https://github.com/richardswinbank/community)

Pair the ADF testing articles with pipeline JSON, NUnit tests and release YAML in the adf-testing-series folder.

**By:** Richard Swinbank. **Source:** Community project. **Type:** repository.
**Needs:** Historical .NET/Visual Studio examples; ADF and Azure SQL for integration tests; cloud costs apply.
**Before using it:** Reference only: no repository licence was found. Obtain permission before copying or adapting code.
**Upstream licence:** No licence found in the inspected repository tree; reference only. Obtain permission before copying or adapting. Linked code keeps its own terms.
[Read the upstream terms](https://github.com/richardswinbank/community/blob/main/README.md).
**Reviewed:** 2026-10-05.

## Platform and tool references

### [Choose an incremental-copy approach](https://learn.microsoft.com/en-us/azure/data-factory/tutorial-incremental-copy-overview)

Compare watermark and change-tracking routes before choosing how to recognise changes.

**By:** Microsoft. **Source:** Platform or tool publisher. **Type:** guide.
**Needs:** Azure Data Factory and supported source; cloud execution.
**Reviewed:** 2026-10-05.

### [Build a watermark load](https://learn.microsoft.com/en-us/azure/data-factory/tutorial-incremental-copy-portal)

Inspect lookup, bounded copy and cursor update steps. Define retry behaviour before advancing the cursor.

**By:** Microsoft. **Source:** Platform or tool publisher. **Type:** guide.
**Needs:** ADF, Azure SQL and storage in the tutorial.
**Reviewed:** 2026-10-05.

### [Reach a private source with an integration runtime](https://learn.microsoft.com/en-us/azure/data-factory/create-self-hosted-integration-runtime)

Check network reachability and host requirements before selecting a private-source copy route.

**By:** Microsoft. **Source:** Platform or tool publisher. **Type:** guide.
**Needs:** ADF and an authorised Windows runtime host; reference only.
**Reviewed:** 2026-10-05.

### [Automate validation and template export](https://learn.microsoft.com/en-us/azure/data-factory/continuous-integration-delivery-improvements)

Use the utilities package for build validation and export. Deployment is a separate step.

**By:** Microsoft. **Source:** Platform or tool publisher. **Type:** guide.
**Needs:** Node.js, factory source and Azure configuration.
**Reviewed:** 2026-10-05.

### [Release an ADF change](https://learn.microsoft.com/en-us/azure/data-factory/continuous-integration-delivery)

Plan environment parameters and trigger handling when promoting a factory change.

**By:** Microsoft. **Source:** Platform or tool publisher. **Type:** guide.
**Needs:** Azure deployment access; environment-specific configuration.
**Reviewed:** 2026-10-05.

### [Measure copy performance](https://learn.microsoft.com/en-us/azure/data-factory/copy-activity-performance)

Use copy metrics to locate a bottleneck before increasing parallelism.

**By:** Microsoft. **Source:** Platform or tool publisher. **Type:** guide.
**Needs:** An existing ADF copy run and monitoring access.
**Reviewed:** 2026-10-05.
