# Suggest a useful resource

Send a pull request with one real task the resource helps solve. Prefer official
documentation and project-owned examples. Give the original author credit and
explain prerequisites, native-cloud costs and any support limits.

Add the entry to `resources.json` with category, title, author, URL, original
selection note (`why`), prerequisites (`requires`), kind and ISO review date.
Fetch and inspect the destination; a search snippet alone is not a review.
For a repository, record the README blob, licence metadata and archived status
in the dated source-review record. Unclassified licences need a note linked to
upstream terms. Do not copy an upstream README or article into this repository.

```sh
python3 scripts/render.py
python3 scripts/check.py
```

Keep the generated index short. Put a practical explanation in `guides/`, link
its sources and distinguish your recommendation from platform behaviour.
Do not add affiliate links, copied list dumps, private data or untested cloud claims.
