# Azure Data Factory

[Library home](../README.md)

Treat the cursor as a record of successfully committed data. A timestamp filter alone does not make a retry safe.

## A useful order

1. Confirm the integration runtime can reach the source.
2. Choose watermark or change capture based on updates and deletes.
3. Define a repeatable sink write and a recovery path before advancing the cursor.
4. Validate and export the factory; review parameters and triggers before deployment.

Try the [original local recipes](https://github.com/ingestron-io/data-engineering-recipes) before adapting them to a workspace.

## Selected references

### [Choose an incremental-copy approach](https://learn.microsoft.com/en-us/azure/data-factory/tutorial-incremental-copy-overview)

Compare watermark and change-tracking routes before choosing how to recognise changes.

**By:** Microsoft. **Type:** guide. **Needs:** Azure Data Factory and supported source; cloud execution.
**Reviewed:** 2026-10-05.

### [Build a watermark load](https://learn.microsoft.com/en-us/azure/data-factory/tutorial-incremental-copy-portal)

Inspect lookup, bounded copy and cursor update steps. Define retry behaviour before advancing the cursor.

**By:** Microsoft. **Type:** guide. **Needs:** ADF, Azure SQL and storage in the tutorial.
**Reviewed:** 2026-10-05.

### [Reach a private source with an integration runtime](https://learn.microsoft.com/en-us/azure/data-factory/create-self-hosted-integration-runtime)

Check network reachability and host requirements before selecting a private-source copy route.

**By:** Microsoft. **Type:** guide. **Needs:** ADF and an authorised Windows runtime host; reference only.
**Reviewed:** 2026-10-05.

### [Automate validation and template export](https://learn.microsoft.com/en-us/azure/data-factory/continuous-integration-delivery-improvements)

Use the utilities package for build validation and export. Deployment is a separate step.

**By:** Microsoft. **Type:** guide. **Needs:** Node.js, factory source and Azure configuration.
**Reviewed:** 2026-10-05.

### [Release an ADF change](https://learn.microsoft.com/en-us/azure/data-factory/continuous-integration-delivery)

Plan environment parameters and trigger handling when promoting a factory change.

**By:** Microsoft. **Type:** guide. **Needs:** Azure deployment access; environment-specific configuration.
**Reviewed:** 2026-10-05.

### [Measure copy performance](https://learn.microsoft.com/en-us/azure/data-factory/copy-activity-performance)

Use copy metrics to locate a bottleneck before increasing parallelism.

**By:** Microsoft. **Type:** guide. **Needs:** An existing ADF copy run and monitoring access.
**Reviewed:** 2026-10-05.
