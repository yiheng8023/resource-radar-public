# Relationship Map

```text
resource-radar
  private source and true candidate pool
  -> may consume this public template
  -> may emit public-safe projections after review

resource-radar-public
  public-safe template, schema, demo data, policies, generated report
  -> does not own private candidates
  -> does not mutate external accounts
  -> does not install downstream artifacts

open-resource-governance
  public hub and global map
  -> indexes this repository as the public radar template
  -> documents how it relates to bookmarks, skills, and config lanes
```

## Downstream consumers

Potential consumers include:

- bookmark catalogs;
- curated skill repositories;
- tool directories;
- learning maps;
- documentation indexes;
- dataset catalogs;
- project-specific resource dashboards.

No downstream lane should treat this repository as proof that a resource has
already passed its own admission rules.
