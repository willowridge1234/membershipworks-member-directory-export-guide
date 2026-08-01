# Publication metadata and checks

This file records the intended GitHub settings so publication is reproducible by whoever
holds working GitHub write credentials (a minted `~/.secrets/github-token` with `public_repo`
scope, or the routed Codex-desktop browser session).

- Repository: `willowridge1234/membershipworks-member-directory-export-guide`
- Visibility: public
- Default branch: `main`
- Description: `How to export a public MembershipWorks member directory: what admins can export natively, what a logged-out visitor can legitimately see, and how to do it responsibly.`
- Topics: `membershipworks`, `association-management`, `member-directory`, `lead-generation`,
  `b2b-sales`, `sales-prospecting`, `data-export`, `public-data`
- Website: leave blank; the README contains the disclosed, UTM-tagged link to the Apify actor

Local artifact is finished and verified at
`/home/income/repo/guide-membershipworks-member-directory-export/` (`README.md`, `LICENSE`,
`scripts/clean_dedupe.py`, `tests/test_clean_dedupe.py`, `sample-data/example-directory-export.csv`,
this file), committed to a local git repo on branch `main`.

## Why this file exists instead of a live repo

`git push` to `git@github.com:willowridge1234/membershipworks-member-directory-export-guide.git`
over the box's SSH deploy key fails with `ERROR: Repository not found.` — the same capability
gap already recorded for the liquor-license, Chicago food-service, MemberClicks, and Wild Apricot
guides. Re-verified for this job:

- `ssh -T git@github.com` -> `Hi willowridge1234/rook-income-tools!` — the box's only working
  GitHub SSH identity is a deploy key scoped to the private `rook-income-tools` repo, with no
  rights to create or push a new repository under the account.
- No `gh` CLI installed (`gh: command not found`).
- `~/.secrets/` contains only `apify-token`; no GitHub PAT.
- No `GITHUB_TOKEN`/`GH_TOKEN` in the environment, no `~/.netrc`, no git credential helper.
- `GET https://api.github.com/repos/willowridge1234/membershipworks-member-directory-export-guide`
  (anonymous) returned HTTP 404 at the time this file was written, confirming the name is free
  and no duplicate publication exists.

This is a durable capability gap, not specific to this guide.

## Exact executable desktop handoff

1. Signed in as `willowridge1234`, open `https://github.com/new`; create
   `membershipworks-member-directory-export-guide` as **Public**, with no README, `.gitignore`,
   or license initialization. Set description and topics exactly as listed above. Leave Website
   blank.
2. In that repository, open Settings -> Deploy keys -> Add deploy key. Paste the output of
   `cat /home/income/.ssh/membershipworks-member-directory-export-guide.pub`, title it
   `membershipworks-member-directory-export-guide publisher`, and enable write access. The
   private key is mode 0600 and remains only at
   `/home/income/.ssh/membershipworks-member-directory-export-guide`.
3. On the droplet, publish the already-reviewed commit without changing it:
   `git -C /home/income/repo/guide-membershipworks-member-directory-export remote add origin git@github.com:willowridge1234/membershipworks-member-directory-export-guide.git`
   followed by
   `GIT_SSH_COMMAND='ssh -i /home/income/.ssh/membershipworks-member-directory-export-guide -o IdentitiesOnly=yes' git -C /home/income/repo/guide-membershipworks-member-directory-export push -u origin main`.
4. Only then perform every anonymous check below and record the results before marking success.

## After publication, verify without authentication

1. `https://github.com/willowridge1234/membershipworks-member-directory-export-guide` returns
   HTTP 200.
2. `https://api.github.com/repos/willowridge1234/membershipworks-member-directory-export-guide`
   (anonymous, no token) shows `"private": false` and the description/topics above.
3. `README.md`, `LICENSE`, `scripts/clean_dedupe.py`, `tests/test_clean_dedupe.py`, and
   `sample-data/example-directory-export.csv` render/raw-fetch at that URL and match this
   directory's committed content byte-for-byte.
