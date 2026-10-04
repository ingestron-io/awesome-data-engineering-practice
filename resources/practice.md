# Quality, governance and project work

[Library home](../README.md)

Write the expected behaviour in examples that someone else can check. Tool selection comes after the problem is clear.

## A useful order

1. Define the row meaning, key, freshness and owner with the requester.
2. Agree what should happen to bad rows and missed deadlines.
3. Test reader access through each supported query path.
4. Record the decision, release revision and recovery procedure.

Try the [original local recipes](https://github.com/ingestron-io/data-engineering-recipes) before adapting them to a workspace.

## Selected references

### [OpenLineage event model](https://openlineage.io/docs/spec/object-model/)

Understand job, run and dataset metadata before choosing what evidence your pipeline should emit.

**By:** OpenLineage contributors. **Type:** guide. **Needs:** Reference only; an event consumer is a separate dependency.
**Reviewed:** 2026-10-05.

### [dbt data tests](https://docs.getdbt.com/docs/build/data-tests)

Use assertions to describe invalid rows and business-key failures. Match the adapter to your engine.

**By:** dbt Labs. **Type:** guide. **Needs:** dbt and a supported adapter; platform costs vary.
**Reviewed:** 2026-10-05.

### [Write an architecture decision record](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record)

Capture a concrete choice, rejected alternatives and consequences for the next maintainer.

**By:** Microsoft. **Type:** guide. **Needs:** No runtime needed.
**Reviewed:** 2026-10-05.

### [Choose a database for the workload](https://learn.microsoft.com/en-us/azure/architecture/databases/database-get-started)

Compare storage requirements and database choices before drawing a service diagram.

**By:** Microsoft. **Type:** guide. **Needs:** Reference only; architectures can include paid services.
**Reviewed:** 2026-10-05.

### [Original runnable engineering recipes](https://github.com/ingestron-io/data-engineering-recipes)

Try synthetic retries, late updates, joins and rejected rows locally, then review platform differences.

**By:** Pipeline Practice. **Type:** repository. **Needs:** Python and DuckDB; optional Java/PySpark.
**Upstream licence:** MIT. Linked code keeps its own terms.
**Reviewed:** 2026-10-05.
