# Retry a load without changing the result

[Library home](../README.md) · [ADF](../resources/adf.md) · [Databricks](../resources/databricks.md) · [Fabric](../resources/fabric.md)

The source sent the same batch twice. Your report now shows twice the sales.
Start by deciding what identifies one order and which version should win.

## Try the failure

Run [Retry a batch](https://github.com/ingestron-io/data-engineering-recipes/tree/main/recipes/retry-batch)
locally. The same two orders are loaded twice. The final count stays at two and
the total stays at 3000 cents.

Then run [Late updates](https://github.com/ingestron-io/data-engineering-recipes/tree/main/recipes/late-updates).
An older change must not overwrite a newer order. A replay must not bring back a deleted order.

## Decide before building

- What is the business key? Can it be reused?
- Does the source provide a reliable version or change position?
- Can two different changes have the same version? Where do conflicts go?
- How are deletes delivered? A watermark on surviving rows may miss them.
- What happens if the write succeeds but saving the cursor fails?

These questions are our recommended review approach. The engine still matters:
Databricks MERGE has runtime-specific duplicate-match rules; Fabric Copy job has
watermark and change-capture routes; ADF lets you build an explicit cursor flow.
Use the linked platform references before adapting the SQL.

## Keep the proof

Save input IDs, the cursor range, accepted/rejected counts and the output total
for the first run and its replay. A completed pipeline is only one part of that evidence.
