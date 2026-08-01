# Publication handoff

Target: `willowridge1234/membershipworks-member-directory-export-guide`, public branch `main`.

This repository is already live. Publish the current local `main` as one fast-forward commit on
top of the current public `main`; do not re-initialize the repository and do not force-push. The
box has no GitHub push credential, so publication must use the routed GitHub integration.

## Exact publication procedure

1. Fetch the public `main` commit and use its tree as the base tree.
2. Create UTF-8 blobs from these exact committed local files:
   - `README.md`
   - `PUBLISHING.md`
   - `scripts/clean_dedupe.py`
   - `tests/test_clean_dedupe.py`
3. Create a tree replacing only those four paths, preserving every other public path from the
   base tree.
4. Create a commit with the public `main` commit as its sole parent and message
   `Fix duplicate grouping claims and transitive matching`.
5. Fast-forward `refs/heads/main` to that commit with force disabled.

The live README contained a later related-guides edit that was absent from the old local commit.
That edit has been reconciled into the local README and must be preserved during publication.

## Required anonymous verification

- Fetch the raw public `README.md`, `PUBLISHING.md`, `scripts/clean_dedupe.py`, and
  `tests/test_clean_dedupe.py`; after normalizing CRLF to LF, each must equal the corresponding
  committed local file.
- The disclosed, UTM-tagged paid-actor URL must occur exactly once in `README.md`.
- `python3 tests/test_clean_dedupe.py` must report seven passing tests in a fresh public copy.
- The documented sample command must still read six rows and flag four rows into two review
  groups without merging or deleting anything.
- Confirm the README still contains no actor-bound query, collection endpoint, selector, or
  "secret method" framing, and the sample remains entirely synthetic (`.example` domains and
  reserved `555-01xx` numbers).

If the branch update cannot be confirmed, record the external-effect job as `uncertain`; never
report publication success based only on blob, tree, or commit creation.
