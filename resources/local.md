# Local Python, DuckDB and VS Code

[Library home](../README.md)

Run a file-sized problem on your own computer. These exercises need no database service, container or cloud trial.

## A useful order

1. Create a Python environment and install the pinned recipe dependencies.
2. Select that environment in VS Code and in your notebook kernel.
3. Read CSV fields deliberately; inspect the accepted Parquet output.
4. Add rejection and schema-change cases before using your own authorised files.

Try the [original local recipes](https://github.com/ingestron-io/data-engineering-recipes) before adapting them to a workspace.

## Selected references

### [DuckDB Python quickstart](https://duckdb.org/docs/current/clients/python/overview.html)

Run SQL against local files in a Python process without a database server.

**By:** DuckDB contributors. **Type:** guide. **Needs:** Local Python; DuckDB package.
**Reviewed:** 2026-10-05.

### [Query Parquet with DuckDB](https://duckdb.org/docs/current/data/parquet/overview.html)

Inspect files and filter columns before loading a full dataset into memory.

**By:** DuckDB contributors. **Type:** guide. **Needs:** DuckDB and local Parquet files.
**Reviewed:** 2026-10-05.

### [Control CSV parsing](https://duckdb.org/docs/current/data/csv/overview.html)

Make types and bad-row behaviour explicit when a CSV contains surprises.

**By:** DuckDB contributors. **Type:** guide. **Needs:** DuckDB and local CSV files.
**Reviewed:** 2026-10-05.

### [Inspect a DuckDB query plan](https://duckdb.org/docs/current/guides/meta/explain.html)

Compare actual query work before making a performance claim.

**By:** DuckDB contributors. **Type:** guide. **Needs:** DuckDB and a reproducible query.
**Reviewed:** 2026-10-05.

### [Select the Python environment in VS Code](https://code.visualstudio.com/docs/python/environments)

Fix interpreter mismatches when a package works in the terminal but not in the editor.

**By:** Microsoft. **Type:** guide. **Needs:** VS Code and the Python extension.
**Reviewed:** 2026-10-05.

### [Run Jupyter notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

Select the same environment as your terminal so notebook results are reproducible.

**By:** Microsoft. **Type:** guide. **Needs:** VS Code, Python/Jupyter extensions and an appropriate kernel.
**Reviewed:** 2026-10-05.

### [Manage Python environments with uv](https://docs.astral.sh/uv/guides/projects/)

Explore project dependencies and lockfiles when a small recipe grows into a maintained tool.

**By:** Astral. **Type:** guide. **Needs:** Local uv installation.
**Reviewed:** 2026-10-05.

### [Scan data lazily with Polars](https://docs.pola.rs/user-guide/lazy/using/)

Use a query plan for local transformations rather than eagerly loading every file.

**By:** Polars contributors. **Type:** guide. **Needs:** Python and Polars; local files.
**Reviewed:** 2026-10-05.
