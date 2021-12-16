#!/usr/bin/env python3

import unittest

from p2 import (
    parse_input,
    calc_fuel_to_position,
    find_lowest_fuel_cost,
)


class TestProblemOne(unittest.TestCase):
    def test_parse_intput(self):
        filename = "input-sample.txt"
        with open(filename) as f:
            input = f.readlines()

        expected_buckets = {
            0: 1,
            1: 2,
            2: 3,
            3: 0,
            4: 1,
            5: 0,
            6: 0,
            7: 1,
            8: 0,
            9: 0,
            10: 0,
            11: 0,
            12: 0,
            13: 0,
            14: 1,
            15: 0,
            16: 1,
        }
        crab_buckets, _ = parse_input(input=input)
        self.assertEqual(crab_buckets, expected_buckets)

    def test_calc_fuel_to_position(self):
        filename = "input-sample.txt"
        with open(filename) as f:
            input = f.readlines()

        crab_buckets, _ = parse_input(input=input)
        self.assertEqual(calc_fuel_to_position(crabs=crab_buckets, position=2), 206)
        self.assertEqual(calc_fuel_to_position(crabs=crab_buckets, position=5), 168)

    def test_find_lowest_fuel_cost_sample(self):
        filename = "input-sample.txt"
        with open(filename) as f:
            input = f.readlines()

        crab_buckets, max_x = parse_input(input=input)
        self.assertEqual(find_lowest_fuel_cost(crabs=crab_buckets, max_x=max_x), 168)

    def test_find_lowest_fuel_cost_full(self):
        filename = "input.txt"
        with open(filename) as f:
            input = f.readlines()

        crab_buckets, max_x = parse_input(input=input)
        self.assertEqual(
            find_lowest_fuel_cost(crabs=crab_buckets, max_x=max_x), 94813675
        )


if __name__ == "__main__":
    unittest.main()
