#!/usr/bin/env python3
"""
Generic cleaning/dedup helper for directory-shaped CSV exports.

Takes any CSV with roughly these columns (extra or missing columns are fine):
  business_name, contact_person, phone, website, address, city, region,
  postal_code, category, profile_url

It does not know or care where the CSV came from. It normalizes a few fields
for comparison, groups rows that share a strong identity signal (matching
website domain, or matching normalized name + phone), and reports each group
for a human to decide whether it's one account, a duplicate, or genuinely
separate locations/contacts under the same account. It never merges or
deletes rows itself -- every original row is preserved in the output.

Usage:
    python3 clean_dedupe.py input.csv output.csv
"""

import csv
import re
import sys

LEGAL_SUFFIXES = (
    "llc", "l.l.c", "inc", "inc.", "incorporated", "co", "co.", "company",
    "corp", "corp.", "corporation", "llp", "l.l.p", "ltd", "ltd.", "limited",
    "pllc", "pc", "p.c",
)


def normalize_name(name):
    name = (name or "").strip().lower()
    name = re.sub(r"[^\w\s&-]", " ", name)
    tokens = [t for t in name.split() if t]
    while tokens and tokens[-1].strip(".") in LEGAL_SUFFIXES:
        tokens.pop()
    return " ".join(tokens)


def normalize_domain(website):
    website = (website or "").strip().lower()
    if not website:
        return ""
    website = re.sub(r"^https?://", "", website)
    website = re.sub(r"^www\.", "", website)
    website = website.split("/")[0]
    return website


def normalize_phone(phone):
    digits = re.sub(r"\D", "", phone or "")
    if len(digits) == 11 and digits.startswith("1"):
        digits = digits[1:]
    return digits


def load_rows(path):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader), reader.fieldnames or []


def build_groups(rows):
    """Return a dict mapping row index -> (group_key, reason)."""
    by_domain = {}
    by_name_phone = {}
    for i, row in enumerate(rows):
        domain = normalize_domain(row.get("website", ""))
        name = normalize_name(row.get("business_name", ""))
        phone = normalize_phone(row.get("phone", ""))
        if domain:
            by_domain.setdefault(domain, []).append(i)
        if name and phone:
            by_name_phone.setdefault((name, phone), []).append(i)

    assignment = {}
    next_group_id = 1

    def assign(indices, reason):
        nonlocal next_group_id
        existing = {assignment[i][0] for i in indices if i in assignment}
        if existing:
            group_id = sorted(existing)[0]
        else:
            group_id = next_group_id
            next_group_id += 1
        for i in indices:
            assignment[i] = (group_id, reason)

    for domain, indices in by_domain.items():
        if len(indices) > 1:
            assign(indices, f"matching website domain ({domain})")

    for (name, phone), indices in by_name_phone.items():
        if len(indices) > 1:
            assign(indices, f"matching normalized name + phone ({name!r}, {phone})")

    return assignment


def main():
    if len(sys.argv) != 3:
        print(f"usage: {sys.argv[0]} input.csv output.csv", file=sys.stderr)
        return 2

    in_path, out_path = sys.argv[1], sys.argv[2]
    rows, fieldnames = load_rows(in_path)
    assignment = build_groups(rows)

    group_counts = {}
    for group_id, _reason in assignment.values():
        group_counts[group_id] = group_counts.get(group_id, 0) + 1

    out_fields = list(fieldnames) + [
        "normalized_name",
        "normalized_domain",
        "normalized_phone",
        "duplicate_group_id",
        "duplicate_group_size",
        "duplicate_review_reason",
    ]

    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=out_fields)
        writer.writeheader()
        for i, row in enumerate(rows):
            out_row = dict(row)
            out_row["normalized_name"] = normalize_name(row.get("business_name", ""))
            out_row["normalized_domain"] = normalize_domain(row.get("website", ""))
            out_row["normalized_phone"] = normalize_phone(row.get("phone", ""))
            if i in assignment:
                group_id, reason = assignment[i]
                out_row["duplicate_group_id"] = group_id
                out_row["duplicate_group_size"] = group_counts[group_id]
                out_row["duplicate_review_reason"] = reason
            else:
                out_row["duplicate_group_id"] = ""
                out_row["duplicate_group_size"] = 1
                out_row["duplicate_review_reason"] = ""
            writer.writerow(out_row)

    flagged = sum(1 for i in range(len(rows)) if i in assignment)
    print(f"{len(rows)} rows read, {flagged} flagged into {len(group_counts)} review group(s).")
    print("Nothing was merged or deleted -- review each group and decide manually.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
