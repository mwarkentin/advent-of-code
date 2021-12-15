#!/usr/bin/env python3

import unittest

from p1 import (
    parse_input,
    next_day,
    simulate_days,
)


class TestProblemOne(unittest.TestCase):
    def test_parse_intput(self):
        """
        Test input parsing to get draws and boards
        """
        filename = "input-sample.txt"
        with open(filename) as f:
            input = f.readlines()

        expected_fish = [3, 4, 3, 1, 2]

        parsed_input = parse_input(input=input)

        self.assertEqual(parsed_input, expected_fish)

    def test_next_day(self):
        fish = [3, 4, 3, 1, 2]

        expected_fish_day_1 = [2, 3, 2, 0, 1]
        fish = next_day(fish)

        self.assertEqual(fish, expected_fish_day_1)

        expected_fish_day_2 = [1, 2, 1, 6, 0, 8]
        fish = next_day(fish)

        self.assertEqual(fish, expected_fish_day_2)

        expected_fish_day_7 = [3, 4, 3, 1, 2, 3, 4, 5, 5, 6]
        fish = next_day(fish)
        fish = next_day(fish)
        fish = next_day(fish)
        fish = next_day(fish)
        fish = next_day(fish)

        self.assertEqual(fish, expected_fish_day_7)

        expected_fish_day_18 = [
            6,
            0,
            6,
            4,
            5,
            6,
            0,
            1,
            1,
            2,
            6,
            0,
            1,
            1,
            1,
            2,
            2,
            3,
            3,
            4,
            6,
            7,
            8,
            8,
            8,
            8,
        ]
        fish = next_day(fish)
        fish = next_day(fish)
        fish = next_day(fish)
        fish = next_day(fish)
        fish = next_day(fish)
        fish = next_day(fish)
        fish = next_day(fish)
        fish = next_day(fish)
        fish = next_day(fish)
        fish = next_day(fish)
        fish = next_day(fish)

        self.assertEqual(fish, expected_fish_day_18)

    def test_simulate_days_sample(self):
        filename = "input-sample.txt"
        with open(filename) as f:
            input = f.readlines()

        fish = parse_input(input=input)
        fish = simulate_days(fish=fish, days=18)
        self.assertEqual(len(fish), 26)

        fish = parse_input(input=input)
        fish = simulate_days(fish=fish, days=80)
        self.assertEqual(len(fish), 5934)

    def test_simulate_days_full(self):
        filename = "input.txt"
        with open(filename) as f:
            input = f.readlines()

        fish = parse_input(input=input)
        fish = simulate_days(fish=fish, days=18)
        self.assertEqual(len(fish), 1565)

        fish = parse_input(input=input)
        fish = simulate_days(fish=fish, days=80)
        self.assertEqual(len(fish), 352195)


if __name__ == "__main__":
    unittest.main()
