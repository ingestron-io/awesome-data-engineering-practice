# Test what a reader can actually see

[Library home](../README.md) · [Databricks](../resources/databricks.md) · [Fabric](../resources/fabric.md)

An administrator’s masked preview is not a reader test. Use distinct authorised
identities and synthetic values you can recognise in the result.

## Write the expectation first

| Identity       | Expected read                                | Expected write             |
| -------------- | -------------------------------------------- | -------------------------- |
| Data steward   | Synthetic email visible where policy permits | Only the agreed operations |
| Report reader  | Email hidden or column unavailable           | Denied                     |
| Unrelated user | Table unavailable                            | Denied                     |

Adapt this example matrix to your policy. A hash or a renamed column is not an
access restriction. Removing email from a serving table does not stop someone
who can read the raw table.

## Test each route

Record the actual identity, query route, expected result and observed result.
Include direct SQL, notebooks, semantic models and exported files where those
routes exist. A policy attached to one route may not cover another.

Use the [Databricks reader probe](https://github.com/ingestron-io/data-engineering-recipes/tree/main/recipes/masking)
for a disposable Unity Catalog test. Its local tests use fake connections; real
permission tests remain a native task. For Fabric, begin with its workspace,
item and data permission model rather than copying Unity Catalog SQL.

## Keep the evidence safe

Use fictional emails and remove tokens, account details and real rows from
screenshots. Record a permission error separately from a connection failure:
an unavailable service does not prove access was denied.
