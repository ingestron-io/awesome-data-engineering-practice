# Microsoft Fabric

[Library home](../README.md)

A notebook release includes its workspace bindings. Correct code pointed at the wrong lakehouse is still a failed release.

## A useful order

1. Trace source → lakehouse → notebook → consumer for one table.
2. Check how updates and deletes arrive, and what a retry would repeat.
3. Review notebook source, environment and lakehouse bindings together.
4. Check supported items before selecting a Git or deployment route.

Try the [original local recipes](https://github.com/ingestron-io/data-engineering-recipes) before adapting them to a workspace.

Jump to: [Practitioner articles](#practitioner-articles) · [Community projects and project guides](#community-projects-and-project-guides) · [Platform and tool references](#platform-and-tool-references)

## Practitioner articles

### [Data engineering with Microsoft Fabric (incremental batch load)](https://www.ibradshaw.info/blog/41/)

Walk through moving an incremental file load from Databricks to Fabric, including notebook parameters and file paths.

**By:** Ian Bradshaw. **Source:** Practitioner article. **Type:** article.
**Needs:** Fabric workspace, capacity, lakehouse and notebooks; cloud costs apply.
**Before using it:** A dated migration walkthrough, not a current feature comparison. Check today’s utilities and retry behaviour.
**Published:** 2024-02-12.
**Reviewed:** 2026-10-05.

### [Unreliable logging in data factory pipelines](https://richardswinbank.net/fabric/unreliable_logging_in_data_factory_pipelines)

Investigate a timestamp that differs between an activity log and the stored result. Compare the actual write when debugging.

**By:** Richard Swinbank. **Source:** Practitioner article. **Type:** article.
**Needs:** Fabric, ADF or Synapse and a SQL target to reproduce; cloud costs apply.
**Before using it:** The author’s observed behaviour; reproduce on your platform before treating it as a current defect.
**Published:** 2025-03-03.
**Reviewed:** 2026-10-05.

### [Operationalize fabric-cicd to work with Microsoft Fabric and GitHub Actions](https://www.kevinrchant.com/2025/04/11/operationalize-fabric-cicd-to-work-with-microsoft-fabric-and-github-actions/)

Follow a worked release across test and production workspaces. Review how variables and parameters change by target.

**By:** Kevin Chant. **Source:** Practitioner article. **Type:** article.
**Needs:** Fabric capacity, GitHub Actions, Python and an authorised Entra identity; cloud costs apply.
**Before using it:** The sample can unpublish orphan items and omits approval setup. Review deletion, authentication and supported items first.
**Published:** 2025-04-11.
**Reviewed:** 2026-10-05.

## Community projects and project guides

### [Fabric CI/CD with GitHub Actions — companion sample](https://github.com/kevchant/GitHub-fabric-cicd-sample)

Inspect a practitioner workflow with separate workspace values and a reusable Python deployment script.

**By:** Kevin Chant. **Source:** Community project. **Type:** repository.
**Needs:** GitHub Actions, Python, Fabric capacity and an authorised Entra identity; cloud costs apply.
**Before using it:** Review orphan-item deletion and add protected approvals before production use. Included Fabric samples originate from Microsoft.
**Upstream licence:** README declares MIT; GitHub licence metadata is absent. Included Microsoft samples retain their upstream terms. Linked code keeps its own terms.
[Read the upstream terms](https://github.com/kevchant/GitHub-fabric-cicd-sample/blob/main/README.md).
**Reviewed:** 2026-10-05.

## Platform and tool references

### [Understand lakehouse ingestion and transformation](https://learn.microsoft.com/en-us/fabric/data-engineering/tutorial-lakehouse-introduction)

Follow the end-to-end data flow, then inspect where incremental updates enter it.

**By:** Microsoft. **Source:** Platform or tool publisher. **Type:** guide.
**Needs:** Fabric workspace and capacity; cloud tutorial.
**Reviewed:** 2026-10-05.

### [Load files and tables from a notebook](https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-notebook-load-data)

Check Files versus Tables and relative versus ABFS paths before moving a notebook.

**By:** Microsoft. **Source:** Platform or tool publisher. **Type:** guide.
**Needs:** Fabric notebook and lakehouse.
**Reviewed:** 2026-10-05.

### [Review notebook code and bindings in Git](https://learn.microsoft.com/en-us/fabric/data-engineering/notebook-source-control-deployment)

Check notebook source and target lakehouse/environment bindings during a release.

**By:** Microsoft. **Source:** Platform or tool publisher. **Type:** guide.
**Needs:** Fabric workspace, Git integration and item ownership.
**Reviewed:** 2026-10-05.

### [Check supported items in Git integration](https://learn.microsoft.com/en-us/fabric/cicd/git-integration/intro-to-git-integration)

Check supported items and provider limitations before designing branch-based development.

**By:** Microsoft. **Source:** Platform or tool publisher. **Type:** guide.
**Needs:** Fabric tenant settings, supported capacity and Git provider.
**Reviewed:** 2026-10-05.

### [Promote changes with deployment pipelines](https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines)

Compare stages and dependencies; a deployment does not prove the data is correct.

**By:** Microsoft. **Source:** Platform or tool publisher. **Type:** guide.
**Needs:** Fabric deployment permissions and supported items/capacity.
**Reviewed:** 2026-10-05.

### [Fabric CI/CD Python library](https://github.com/microsoft/fabric-cicd)

Explore code-first publishing, parameters and workspace examples. Check item support before choosing it.

**By:** Microsoft contributors. **Source:** Platform or tool publisher. **Type:** repository.
**Needs:** Python, Fabric authentication and deployment permissions.
**Upstream licence:** MIT. Linked code keeps its own terms.
**Reviewed:** 2026-10-05.

### [Fabric CLI](https://github.com/microsoft/fabric-cli)

Start with workspace listing and item inspection before using import or deployment commands.

**By:** Microsoft contributors. **Source:** Platform or tool publisher. **Type:** repository.
**Needs:** Local Python; Fabric account for remote operations.
**Upstream licence:** MIT. Linked code keeps its own terms.
**Reviewed:** 2026-10-05.

### [Fabric samples](https://github.com/microsoft/fabric-samples)

Find notebooks and scenario samples; read prerequisites for the specific folder you choose.

**By:** Microsoft contributors. **Source:** Platform or tool publisher. **Type:** repository.
**Needs:** Varies by sample; many need Fabric capacity.
**Upstream licence:** MIT. Linked code keeps its own terms.
**Reviewed:** 2026-10-05.

### [Fabric toolbox](https://github.com/microsoft/fabric-toolbox)

Inspect operational scripts for your task. Review each tool and its permissions before use.

**By:** Microsoft contributors. **Source:** Platform or tool publisher. **Type:** repository.
**Needs:** Varies by utility; usually an authorised Fabric tenant.
**Upstream licence:** MIT. Linked code keeps its own terms.
**Reviewed:** 2026-10-05.

### [Semantic Link Labs](https://github.com/microsoft/semantic-link-labs)

Explore semantic-model and workspace inspection from Fabric notebooks.

**By:** Microsoft contributors. **Source:** Platform or tool publisher. **Type:** repository.
**Needs:** Fabric notebook; semantic-link dependencies and permissions.
**Upstream licence:** MIT. Linked code keeps its own terms.
**Reviewed:** 2026-10-05.

### [Choose watermark or change capture in Copy job](https://learn.microsoft.com/en-us/fabric/data-factory/incremental-copy-job)

Check whether your load needs deletions and what resetting an append load means for duplicates.

**By:** Microsoft. **Source:** Platform or tool publisher. **Type:** guide.
**Needs:** Supported source and Fabric Copy job.
**Reviewed:** 2026-10-05.

### [Separate workspace, item and data permissions](https://learn.microsoft.com/en-us/fabric/security/security-overview)

Start an access review by listing the paths a reader can use, including direct data access.

**By:** Microsoft. **Source:** Platform or tool publisher. **Type:** guide.
**Needs:** Fabric tenant; test with distinct authorised identities.
**Reviewed:** 2026-10-05.
