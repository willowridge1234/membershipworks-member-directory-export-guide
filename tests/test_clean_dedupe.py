#!/usr/bin/env python3
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from clean_dedupe import (  # noqa: E402
    build_groups,
    normalize_domain,
    normalize_name,
    normalize_phone,
)


class NormalizeTests(unittest.TestCase):
    def test_normalize_name_strips_suffix_and_case(self):
        self.assertEqual(normalize_name("Example Harbor Roofing Co"), "example harbor roofing")
        self.assertEqual(normalize_name("Example Harbor Roofing Company"), "example harbor roofing")

    def test_normalize_domain_strips_protocol_and_www(self):
        self.assertEqual(normalize_domain("http://www.exampleharborroofing.example"), "exampleharborroofing.example")
        self.assertEqual(normalize_domain("www.exampleharborroofing.example"), "exampleharborroofing.example")
        self.assertEqual(normalize_domain("https://fictionalgrovebakery.example"), "fictionalgrovebakery.example")

    def test_normalize_phone_strips_formatting(self):
        self.assertEqual(normalize_phone("555-0101"), "5550101")
        self.assertEqual(normalize_phone("(555) 010-1"), "5550101")


class GroupingTests(unittest.TestCase):
    def test_shared_domain_groups_rows(self):
        rows = [
            {"business_name": "Example Harbor Roofing Co", "phone": "555-0101", "website": "http://www.exampleharborroofing.example"},
            {"business_name": "Example Harbor Roofing Company", "phone": "(555) 010-1", "website": "www.exampleharborroofing.example"},
            {"business_name": "Unrelated Fictional Co", "phone": "555-0999", "website": "https://unrelatedfictional.example"},
        ]
        assignment = build_groups(rows)
        self.assertIn(0, assignment)
        self.assertIn(1, assignment)
        self.assertNotIn(2, assignment)
        self.assertEqual(assignment[0][0], assignment[1][0])

    def test_shared_domain_alone_groups_different_names_and_phones(self):
        rows = [
            {"business_name": "Alpha Example LLC", "phone": "555-0101", "website": "https://shared.example"},
            {"business_name": "Beta Sample LLC", "phone": "555-0102", "website": "https://shared.example"},
        ]
        assignment = build_groups(rows)
        self.assertEqual(assignment[0][0], assignment[1][0])
        self.assertIn("matching website domain", assignment[0][1])

    def test_bridge_edges_form_one_transitive_group(self):
        rows = [
            {"business_name": "Alpha Example LLC", "phone": "555-0101", "website": "https://x.example"},
            {"business_name": "Bridge Example LLC", "phone": "555-0102", "website": "https://x.example"},
            {"business_name": "Bridge Example LLC", "phone": "555-0102", "website": "https://y.example"},
            {"business_name": "Omega Example LLC", "phone": "555-0103", "website": "https://y.example"},
        ]
        assignment = build_groups(rows)
        self.assertEqual(set(assignment), {0, 1, 2, 3})
        self.assertEqual({group_id for group_id, _reason in assignment.values()}, {1})

    def test_no_false_group_across_unrelated_rows(self):
        rows = [
            {"business_name": "Alpha Example Inc", "phone": "555-1000", "website": "https://alphaexample.example"},
            {"business_name": "Beta Sample LLC", "phone": "555-2000", "website": "https://betasample.example"},
        ]
        assignment = build_groups(rows)
        self.assertEqual(assignment, {})


if __name__ == "__main__":
    unittest.main()
