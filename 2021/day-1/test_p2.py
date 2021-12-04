#!/usr/bin/env python

import unittest

from p2 import count_depth_changes, get_sliding_window


class TestCountDepthChanges(unittest.TestCase):
    def test_count_depth_changes(self):
        """ """
        data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        expected_result = {"decreased": 1, "increased": 5, "no_change": 1}
        result = count_depth_changes(data)
        self.assertEqual(result, expected_result)


class TestGetSlidingWindow(unittest.TestCase):
    def test_get_full_sliding_window(self):
        """ """
        data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        result = get_sliding_window(depths=data, index=0)
        self.assertEqual(result, 607)
        result = get_sliding_window(depths=data, index=1)
        self.assertEqual(result, 618)

    def test_get_sliding_window_too_big(self):
        """ """
        data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        self.assertRaises(ValueError, get_sliding_window, depths=data, index=8)


if __name__ == "__main__":
    unittest.main()
