# Design Basis

The design starts from one practical observation: useful resources are not only
software packages. They may be docs, standards, examples, datasets, workflows,
research papers, bookmarks, agent skills, or project templates.

## Goals

1. Keep discovery broad without turning the output into noise.
2. Separate public reusable method from private candidate state.
3. Record why a resource is worth attention.
4. Treat popularity as one weak signal, not the quality gate.
5. Let multiple downstream lanes consume the same normalized record.
6. Keep automation gated, deterministic, and auditable.

## Non-goals

- no blind auto-import into downstream repositories;
- no claim that a resource is commercially safe without review;
- no agent-specific design;
- no assumption that GitHub stars are enough;
- no scraping or external account mutation in the public demo.

## Loop

```text
discover
-> normalize
-> score
-> lifecycle classify
-> report
-> review
-> project into a lane
```

The public repository demonstrates the loop with static demo data. Private
installations can add real source adapters and account-specific automation.
