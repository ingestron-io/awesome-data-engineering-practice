# Microsoft Fabric

[Library home](../README.md)

A notebook release includes its workspace bindings. Correct code pointed at the wrong lakehouse is still a failed release.

## A useful order

1. Trace source → lakehouse → notebook → consumer for one table.
2. Check how updates and deletes arrive, and what a retry would repeat.
3. Review notebook source, environment and lakehouse bindings together.
4. Check supported items before selecting a Git or deployment route.

Try the [original local recipes](https://github.com/ingestron-io/data-engineering-recipes) before adapting them to a workspace.

## Selected references

### [Understand lakehouse ingestion and transformation](https://learn.microsoft.com/en-us/fabric/data-engineering/tutorial-lakehouse-introduction)

Follow the end-to-end data flow, then inspect where incremental updates enter it.

**By:** Microsoft. **Type:** guide. **Needs:** Fabric workspace and capacity; cloud tutorial.
**Reviewed:** 2026-10-05.

### [Load files and tables from a notebook](https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-notebook-load-data)

Check Files versus Tables and relative versus ABFS paths before moving a notebook.

**By:** Microsoft. **Type:** guide. **Needs:** Fabric notebook and lakehouse.
**Reviewed:** 2026-10-05.

### [Review notebook code and bindings in Git](https://learn.microsoft.com/en-us/fabric/data-engineering/notebook-source-control-deployment)

Check notebook source and target lakehouse/environment bindings during a release.

**By:** Microsoft. **Type:** guide. **Needs:** Fabric workspace, Git integration and item ownership.
**Reviewed:** 2026-10-05.

### [Check supported items in Git integration](https://learn.microsoft.com/en-us/fabric/cicd/git-integration/intro-to-git-integration)

Check supported items and provider limitations before designing branch-based development.

**By:** Microsoft. **Type:** guide. **Needs:** Fabric tenant settings, supported capacity and Git provider.
**Reviewed:** 2026-10-05.

### [Promote changes with deployment pipelines](https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines)

Compare stages and dependencies; a deployment does not prove the data is correct.

**By:** Microsoft. **Type:** guide. **Needs:** Fabric deployment permissions and supported items/capacity.
**Reviewed:** 2026-10-05.

### [Fabric CI/CD Python library](https://github.com/microsoft/fabric-cicd)

Explore code-first publishing, parameters and workspace examples. Check item support before choosing it.

**By:** Microsoft contributors. **Type:** repository. **Needs:** Python, Fabric authentication and deployment permissions.
**Upstream licence:** MIT. Linked code keeps its own terms.
**Reviewed:** 2026-10-05.

### [Fabric CLI](https://github.com/microsoft/fabric-cli)

Start with workspace listing and item inspection before using import or deployment commands.

**By:** Microsoft contributors. **Type:** repository. **Needs:** Local Python; Fabric account for remote operations.
**Upstream licence:** MIT. Linked code keeps its own terms.
**Reviewed:** 2026-10-05.

### [Fabric samples](https://github.com/microsoft/fabric-samples)

Find notebooks and scenario samples; read prerequisites for the specific folder you choose.

**By:** Microsoft contributors. **Type:** repository. **Needs:** Varies by sample; many need Fabric capacity.
**Upstream licence:** MIT. Linked code keeps its own terms.
**Reviewed:** 2026-10-05.

### [Fabric toolbox](https://github.com/microsoft/fabric-toolbox)

Inspect operational scripts for your task. Review each tool and its permissions before use.

**By:** Microsoft contributors. **Type:** repository. **Needs:** Varies by utility; usually an authorised Fabric tenant.
**Upstream licence:** MIT. Linked code keeps its own terms.
**Reviewed:** 2026-10-05.

### [Semantic Link Labs](https://github.com/microsoft/semantic-link-labs)

Explore semantic-model and workspace inspection from Fabric notebooks.

**By:** Microsoft contributors. **Type:** repository. **Needs:** Fabric notebook; semantic-link dependencies and permissions.
**Upstream licence:** MIT. Linked code keeps its own terms.
**Reviewed:** 2026-10-05.

### [Choose watermark or change capture in Copy job](https://learn.microsoft.com/en-us/fabric/data-factory/incremental-copy-job)

Check whether your load needs deletions and what resetting an append load means for duplicates.

**By:** Microsoft. **Type:** guide. **Needs:** Supported source and Fabric Copy job.
**Reviewed:** 2026-10-05.

### [Separate workspace, item and data permissions](https://learn.microsoft.com/en-us/fabric/security/security-overview)

Start an access review by listing the paths a reader can use, including direct data access.

**By:** Microsoft. **Type:** guide. **Needs:** Fabric tenant; test with distinct authorised identities.
**Reviewed:** 2026-10-05.
