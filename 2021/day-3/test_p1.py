#!/usr/bin/env python

import unittest

from p1 import get_most_common_bit, get_least_common_bit, calculate_gamma_rate_binary


class TestProblemOne(unittest.TestCase):
    def test_get_most_common_bit(self):
        """
        Get most common bits for each column from a sample diagnostic report
        """
        filename = "input-sample.txt"
        with open(filename) as f:
            report = f.readlines()

        self.assertEqual(get_most_common_bit(diagnostic_report=report, position=0), 1)
        self.assertEqual(get_most_common_bit(diagnostic_report=report, position=1), 0)
        self.assertEqual(get_most_common_bit(diagnostic_report=report, position=2), 1)
        self.assertEqual(get_most_common_bit(diagnostic_report=report, position=3), 1)
        self.assertEqual(get_most_common_bit(diagnostic_report=report, position=4), 0)

    def test_get_least_common_bit(self):
        """
        Get least common bits for each column from a sample diagnostic report
        """
        filename = "input-sample.txt"
        with open(filename) as f:
            report = f.readlines()

        self.assertEqual(get_least_common_bit(diagnostic_report=report, position=0), 0)
        self.assertEqual(get_least_common_bit(diagnostic_report=report, position=1), 1)
        self.assertEqual(get_least_common_bit(diagnostic_report=report, position=2), 0)
        self.assertEqual(get_least_common_bit(diagnostic_report=report, position=3), 0)
        self.assertEqual(get_least_common_bit(diagnostic_report=report, position=4), 1)


if __name__ == "__main__":
    unittest.main()
