# Suggest a useful resource

Send a pull request with one real task the resource helps solve. We welcome
practitioner articles, consultancy walkthroughs, community projects and platform
documentation. Prefer the author's own page or maintained project over a copied
list or anonymous summary. Give the original author credit and explain
prerequisites, native-cloud costs and any support limits.

A community article should show a worked problem, a useful investigation or a
concrete trade-off. Keep personal experience separate from verified platform
behaviour. Do not claim financial independence from a non-vendor URL.

Add the entry to `resources.json` with category, title, author, URL, original
selection note (`why`), prerequisites (`requires`), kind and ISO review date.
Add `sourceType`: `vendor`, `project`, `practitioner`, `consultancy` or `original`.
Use `kind: article` for a practitioner or consultancy article; add `caution` for
its version/experience boundary and `publishedAt` when the page states a date.
Do not guess a publication date; the renderer labels its absence.
Fetch and inspect the destination; a search snippet alone is not a review.
For a repository, record the README blob, licence metadata and archived status
in a dated `docs/*-review-*.json` record. Each selected URL has one current record.
Article evidence repeats its source type and publication date (or `null` when
unstated). Unclassified licences need a note linked to upstream terms. If no
licence exists, label the sample reference only and ask its owner before reuse.
Do not copy an upstream README or article into this repository.

```sh
python3 scripts/render.py
python3 scripts/check.py
```

Keep the generated index short. Put a practical explanation in `guides/`, link
its sources and distinguish your recommendation from platform behaviour.
Do not add affiliate links, copied list dumps, private data or untested cloud claims.
