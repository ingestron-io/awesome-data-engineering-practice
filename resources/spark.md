# Spark and Delta

[Library home](../README.md)

Debug a small input before tuning a large job. Test key counts and totals, then inspect the query plan.

## A useful order

1. Run the synthetic replay example and identify the business key.
2. Test nulls, duplicates, late updates and deletes.
3. Compare plans and measured runtimes for a single tuning change.
4. Check Spark/Delta compatibility and managed-runtime differences.

Try the [original local recipes](https://github.com/ingestron-io/data-engineering-recipes) before adapting them to a workspace.

## Selected references

### [Spark SQL reference](https://spark.apache.org/docs/latest/sql-ref.html)

Check null, join and expression behaviour against the runtime you actually use.

**By:** Apache Spark. **Type:** guide. **Needs:** Spark; latest docs can differ from your managed runtime.
**Reviewed:** 2026-10-05.

### [Explain and tune a Spark query](https://spark.apache.org/docs/latest/sql-performance-tuning.html)

Use query plans, statistics and skew evidence to choose a tuning change.

**By:** Apache Spark. **Type:** guide. **Needs:** Spark workload and measured baseline.
**Reviewed:** 2026-10-05.

### [Test PySpark transformations](https://spark.apache.org/docs/latest/api/python/getting_started/testing_pyspark.html)

Write focused DataFrame and schema assertions for small synthetic inputs.

**By:** Apache Spark. **Type:** guide. **Needs:** Compatible Python, Java and PySpark versions.
**Reviewed:** 2026-10-05.

### [Structured Streaming semantics](https://spark.apache.org/docs/latest/streaming/apis-on-dataframes-and-datasets.html)

Check state, watermarks, checkpoints and sink behaviour before claiming replay safety.

**By:** Apache Spark. **Type:** guide. **Needs:** Spark streaming workload; source/sink-specific guarantees.
**Reviewed:** 2026-10-05.

### [Delta Lake source and examples](https://github.com/delta-io/delta)

Explore transactions and table examples; check the Spark/Delta compatibility matrix first.

**By:** Delta Lake contributors. **Type:** repository. **Needs:** Compatible Java, Spark and Delta versions.
**Upstream licence:** Apache-2.0. Linked code keeps its own terms.
**Reviewed:** 2026-10-05.
