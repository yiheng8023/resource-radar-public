# resource-radar-public

English | [简体中文](README.zh-CN.md)

A public-safe, agent-neutral starter kit for building a resource radar: collect
public resources, normalize metadata, score quality signals, track lifecycle
state, and generate reviewable reports without exposing a private candidate
pool.

This repository is the public template and demo surface for a private resource radar
workflow. It is intentionally generic: it can support GitHub projects,
technical documentation, research resources, bookmark catalogs, agent skills,
learning materials, and other useful public resources.

## Start here

| If you want to... | Go here |
| --- | --- |
| See the generated demo report | [`outputs/demo-report.md`](outputs/demo-report.md) |
| Inspect demo resource records | [`data/demo/`](data/demo) |
| Review scoring and lifecycle policy | [`policies/`](policies) |
| Run the demo locally | `python -B scripts/run_demo.py --check` |
| Understand the full system | [`open-resource-governance/docs/system-topology.md`](https://github.com/yiheng8023/open-resource-governance/blob/main/docs/system-topology.md) |

## System context

This repository is one public workstream in the
[`open-resource-governance`](https://github.com/yiheng8023/open-resource-governance)
ecosystem.

```text
open-resource-governance
  -> maps the whole system, public/private boundaries, and release gates

resource-radar-public
  -> provides public-safe resource structure, scoring/lifecycle examples, demo reports, and validation

private resource-radar
  -> may keep real candidate pools, snapshots, account-specific automation, and review notes

research-bookmarks-public
  -> can provide public source seeds for future discovery

agent-skills-curated
  -> may consume reviewed skill candidates after separate admission
```

If you only need the radar pattern, start here. If you need the whole repository
family map, see the hub topology:
[`open-resource-governance/docs/system-topology.md`](https://github.com/yiheng8023/open-resource-governance/blob/main/docs/system-topology.md).

## What problem does this solve?

Good resources decay into noise when they are collected without structure:

- links are scattered across stars, bookmarks, notes, chats, and local files;
- popularity is mistaken for quality;
- license, freshness, maintenance, and trust signals are not recorded;
- private preferences and public resources get mixed together;
- downstream systems cannot tell whether something is a tool, reference,
  skill candidate, learning source, bookmark seed, or reject.

`resource-radar-public` gives you a small, reproducible pattern:

```text
public candidates
-> normalized records
-> scoring and lifecycle policy
-> deterministic report
-> review gate
-> downstream-specific output
```

## What this repository provides

- A public-safe resource record structure.
- Demo resource records using only public, official, or broadly reusable
  examples.
- A universal domain taxonomy aligned with the bookmark workstream.
- Configurable scoring and lifecycle policies.
- A deterministic demo report generator.
- Verification scripts that check schema shape, generated output, and obvious
  private-data mistakes.
- Documentation for public/private boundaries, source policy, automation
  limits, and downstream relationships.

## What this repository does not own

This repository does not:

- store a private candidate pool;
- scrape the web or GitHub at scale;
- star, unstar, label, or mutate external accounts;
- decide that a resource is safe for commercial use;
- install tools, agent skills, plugins, MCP servers, or browser bookmarks;
- replace legal, security, licensing, or maintainer review.

## Relationship to the private radar

The paired private repository is `resource-radar`.

```text
resource-radar
  private source, true candidate pool, snapshots, review notes, account-specific automation

resource-radar-public
  public resource structure, demo records, scoring/lifecycle examples, reports, validation
```

Private automation may consume this public template, but public users should not
need the private repository to understand or run the demo.

## Agent-neutral and tool-neutral

This repository is not Codex-specific, Claude-specific, or agent-specific.
Agent skills are only one possible downstream target. Other targets may include
bookmarks, software tools, learning resources, reference catalogs, datasets,
documentation sources, or future project-specific outputs.

## Quick start

```bash
git clone https://github.com/yiheng8023/resource-radar-public.git
cd resource-radar-public
python -B scripts/run_demo.py --check
python -B scripts/verify.py
```

To regenerate the demo report:

```bash
python -B scripts/run_demo.py
```

Generated output:

- [`outputs/demo-report.md`](outputs/demo-report.md)
- [`outputs/demo-report.json`](outputs/demo-report.json)

## Directory layout

```text
data/demo/              public-safe demo resource records
docs/                   design, boundary, source policy, relationship map
outputs/                deterministic generated demo report
policies/               scoring and lifecycle policy examples
policies/domain-taxonomy.json
                        universal public domain taxonomy
schemas/                resource record schema
scripts/                demo generation and verification scripts
```

## Resource lifecycle

The demo uses a conservative state model:

| State | Meaning |
| --- | --- |
| `candidate` | Worth tracking, not yet reviewed for downstream use |
| `watch` | Promising but needs freshness, license, or quality follow-up |
| `reference` | Useful as a public reference or benchmark |
| `adopt` | Strong enough to consider for a downstream target |
| `reject` | Do not promote; keep only if evidence is useful |
| `retired` | Previously useful but no longer recommended |

The state is not a final verdict. It is a review aid.

## Quality signals

The public demo intentionally treats stars as optional and weak. Scoring favors
signals that are easier to audit:

- official or authoritative source;
- clear documentation;
- active maintenance or freshness;
- visible tests, releases, or quality process when relevant;
- license clarity;
- downstream fit;
- low private-data and account-coupling risk.

## Downstream targets

A resource can map to multiple targets:

- `tool`
- `reference`
- `learning`
- `bookmark_seed`
- `skill_candidate`
- `dataset`
- `workflow`
- `standard`

This avoids forcing every useful resource into an agent-skill repository.

## Verification

The public verification checks:

- required files exist;
- resource IDs are unique;
- demo records match the expected public-safe shape;
- generated reports are deterministic and up to date;
- public files do not contain obvious private-only terms;
- URLs are HTTPS public references;
- policy files have the expected schema version.

## Safety boundary

Only public-safe data belongs here. Do not add private bookmarks, credentials,
tokens, local paths, account state, personal preferences, private review notes,
browser/session data, or private candidate lists.

## License

MIT. See [`LICENSE`](LICENSE).
