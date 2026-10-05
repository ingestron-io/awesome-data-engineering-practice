# Quality, governance and project work

[Library home](../README.md)

Write the expected behaviour in examples that someone else can check. Tool selection comes after the problem is clear.

## A useful order

1. Define the row meaning, key, freshness and owner with the requester.
2. Agree what should happen to bad rows and missed deadlines.
3. Test reader access through each supported query path.
4. Record the decision, release revision and recovery procedure.

Try the [original local recipes](https://github.com/ingestron-io/data-engineering-recipes) before adapting them to a workspace.

Jump to: [Practitioner articles](#practitioner-articles) · [Community projects and project guides](#community-projects-and-project-guides) · [Platform and tool references](#platform-and-tool-references) · [Original recipes](#original-recipes)

## Practitioner articles

### [Data Dies in Darkness](https://locallyoptimistic.com/post/data-dies-in-darkness/)

Start with disagreeing report totals. Consider named metric owners and a feedback loop for finding stale assumptions.

**By:** Michael Kaminsky · Locally Optimistic · **Source:** Practitioner article

- **Needs:** Discussion with business owners and data consumers; no new tool required.
- **Before using it:** An organisational opinion. Its broad collection/sharing advice is not a privacy or retention policy.
- **Published:** 2018-04-15. **Reviewed:** 2026-10-05.

## Community projects and project guides

### [OpenLineage event model](https://openlineage.io/docs/spec/object-model/)

Understand job, run and dataset metadata before choosing what evidence your pipeline should emit.

**By:** OpenLineage contributors · **Source:** Community project

- **Needs:** Reference only; an event consumer is a separate dependency.
- **Reviewed:** 2026-10-05.

### [Open Data Contract Standard](https://github.com/bitol-io/open-data-contract-standard)

Write down what a table means, who owns it and how fresh it should be. Review the agreement in Git.

**By:** Bitol contributors · **Source:** Community project

- **Needs:** YAML examples; JSON Schema-aware editor such as VS Code.
- **Before using it:** An agreed file describes expectations; separate implementation and access tests must enforce them.
- **Upstream licence:** Apache-2.0. Linked code keeps its own terms.
- **Reviewed:** 2026-10-05.

## Platform and tool references

### [dbt data tests](https://docs.getdbt.com/docs/build/data-tests)

Use assertions to describe invalid rows and business-key failures. Match the adapter to your engine.

**By:** dbt Labs · **Source:** Platform or tool publisher

- **Needs:** dbt and a supported adapter; platform costs vary.
- **Reviewed:** 2026-10-05.

### [Write an architecture decision record](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record)

Capture a concrete choice, rejected alternatives and consequences for the next maintainer.

**By:** Microsoft · **Source:** Platform or tool publisher

- **Needs:** No runtime needed.
- **Reviewed:** 2026-10-05.

### [Choose a database for the workload](https://learn.microsoft.com/en-us/azure/architecture/databases/database-get-started)

Compare storage requirements and database choices before drawing a service diagram.

**By:** Microsoft · **Source:** Platform or tool publisher

- **Needs:** Reference only; architectures can include paid services.
- **Reviewed:** 2026-10-05.

## Original recipes

### [Original runnable engineering recipes](https://github.com/ingestron-io/data-engineering-recipes)

Try synthetic retries, late updates, joins and rejected rows locally, then review platform differences.

**By:** Pipeline Practice · **Source:** Original recipe

- **Needs:** Python and DuckDB; optional Java/PySpark.
- **Upstream licence:** MIT. Linked code keeps its own terms.
- **Reviewed:** 2026-10-05.
