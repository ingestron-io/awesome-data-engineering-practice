# Local Python, DuckDB and VS Code

[Library home](../README.md)

Run a file-sized problem on your own computer. These exercises need no database service, container or cloud trial.

## A useful order

1. Create a Python environment and install the pinned recipe dependencies.
2. Select that environment in VS Code and in your notebook kernel.
3. Read CSV fields deliberately; inspect the accepted Parquet output.
4. Add rejection and schema-change cases before using your own authorised files.

Try the [original local recipes](https://github.com/ingestron-io/data-engineering-recipes) before adapting them to a workspace.

Jump to: [Practitioner articles](#practitioner-articles) · [Community projects and project guides](#community-projects-and-project-guides) · [Platform and tool references](#platform-and-tool-references)

## Practitioner articles

### [Why I Finally Pulled the Plug on Polars and Moved to DuckDB](https://www.confessionsofadataguy.com/why-i-finally-pulled-the-plug-on-polars-and-moved-to-duckdb/)

Read a practitioner’s account of cloud file-reading friction. Include dependency and authentication behaviour in tool evaluation.

**By:** Daniel · Confessions of a Data Guy · **Source:** Practitioner article

- **Needs:** Reading only; the author’s reproduction involves AWS Lambda and S3.
- **Before using it:** Workload-specific experience, not a benchmark or universal verdict on Polars. Test your own pinned environment.
- **Published:** 2026-04-10. **Reviewed:** 2026-10-05.

## Community projects and project guides

### [DuckDB Python quickstart](https://duckdb.org/docs/current/clients/python/overview.html)

Run SQL against local files in a Python process without a database server.

**By:** DuckDB contributors · **Source:** Community project

- **Needs:** Local Python; DuckDB package.
- **Reviewed:** 2026-10-05.

### [Query Parquet with DuckDB](https://duckdb.org/docs/current/data/parquet/overview.html)

Inspect files and filter columns before loading a full dataset into memory.

**By:** DuckDB contributors · **Source:** Community project

- **Needs:** DuckDB and local Parquet files.
- **Reviewed:** 2026-10-05.

### [Control CSV parsing](https://duckdb.org/docs/current/data/csv/overview.html)

Make types and bad-row behaviour explicit when a CSV contains surprises.

**By:** DuckDB contributors · **Source:** Community project

- **Needs:** DuckDB and local CSV files.
- **Reviewed:** 2026-10-05.

### [Inspect a DuckDB query plan](https://duckdb.org/docs/current/guides/meta/explain.html)

Compare actual query work before making a performance claim.

**By:** DuckDB contributors · **Source:** Community project

- **Needs:** DuckDB and a reproducible query.
- **Reviewed:** 2026-10-05.

### [Scan data lazily with Polars](https://docs.pola.rs/user-guide/lazy/using/)

Use a query plan for local transformations rather than eagerly loading every file.

**By:** Polars contributors · **Source:** Community project

- **Needs:** Python and Polars; local files.
- **Reviewed:** 2026-10-05.

### [SQLFluff](https://github.com/sqlfluff/sqlfluff)

Catch inconsistent SQL before review. Select a dialect and check templated SQL in CI or your editor.

**By:** SQLFluff contributors · **Source:** Community project

- **Needs:** Python CLI and a dialect configuration; no database service.
- **Before using it:** Linting checks syntax and style; it does not prove the query returns correct business results.
- **Upstream licence:** MIT. Linked code keeps its own terms.
- **Reviewed:** 2026-10-05.

### [SQLGlot](https://github.com/tobymao/sqlglot)

Inspect SQL structure or compare dialects without connecting to a database. Useful when reviewing a migration.

**By:** SQLGlot contributors · **Source:** Community project

- **Needs:** Python package; explicit source and target dialects.
- **Before using it:** A successful translation still needs result tests in the target engine.
- **Upstream licence:** MIT. Linked code keeps its own terms.
- **Reviewed:** 2026-10-05.

### [Pandera](https://github.com/unionai-oss/pandera)

Check column types and allowed values before accepting a file. Keep the rules beside the Python transformation.

**By:** Union.ai and Pandera contributors · **Source:** Community project

- **Needs:** Python and the extra for your chosen dataframe library; local file checks need no service.
- **Before using it:** Company-backed open-source project. Use the API and backend supported by your pinned version.
- **Upstream licence:** MIT. Linked code keeps its own terms.
- **Reviewed:** 2026-10-05.

### [Hypothesis](https://github.com/HypothesisWorks/hypothesis)

Find edge cases you did not put in a fixture. Describe a rule and generate inputs that try to break it.

**By:** Hypothesis contributors · **Source:** Community project

- **Needs:** Python test environment; no database service.
- **Before using it:** Generated inputs complement explicit business examples; define the property carefully.
- **Upstream licence:** Upstream LICENSE.txt declares MPL-2.0 with exceptions for attributed third-party code; inspect the applicable file terms. [Read the upstream terms](https://github.com/HypothesisWorks/hypothesis/blob/master/LICENSE.txt).
- **Reviewed:** 2026-10-05.

### [Faker](https://github.com/joke2k/faker)

Create synthetic names, addresses and dates for examples. Set a seed when you need repeatable test inputs.

**By:** Faker contributors · **Source:** Community project

- **Needs:** Python package; locale and seed configuration.
- **Before using it:** Synthetic generation does not anonymise an existing customer dataset; keep real personal data out.
- **Upstream licence:** MIT. Linked code keeps its own terms.
- **Reviewed:** 2026-10-05.

## Platform and tool references

### [Select the Python environment in VS Code](https://code.visualstudio.com/docs/python/environments)

Fix interpreter mismatches when a package works in the terminal but not in the editor.

**By:** Microsoft · **Source:** Platform or tool publisher

- **Needs:** VS Code and the Python extension.
- **Reviewed:** 2026-10-05.

### [Run Jupyter notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

Select the same environment as your terminal so notebook results are reproducible.

**By:** Microsoft · **Source:** Platform or tool publisher

- **Needs:** VS Code, Python/Jupyter extensions and an appropriate kernel.
- **Reviewed:** 2026-10-05.

### [Manage Python environments with uv](https://docs.astral.sh/uv/guides/projects/)

Explore project dependencies and lockfiles when a small recipe grows into a maintained tool.

**By:** Astral · **Source:** Platform or tool publisher

- **Needs:** Local uv installation.
- **Reviewed:** 2026-10-05.
