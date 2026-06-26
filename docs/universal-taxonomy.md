# Universal Resource Taxonomy

`resource-radar-public` includes a public-safe universal domain taxonomy in
[`policies/domain-taxonomy.json`](../policies/domain-taxonomy.json).

The taxonomy is shared with the bookmark lane. It gives humans a stable
top-level directory while keeping the radar model richer than a browser folder
tree.

## Why align with bookmarks?

Bookmarks are the easiest human-facing projection to understand. Their top-level
domains provide a useful navigation layer:

```text
AI / software / data / science / engineering / health / environment / history
humanities / social science / design / education / law / governance / industry
media-life / methodology
```

The radar should align with that directory so a resource can flow into bookmark
exports, catalog reports, curated-skill candidate lists, or future knowledge
graphs without being reclassified from scratch.

## Why not make taxonomy equal to bookmarks?

The radar needs separate axes:

- domain category;
- source type;
- downstream lane;
- lifecycle state;
- trust tier;
- license review;
- risk flags;
- visibility layer;
- export target.

A browser folder can be a projection, but it should not carry all governance
meaning by itself.

## Reserved domains

Two domains are intentionally reserved for controlled placement:

- `90_low_trust_fallback_resources`: fallback resources that must never become
  main-domain authority without review.
- `99_archive`: historical, deprecated, or review-later resources.

These are valid taxonomy nodes, but public exports may choose to hide them or
keep them separate.
