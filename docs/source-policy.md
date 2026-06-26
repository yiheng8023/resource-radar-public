# Source Policy

Sources should be treated as evidence, not as automatic approval.

## Preferred source traits

- official or primary source when available;
- stable HTTPS URL;
- clear maintainer or organization identity;
- documented license or terms;
- active maintenance or clear archival status;
- usable documentation;
- low account coupling;
- clear downstream fit.

## Weak signals

Stars, likes, reposts, social hype, and old reputation are useful only as weak
signals. They must not be the only reason to promote a resource.

## License stance

License metadata is conservative:

- no license means `needs_manual_review`;
- unclear terms mean `needs_manual_review`;
- source-available is not the same as open source;
- this repository does not provide legal advice.

## Promotion gate

Before a resource enters a downstream lane, check:

1. source provenance;
2. license or terms;
3. maintenance/freshness;
4. quality and documentation;
5. overlap with existing resources;
6. portability;
7. security and supply-chain risk;
8. downstream-specific acceptance rules.
