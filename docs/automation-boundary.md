# Automation Boundary

The public demo uses deterministic local scripts only. It does not call GitHub
APIs, search engines, browsers, paid services, or external accounts.

## Safe to automate in this repository

- validate demo records;
- apply scoring rules;
- classify lifecycle hints;
- regenerate demo reports;
- check public-safety text rules.

## Requires private implementation or explicit authorization

- GitHub account discovery;
- starring, unstarring, labeling, or list management;
- web crawling;
- paid API calls;
- downstream repository writes;
- promotion into curated skill releases;
- import into browser bookmarks;
- publishing or release automation.

## Recommended private workflow

```text
source adapters
-> snapshots
-> normalization
-> deduplication
-> scoring
-> human review
-> public-safe projection
-> downstream-specific admission
```
