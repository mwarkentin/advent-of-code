#!/usr/bin/env python

import unittest

from p1 import count_depth_changes


class TestCountDepthChanges(unittest.TestCase):
    def test_count_depth_changes(self):
        """
        Test that it can sum a list of integers
        """
        data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        expected_result = {"decreased": 2, "increased": 7, "no_change": 0}
        result = count_depth_changes(data)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