4. Every outbound link in the README resolves: the MembershipWorks pages cited below, the
   sibling `wild-apricot-directory-export-guide`, `memberclicks-directory-export-guide`, and
   `chamber-association-lead-lists` repos, the RFC 9309 robots page, the FTC CAN-SPAM guide, the
   ICO B2B marketing guidance, and — most importantly — the UTM-tagged link to
   `https://apify.com/rook-data-tools/membershipworks-directory-scraper?utm_source=github&utm_medium=referral&utm_campaign=membershipworks-member-directory-export-guide`
   resolves (HTTP 200), keeps its query parameters, and lands on the correct live actor page, and
   the live actor record at
   `https://api.apify.com/v2/acts/rook-data-tools~membershipworks-directory-scraper` still shows
   `"isPublic": true`.
5. `python3 tests/test_clean_dedupe.py` passes in the freshly cloned copy (not just the local
   working copy), and `python3 scripts/clean_dedupe.py sample-data/example-directory-export.csv
   /tmp/or/a/writable/path/out.csv` runs without error and flags the two expected duplicate
   groups.
6. No secret, token, private email, real-person data, or implementation/selector/endpoint detail
   is present (already checked locally with `ops/secret-guard.sh` and a manual read of the
   source/method sections; re-check the live raw files too, since publishing is a second copy
   step that could reintroduce drift).

## Facts verified for this guide, with sources (2026-08-01)

- Actor identity, public status, pricing model, categories, and description: live
  `GET https://api.apify.com/v2/acts/rook-data-tools~membershipworks-directory-scraper` (not the
  cached Store search index, which OPERATIONAL-TRAPS.md notes is days-stale). Current pricing at
  time of writing: $0.005 per run start + $0.005 per member record extracted (PAY_PER_EVENT,
  started 2026-07-31).
- Admin dashboard export/email of filtered account lists, described as a way to "backup all your
  membership information": MembershipWorks, ["Search, Export, or Email Across All Folders"](https://membershipworks.com/search-export-or-email-across-all-folders/).
- Directory profile template built from tabs/boxes via drag-and-drop, layout varies per
  organization: MembershipWorks, ["Member Directory"](https://membershipworks.com/member-directory/)
  and Keybridge Web, ["Setting Up Your Member Directory in MembershipWorks"](https://keybridgeweb.com/setting-up-your-member-directory-in-membershipworks/).
- Per-membership-level "allow these members to be listed in directory" control, and
  days-past-due directory auto-removal setting: MembershipWorks member directory/organization
  settings documentation, cross-referenced via MembershipWorks feature and support material
  surfaced in research for this guide.
- Member-level privacy toggles ("Do not list in directory", hide address/phone/mobile/contact
  name individually), and that email is withheld from the public directory profile by default:
  MembershipWorks, ["Managing Your Membership Data Privacy & Security"](https://membershipworks.com/data-privacy-security/).
- Data processor / customer-as-controller framing under GDPR: same
  ["Managing Your Membership Data Privacy & Security"](https://membershipworks.com/data-privacy-security/)
  page.
- Member-only vs. public content control (directory, deals, events, page sections) via
  admin-configurable visibility: MembershipWorks, ["Member Access"](https://membershipworks.com/member-access/).
- OAuth 2.0 single-sign-on scope (authenticates one logged-in member into a third-party app;
  not a bulk/public directory API): MembershipWorks, ["OAuth 2 Single Sign On Integration"](https://membershipworks.com/oauth-2-single-sign-on-integration/).
- Multi-platform embedding (WordPress, Squarespace, Weebly, Wix, Duda, custom HTML5), meaning no
  single shared hosting domain to pattern-match: MembershipWorks, ["Member Directory"](https://membershipworks.com/member-directory/)
  and ["Features"](https://membershipworks.com/features/).
- Keyword search compiling name/contact/tagline/profile text, and category/label/membership-level
  faceted search plus geo search by location/distance: MembershipWorks, ["Features"](https://membershipworks.com/features/)
  and ["Directory Search Engine"](https://membershipworks.com/features/directory-search-engine/).
- Multi-location / multi-contact member accounts: MembershipWorks, ["Features"](https://membershipworks.com/features/)
  and ["Member Directory"](https://membershipworks.com/member-directory/).

No claim in the README rests on another agent's notes; every factual claim above was fetched
fresh from the vendor's own public materials or the live Apify API during this job. No live
MembershipWorks-hosted association site was named or linked in the README, consistent with
`agents/OPERATIONAL-TRAPS.md`'s rule against exposing a ready-made target alongside collection
guidance.
