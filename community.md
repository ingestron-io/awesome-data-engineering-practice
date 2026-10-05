# Community projects and field notes

[Library home](README.md)

Learn from people who explain a failure, show their code or describe a trade-off.
This page brings together practitioner articles, consultancy walkthroughs and community projects.
Some projects have commercial backing. Source labels describe who publishes the material, not financial independence.

Each platform page includes prerequisites, publication/review dates and reuse notes.
Article experience is attributed to its author; upstream samples have not been run by this library.

## Databricks

[Read the prerequisites and review notes](resources/databricks.md).

- [Up your CI/CD game with Databricks Asset Bundles and Automated Testing](https://www.advancinganalytics.co.uk/blog/up-your-ci/cd-game-with-databricks-asset-bundles-and-automated-testing) — Separate valid configuration from a tested workload. Follow the author’s validate, deploy-to-test and run-tests sequence. By Connor Quinn · Advancing Analytics.
- [Avoid Delta Live Table Pipeline Conflicts with Parameterised Databricks Asset Bundles](https://www.advancinganalytics.co.uk/blog/avoid-delta-live-table-conflicts-with-databricks-asset-bundles) — See why two developers can collide on the same target tables. Review a separate user target and schema naming. By Jordan Witcombe · Advancing Analytics.

## Microsoft Fabric

[Read the prerequisites and review notes](resources/fabric.md).

- [Fabric CI/CD with GitHub Actions — companion sample](https://github.com/kevchant/GitHub-fabric-cicd-sample) — Inspect a practitioner workflow with separate workspace values and a reusable Python deployment script. By Kevin Chant.
- [Data engineering with Microsoft Fabric (incremental batch load)](https://www.ibradshaw.info/blog/41/) — Walk through moving an incremental file load from Databricks to Fabric, including notebook parameters and file paths. By Ian Bradshaw.
- [Unreliable logging in data factory pipelines](https://richardswinbank.net/fabric/unreliable_logging_in_data_factory_pipelines) — Investigate a timestamp that differs between an activity log and the stored result. Compare the actual write when debugging. By Richard Swinbank.
- [Operationalize fabric-cicd to work with Microsoft Fabric and GitHub Actions](https://www.kevinrchant.com/2025/04/11/operationalize-fabric-cicd-to-work-with-microsoft-fabric-and-github-actions/) — Follow a worked release across test and production workspaces. Review how variables and parameters change by target. By Kevin Chant.

## Azure Data Factory

[Read the prerequisites and review notes](resources/adf.md).

- [azure.datafactory.tools](https://github.com/Azure-Player/azure.datafactory.tools) — Review factory dependencies, environment substitutions and trigger handling when deploying ADF JSON from Git. By Kamil Nowinski and contributors.
- [ADF testing series — companion code](https://github.com/richardswinbank/community) — Pair the ADF testing articles with pipeline JSON, NUnit tests and release YAML in the adf-testing-series folder. By Richard Swinbank.
- [Testing Azure Data Factory in your CI/CD pipeline](https://richardswinbank.net/adf/testing_azure_data_factory_in_your_cicd_pipeline) — Connect pipeline changes to functional tests. The article explains deployment, test-project build and isolated test configuration. By Richard Swinbank.

## Spark and Delta

[Read the prerequisites and review notes](resources/spark.md).

- [Spark SQL reference](https://spark.apache.org/docs/latest/sql-ref.html) — Check null, join and expression behaviour against the runtime you actually use. By Apache Spark.
- [Explain and tune a Spark query](https://spark.apache.org/docs/latest/sql-performance-tuning.html) — Use query plans, statistics and skew evidence to choose a tuning change. By Apache Spark.
- [Test PySpark transformations](https://spark.apache.org/docs/latest/api/python/getting_started/testing_pyspark.html) — Write focused DataFrame and schema assertions for small synthetic inputs. By Apache Spark.
- [Structured Streaming semantics](https://spark.apache.org/docs/latest/streaming/apis-on-dataframes-and-datasets.html) — Check state, watermarks, checkpoints and sink behaviour before claiming replay safety. By Apache Spark.
- [Delta Lake source and examples](https://github.com/delta-io/delta) — Explore transactions and table examples; check the Spark/Delta compatibility matrix first. By Delta Lake contributors.
- [chispa](https://github.com/MrPowers/chispa) — See which rows differ when a Spark transformation test fails. Compare values, schemas and floating-point tolerances. By Matthew Powers and chispa contributors.
- [Testing PySpark Code](https://www.mungingdata.com/pyspark/testing-pytest-chispa/) — Build small input/expected-output tests, including nulls. Read assertion failures to find the row that broke a transformation. By MungingData.

## Local Python, DuckDB and VS Code

[Read the prerequisites and review notes](resources/local.md).

- [DuckDB Python quickstart](https://duckdb.org/docs/current/clients/python/overview.html) — Run SQL against local files in a Python process without a database server. By DuckDB contributors.
- [Query Parquet with DuckDB](https://duckdb.org/docs/current/data/parquet/overview.html) — Inspect files and filter columns before loading a full dataset into memory. By DuckDB contributors.
- [Control CSV parsing](https://duckdb.org/docs/current/data/csv/overview.html) — Make types and bad-row behaviour explicit when a CSV contains surprises. By DuckDB contributors.
- [Inspect a DuckDB query plan](https://duckdb.org/docs/current/guides/meta/explain.html) — Compare actual query work before making a performance claim. By DuckDB contributors.
- [Scan data lazily with Polars](https://docs.pola.rs/user-guide/lazy/using/) — Use a query plan for local transformations rather than eagerly loading every file. By Polars contributors.
- [SQLFluff](https://github.com/sqlfluff/sqlfluff) — Catch inconsistent SQL before review. Select a dialect and check templated SQL in CI or your editor. By SQLFluff contributors.
- [SQLGlot](https://github.com/tobymao/sqlglot) — Inspect SQL structure or compare dialects without connecting to a database. Useful when reviewing a migration. By SQLGlot contributors.
- [Pandera](https://github.com/unionai-oss/pandera) — Check column types and allowed values before accepting a file. Keep the rules beside the Python transformation. By Union.ai and Pandera contributors.
- [Hypothesis](https://github.com/HypothesisWorks/hypothesis) — Find edge cases you did not put in a fixture. Describe a rule and generate inputs that try to break it. By Hypothesis contributors.
- [Faker](https://github.com/joke2k/faker) — Create synthetic names, addresses and dates for examples. Set a seed when you need repeatable test inputs. By Faker contributors.
- [Why I Finally Pulled the Plug on Polars and Moved to DuckDB](https://www.confessionsofadataguy.com/why-i-finally-pulled-the-plug-on-polars-and-moved-to-duckdb/) — Read a practitioner’s account of cloud file-reading friction. Include dependency and authentication behaviour in tool evaluation. By Daniel · Confessions of a Data Guy.

## Quality, governance and project work

[Read the prerequisites and review notes](resources/practice.md).

- [OpenLineage event model](https://openlineage.io/docs/spec/object-model/) — Understand job, run and dataset metadata before choosing what evidence your pipeline should emit. By OpenLineage contributors.
- [Open Data Contract Standard](https://github.com/bitol-io/open-data-contract-standard) — Write down what a table means, who owns it and how fresh it should be. Review the agreement in Git. By Bitol contributors.
- [Data Dies in Darkness](https://locallyoptimistic.com/post/data-dies-in-darkness/) — Start with disagreeing report totals. Consider named metric owners and a feedback loop for finding stale assumptions. By Michael Kaminsky · Locally Optimistic.

[Suggest another worked example](CONTRIBUTING.md).
