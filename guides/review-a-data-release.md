# Review a notebook or pipeline release

[Library home](../README.md) · [Databricks](../resources/databricks.md) · [Fabric](../resources/fabric.md) · [ADF](../resources/adf.md)

The notebook passed its tests. In production it still wrote to the development
lakehouse. Review the code and its target together.

## Use a short review packet

| Question                        | Evidence to keep                                         |
| ------------------------------- | -------------------------------------------------------- |
| What changed?                   | Commit, code diff and changed item definitions           |
| Where will it run?              | Target workspace, lakehouse, environment and connections |
| Does it produce the right data? | Fixture results, key counts, totals and rejected rows    |
| Who can query it?               | Real reader identity and expected allow/deny results     |
| Can we recover?                 | Cursor/checkpoint treatment and a tested recovery plan   |

This packet is our suggested practice. It does not replace each platform’s release tooling.

## Check the platform detail

In Databricks, use bundle validation for configuration and a separate workload
test for results. In Fabric, include notebook dependencies and target bindings in
the review. In ADF, inspect environment parameters and trigger handling alongside
the exported template. The platform pages link to the official procedures.

## Reject a stale review

Try [Changed release files](https://github.com/ingestron-io/data-engineering-recipes/tree/main/recipes/release-check).
Changing a file after review makes the local check fail. This is a small teaching
example: a real release also needs a trusted build record and an authorised deployer.
