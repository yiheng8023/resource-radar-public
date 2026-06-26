# Public / Private Boundary

`resource-radar-public` is safe to publish because it contains only reusable
rules, schema, demo fixtures, generated demo reports, and documentation.

## Public-safe

- generic schemas and policies;
- official/public URLs;
- demo resource records;
- generated reports from demo data;
- documentation about scoring, lifecycle, and review boundaries;
- validation scripts that do not require private accounts.

## Private-only

- complete candidate pools from a user's account;
- private GitHub stars, lists, notes, labels, and review decisions;
- account tokens, cookies, sessions, or OAuth state;
- private bookmarks, local paths, browser-local state, and preferences;
- manual review notes that reveal private intent or personal context;
- unpublished scoring experiments that depend on private data.

## Rule

Public repositories can teach the method. Private repositories hold the real
personal or account-coupled state.
