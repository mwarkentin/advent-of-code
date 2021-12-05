#!/usr/bin/env python

import unittest

from p2 import (
    get_most_common_bit,
    get_least_common_bit,
    filter_report,
    get_oxygen_generator_rating,
    get_co2_scrubber_rating,
    get_life_support_rating,
)


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

    def test_filter_report(self):
        filename = "input-sample.txt"
        with open(filename) as f:
            report = f.readlines()

        self.assertEqual(
            filter_report(report, "1", 0),
            [
                "11110",
                "10110",
                "10111",
                "10101",
                "11100",
                "10000",
                "11001",
            ],
        )

        self.assertEqual(
            filter_report(report, "0", 1),
            [
                "00100",
                "10110",
                "10111",
                "10101",
                "00111",
                "10000",
                "00010",
            ],
        )

    def test_get_oxygen_generator_rating(self):
        filename = "input-sample.txt"
        with open(filename) as f:
            report = f.readlines()

        self.assertEqual(get_oxygen_generator_rating(report, 0), "10111")

    def test_get_co2_scrubber_rating(self):
        filename = "input-sample.txt"
        with open(filename) as f:
            report = f.readlines()

        self.assertEqual(get_co2_scrubber_rating(report, 0), "01010")

    def test_get_life_support_rating_sample(self):
        filename = "input-sample.txt"
        with open(filename) as f:
            report = f.readlines()

        self.assertEqual(get_life_support_rating(report), 230)

    def test_get_life_support_rating_full(self):
        filename = "input.txt"
        with open(filename) as f:
            report = f.readlines()

        self.assertEqual(get_life_support_rating(report), 4267809)


if __name__ == "__main__":
    unittest.main()
