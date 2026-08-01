# How to export a public MembershipWorks member directory

[MembershipWorks](https://membershipworks.com/) is membership-management software that chambers, trade groups, and nonprofits embed into their own website — on WordPress, Squarespace, Weebly, Wix, Duda, or a custom HTML5 site — to run memberships, events, and a searchable **member directory**. Unlike a platform that hosts every customer on one shared domain, a MembershipWorks directory usually lives on the association's *own* domain, styled to match the rest of that site.

The directory is a common target for anyone trying to build a list of an association's members, sponsors, or contacts: sales teams, researchers, journalists, other associations doing market comparisons, and members themselves. The usual first question is simple — *"how do I export this?"* The honest answer depends on who you are. MembershipWorks ships a real export tool, but it's an **administrator tool** reached only after logging into that specific organization's MembershipWorks dashboard. If you are not that administrator and the association hasn't given you a file, your options are narrower, and this guide is about using them correctly.

This guide is scoped to one situation: **a public MembershipWorks directory that has no export offered to you**, and how to collect the visible, unauthenticated part of it responsibly. It assumes you already understand the general legal and quality issues around directory-sourced leads; for that broader treatment across multiple association-management platforms, see [chamber-association-lead-lists](https://github.com/willowridge1234/chamber-association-lead-lists), a companion guide from the same authors. Sibling guides cover the same situation on [Wild Apricot](https://github.com/willowridge1234/wild-apricot-directory-export-guide) and [MemberClicks](https://github.com/willowridge1234/memberclicks-directory-export-guide).

**Commercial disclosure:** Rook Data Tools publishes a purpose-built MembershipWorks Directory Scraper on the Apify platform — **that's our own commercial product, priced pay-per-event, and running it costs money.** It's linked once, in the "Where the actor fits" section below, and it is not an independent recommendation. Every other section of this guide stands on its own whether you end up collecting a handful of records by hand, get an export from the association directly, or use a tool — ours or anyone else's.

## Who this is for

- A salesperson or founder who wants a lead list of a MembershipWorks-hosted association's public members.
- A researcher, journalist, or comparison shopper who needs a defensible snapshot of a public membership roster.
- An association staffer evaluating a *different* association's public directory, who doesn't have (and shouldn't ask for) that association's own admin login.
- Anyone who looked for the obvious "export" button and found it either doesn't exist for them or sits behind a login they don't have.

This guide does not cover accessing your own association's data as its administrator — MembershipWorks' own help documentation already covers that — and it does not cover accessing any member-only or login-gated area under any circumstance.

## First, recognize a MembershipWorks site

Confirm you're actually looking at a MembershipWorks directory before assuming anything about export options or rules, since those differ by platform, and MembershipWorks gives you fewer visual cues than a vendor-hosted platform would.

Because MembershipWorks embeds into the association's own WordPress, Squarespace, Weebly, Wix, Duda, or custom site rather than a shared `*.membershipworks.com`-style domain, there's no single hosted URL pattern to look for. Instead, look for explicit attribution: "MembershipWorks" mentioned in the site footer, on the member sign-in screen, in an "About this site" or account-management link, or in page source references to the vendor. If none of that is present and the directory still looks similar to what's described below, record the platform as unknown rather than guessing from layout — several association-management platforms produce a broadly similar searchable-directory experience.

## Why the built-in export usually isn't available to you

MembershipWorks' own materials describe an export path built for organization administrators: from the admin dashboard, an admin opens the accounts list, filters it by text search, label, or membership level, and exports or emails the resulting set — described as useful "to backup all your membership information if you want to keep a local copy." That tool lives entirely inside the organization's own logged-in dashboard.

MembershipWorks also offers an OAuth 2.0 single-sign-on integration, but it is not a general-purpose directory API — it exists so an authenticated *member* can log into a separate third-party application (a forum, a learning-management system) using their MembershipWorks account, and it returns that one member's own profile data to the application they're signing into, not a bulk directory feed to an outside developer.

If you are not that association's administrator, neither tool exists for you, no matter how the directory looks from the outside. Three honest paths follow:

1. **Ask.** If your use case is legitimate — a partnership, a sponsorship, a research project — ask the association directly for an export or an introduction. This is the only path that can also get you fields the public page doesn't show, and many associations will say yes to a clearly stated, reasonable request.
2. **Use whatever the association already published for visitors.** Some associations post a public roster, PDF list, or downloadable file outside any login. Check the directory page and its FAQ/help links before assuming none exists.
3. **Collect only what the public directory page already displays to any visitor**, without logging in, if neither of the above applies and the site's own rules allow it. The rest of this guide is about doing that third path correctly and knowing when not to.

## What a public MembershipWorks directory may show — and what it won't

There is no single MembershipWorks record format. The admin builds the directory profile template themselves — organizing member information into tabs and boxes (contact details, maps, galleries, deals, social links, labels) using a drag-and-drop editor — so the fields present, and their layout, vary from one association's site to the next. An admin also decides, per membership level, whether that level's members are listed in the directory at all, and can configure the directory to automatically drop a member's listing a set number of days after they go past due on dues.

On top of the admin's template, **individual visibility is layered per member.** MembershipWorks documents a set of member-level privacy toggles: "Do not list in directory" removes the member's listing entirely regardless of the admin's settings, and separate toggles let a member hide their street address, phone, mobile number, or contact name specifically, while still appearing in the directory otherwise. MembershipWorks also does not display a member's email address on the public directory profile by default — it's deliberately withheld to reduce address harvesting. A directory you can see, in other words, is already the association's and its members' filtered view, not the full membership database.

### Fields commonly visible on a public profile, when the association and member have both chosen to show them

- business or member name, and a logo or profile photo;
- a short tagline or profile description;
- contact person's name, when not hidden;
- category, label, or membership-level tag;
- phone or mobile number, when not hidden;
- a street address or general location, when not hidden;
- a website link and social profile links;
- a map marker tied to the member's location;
- additional locations or contacts, for members with more than one;
- any deals or offers the member has chosen to publish.

### What a public directory almost never gives you

- an email address — MembershipWorks withholds it from the public profile by default;
- anything behind the member login — private profile fields, member-only deals, event rosters, invoices, or renewal status;
- fields an admin's template omits, or a member individually chose to hide;
- reliable revenue, headcount, budget, or purchasing authority;
- confirmation that a named contact still holds that role;
- confirmation that a displayed phone number is actively monitored;
- current buying intent, timing, or need — membership is not a purchase signal;
- the organization's underlying export files or admin-dashboard data.

Treat an empty field as "not shown to the public," not as evidence the association has no such information. Don't fill gaps with guesses.

## The line that matters: public directory vs. member-only area

MembershipWorks lets an organization make its directory fully public, fully member-only, or a mix — the same admin tooling that restricts an event page or a resource page to logged-in members can restrict the directory itself, or specific tabs within a member's profile, to a chosen membership level.

- **In scope:** whatever a directory page shows to an ordinary visitor with no account, no payment, no invitation link, and no bypass of any access control.
- **Out of scope, always:** anything that requires signing in as a member, requesting member access, using someone else's credentials, or working around a login wall, a paywall, or a bot challenge. If the only way to see a field is to be a logged-in member, that field is not part of a public collection — full stop, regardless of how the field is displayed once you're inside.

This guide, and the actor linked below, only address the case where the directory page itself is genuinely reachable without logging in.

## Whose policies actually govern the data

This is the same trap that applies on every association-management platform built this way: **the software vendor's privacy policy is not the association's privacy policy.** MembershipWorks describes itself as a data *processor* acting on the organization's instructions, with the organization itself as the data *controller* responsible for its members' privacy under GDPR and similar laws — meaning the operative rules for a specific directory live on that association's own site, under its own privacy policy and terms of use, not on membershipworks.com. Read the association's own pages before deciding what's appropriate.

## Respect the site's own rules, robots.txt, and rate limits

This section is operational guidance, not legal advice, and applies to any public directory, not just MembershipWorks'.

- Read the association's terms of use and privacy notice for that specific site before collecting anything, and don't proceed if they prohibit your intended use.
- Check the site's `robots.txt`. The [Robots Exclusion Protocol](https://www.rfc-editor.org/rfc/rfc9309.html) is the standard way a site communicates crawler access preferences. Because a MembershipWorks directory is embedded on the association's own hosting platform — WordPress, Squarespace, Wix, Weebly, Duda, or a custom build — there is no single MembershipWorks-wide default to check; read the `robots.txt` for that specific site, since it reflects that host's own configuration, not a MembershipWorks-wide policy.
- The directory content itself typically loads into the page dynamically rather than sitting in the initial page source — view what an ordinary visitor's browser actually renders, not a raw fetch of the page's HTML, before assuming a field is or isn't present.
- Keep any automated request volume conservative regardless of what a platform default allows, and stop or slow down at the first sign of rate-limit responses, errors, or strain on the site. Never rotate identities, defeat bot challenges, or retry aggressively to push past a block.
- Never attempt to reach anything behind the member login, under any framing — that includes borrowing a member's credentials, joining specifically to reach non-public data, or treating "visible after I log in" as if it were public.

## Preserve provenance

A directory-sourced record is only as trustworthy as its documented source. For every record, keep:

- the exact profile URL, when the directory links to individual profile pages;
- the association's name and the specific site domain the directory was embedded on (note that it's rarely a `membershipworks.com` address — see "First, recognize a MembershipWorks site" above);
- the date and time you collected it;
- the raw values as displayed, before any cleanup or normalization;
- which membership level, label, or category the record appeared under.

If the association later migrates platforms or reconfigures its directory, that provenance note is also what tells you why a later collection looks structurally different.

## Deduplicating MembershipWorks-sourced records

Full deduplication method is covered in the [companion cross-platform guide](https://github.com/willowridge1234/chamber-association-lead-lists#how-to-clean-and-deduplicate-a-directory-sourced-list); MembershipWorks has one structural wrinkle worth knowing before you start. A single member account can list **multiple locations or multiple contacts** under one profile — a multi-branch business or a firm with several staff members can appear as one account with several attached rows rather than one row per row of information. Decide up front whether your list unit is the account or the individual location/contact, and don't silently treat a multi-location account's branches as unrelated duplicates, or collapse them into one row when your use case actually needs them separate.

This repository ships a small, generic offline tool for the cleaning step: [`scripts/clean_dedupe.py`](scripts/clean_dedupe.py). It normalizes whitespace, casing, phone formatting, and website domains for comparison while preserving the original raw values. It flags rows for review when they share a website domain, or when both normalized business name and phone match. A shared domain alone is enough to create a review group: in association directories, one firm often lists several contacts or locations under the same domain. That is a deliberately broad default for human review, not proof that the rows are duplicates, and the tool never merges or deletes them. Matching signals are treated transitively, so rows connected through a chain of matches appear in one review group. The tool works on any directory-shaped CSV — it has no MembershipWorks-specific logic and doesn't know or care how the rows were collected. See [`sample-data/example-directory-export.csv`](sample-data/example-directory-export.csv) for a fictional example input in the shape this guide describes (every organization, person, address, and phone number in that file is invented for illustration and does not correspond to any real association or member).

As with any directory source: keep the raw values, use more than one identity signal before merging two records, and don't merge accounts just because they share a category or membership level.

## When automation is the wrong call

Don't automate collection of a MembershipWorks directory when:

- the directory, or the fields you actually need, sits behind a member login;
- the site's terms, robots.txt, or an explicit request from the association say no;
- the directory is small enough to review and copy by hand in a few minutes — a script adds risk for no real benefit;
- what you actually need is verified, current, or private information no public profile will ever contain — the honest fix is asking the association, not scraping harder;
- the association has already told you no, or you have a live relationship where simply asking is faster and cleaner.

Automation is a convenience for the *public, at-scale, repetitive* case. It is never a workaround for a login wall or a "no."

## Where the actor fits

If you've confirmed the site's directory runs on MembershipWorks, confirmed it's genuinely public with no login required to view it, and checked the association's own terms and `robots.txt`, we publish the [MembershipWorks Directory Scraper](https://apify.com/rook-data-tools/membershipworks-directory-scraper?utm_source=github&utm_medium=referral&utm_campaign=membershipworks-member-directory-export-guide) on Apify for exactly that job. **To be direct about the commercial part: this is our own paid product. It runs pay-per-event on Apify — a small charge to start a run plus a small charge per member record actually extracted — so check the listing itself for current pricing before running it, since pricing can change.**

What it does, plainly, per its current public Apify listing: it crawls public MembershipWorks member directories and turns visible listings into structured records — business name, contact person, phone, fax, website, full address, location, category, and profile URL, output as JSON, CSV, or Excel-ready data. It only works against directories that are reachable without logging in; it has no path into a member login, and it isn't built or intended to reach anything behind one.

In the interest of not overselling a new listing: it is new, has no reviews yet, and we don't have independent evidence of how many people have used it beyond ourselves. Judge it on the Apify listing's own current stats and a small test run against a directory you already understand, not on anything claimed here.

We don't publish how it identifies or reaches directory data — consistent with the rest of this guide, the goal is a described outcome, not a technique write-up.

## Final checklist

Before collecting anything from a MembershipWorks directory:

- [ ] Confirmed the site is actually MembershipWorks, from visible evidence, or marked it unknown — including that it's likely embedded on the association's own domain, not a `membershipworks.com` address.
- [ ] Checked whether the association would simply provide an export if asked.
- [ ] Confirmed the specific page and fields you want are visible to an ordinary visitor with no login.
- [ ] Read that association's own terms of use and privacy notice — not MembershipWorks' vendor-level policy — and confirmed nothing there prohibits your use.
- [ ] Checked that specific site's `robots.txt` and treated it as a floor, not a green light.
- [ ] Planned conservative request volume and a stop condition if the site shows any strain.
- [ ] Decided your list unit (account vs. individual location/contact) before collecting, given MembershipWorks' multi-location/multi-contact accounts.
- [ ] Have a plan to preserve profile URL, association name, membership level/category, and collection date per record.
- [ ] Ruled out that what you actually need is private, member-only, or unverifiable from a public profile (starting with email, which MembershipWorks withholds from public profiles by default).

## Frequently asked questions

### Can I export a MembershipWorks member directory as an outside visitor?

Not through MembershipWorks' built-in export tool — it's reached only through an association administrator's own logged-in dashboard. If the association hasn't offered you a file and the directory is genuinely public, you're limited to collecting what an ordinary visitor can already see on the page, subject to the site's own terms and robots.txt.

### Does MembershipWorks have a public API for member directories?

MembershipWorks offers an OAuth 2.0 single-sign-on integration, but it authenticates one logged-in member into a separate third-party application and returns that member's own profile — it isn't a bulk or public API for an outside party to query another association's directory data.

### What information is public on a MembershipWorks directory?

It depends entirely on how that association built its directory profile template and how each individual member set their own privacy toggles — there's no single MembershipWorks record shape. Commonly public fields include member/business name, category, location, phone, website, and a profile description; email is withheld from the public profile by default, and anything a member marked hidden won't appear.

### Is scraping a public MembershipWorks directory legal?

There's no universal answer, and this isn't legal advice. Staying outside any login wall, respecting the association's own terms and `robots.txt`, keeping request volume conservative, and using only what's already visible to an ordinary visitor are the baseline conditions. Separately, collecting a public business contact doesn't by itself authorize marketing to it — see the FTC's [CAN-SPAM compliance guide](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business) for US email rules and the UK ICO's [business-to-business marketing guidance](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/) for a jurisdiction where B2B rules differ from consumer rules. Get legal advice for a high-risk or large-scale use.

### Why isn't MembershipWorks' privacy policy the one that governs this data?

Because MembershipWorks is the software vendor acting as a data processor, not the data controller. Its own materials describe the customer organization as responsible for its members' data and privacy under GDPR and similar laws — so the operative rules for a specific directory live on the association's own site.

### Why can't I see anyone's email address on the directory?

MembershipWorks withholds member email addresses from the public directory profile by default, specifically to reduce address harvesting. If you need to reach a member and no email is shown, look for a published phone number, website, or contact form instead, or ask the association to pass along a message.

## The useful standard

A responsibly collected MembershipWorks directory export is not the biggest file you can pull. It's a traceable set of the records that association actually chose to make public, collected without touching anything behind its member login, respecting its own rules, and honest about what it can and can't tell you about intent, timing, or authority. If you need more than that, the association — not a workaround — is the right next step.

## Related

Other free workflows and guides we publish:

- [n8n-ai-lead-scoring](https://github.com/willowridge1234/n8n-ai-lead-scoring) — Free workflow — score scraped leads against your ICP, log to Google Sheets
- [n8n-review-intent-lead-scoring](https://github.com/willowridge1234/n8n-review-intent-lead-scoring) — Free workflow — score G2/Capterra reviewers by switching intent
- [n8n-tradeshow-exhibitor-lead-scoring](https://github.com/willowridge1234/n8n-tradeshow-exhibitor-lead-scoring) — Free workflow — score trade-show exhibitors against your ICP
- [n8n-lead-scoring-guide](https://github.com/willowridge1234/n8n-lead-scoring-guide) — Guide — which signals predict a good lead, and how to tell if scoring works
- [chamber-association-lead-lists](https://github.com/willowridge1234/chamber-association-lead-lists) — Guide — building B2B lead lists from chamber & association directories
- [memberclicks-directory-export-guide](https://github.com/willowridge1234/memberclicks-directory-export-guide) — Guide — exporting a public MemberClicks member directory
- [new-liquor-license-data-guide](https://github.com/willowridge1234/new-liquor-license-data-guide) — Guide + tool — building a lead list from public liquor-licence records
- [chicago-food-service-license-data-guide](https://github.com/willowridge1234/chicago-food-service-license-data-guide) — Guide + tool — building a lead list from Chicago food-service licence records
- [wild-apricot-directory-export-guide](https://github.com/willowridge1234/wild-apricot-directory-export-guide) — Guide — exporting a public Wild Apricot member directory
- [chambermaster-directory-export-guide](https://github.com/willowridge1234/chambermaster-directory-export-guide) — Guide — exporting a public ChamberMaster or GrowthZone member directory
