#!/usr/bin/env python3

import unittest

from p1 import (
    parse_input,
    calc_fuel_to_position,
)


class TestProblemOne(unittest.TestCase):
    def test_parse_intput(self):
        filename = "input-sample.txt"
        with open(filename) as f:
            input = f.readlines()

        expected_buckets = {0: 1, 1: 2, 2: 3, 3: 0, 4: 1, 5: 0, 6: 0, 7: 1, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 1, 15: 0, 16: 1}
        crab_buckets = parse_input(input=input)
        self.assertEqual(crab_buckets, expected_buckets)

    def test_calc_fuel_to_position(self):
        filename = "input-sample.txt"
        with open(filename) as f:
            input = f.readlines()

        crab_buckets = parse_input(input=input)
        self.assertEqual(calc_fuel_to_position(crabs=crab_buckets, position=2), 37)
        self.assertEqual(calc_fuel_to_position(crabs=crab_buckets, position=1), 41)
        self.assertEqual(calc_fuel_to_position(crabs=crab_buckets, position=3), 39)
        self.assertEqual(calc_fuel_to_position(crabs=crab_buckets, position=10), 71)


if __name__ == "__main__":
    unittest.main()
