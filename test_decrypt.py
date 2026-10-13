"""Unit tests for the decrypt function."""

import unittest

from decrypt import decrypt


class DecryptTestCase(unittest.TestCase):
    """Test cases for the decrypt function."""

    def test_remove_single_dot(self):
        self.assertEqual(decrypt("a.b"), "ab")

    def test_remove_multiple_dots(self):
        self.assertEqual(decrypt("a.b.c.d"), "abcd")

    def test_remove_only_dots(self):
        self.assertEqual(decrypt("..."), "")

    def test_text_without_dots(self):
        self.assertEqual(decrypt("hello"), "hello")

    def test_empty_string(self):
        self.assertEqual(decrypt(""), "")

    def test_multiple_cases_with_subtest(self):
        cases = [
            ("a.b", "ab"),
            ("...", ""),
            ("abc", "abc"),
            ("one.two.three", "onetwothree"),
        ]

        for given, expected in cases:
            with self.subTest(given=given):
                self.assertEqual(decrypt(given), expected)


if __name__ == "__main__":
    unittest.main()
