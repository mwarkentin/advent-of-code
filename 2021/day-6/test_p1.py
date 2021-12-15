#!/usr/bin/env python3

import unittest

from p1 import (
    parse_input,
    next_day,
    simulate_days,
    count_fish,
)


class TestProblemOne(unittest.TestCase):
    def test_parse_intput(self):
        """
        Test input parsing to get draws and boards
        """
        filename = "input-sample.txt"
        with open(filename) as f:
            input = f.readlines()

        expected_buckets = {0: 0, 1: 1, 2: 1, 3: 2, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0}
        fish_buckets = parse_input(input=input)
        self.assertEqual(fish_buckets, expected_buckets)

    def test_next_day(self):
        fish_buckets = {0: 0, 1: 1, 2: 1, 3: 2, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0}

        expected_buckets_day_1 = {0: 1, 1: 1, 2: 2, 3: 1, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
        fish_buckets = next_day(fish_buckets)
        self.assertEqual(fish_buckets, expected_buckets_day_1)

        expected_buckets_day_2 = {0: 1, 1: 2, 2: 1, 3: 0, 4: 0, 5: 0, 6: 1, 7: 0, 8: 1}
        fish_buckets = next_day(fish_buckets)
        self.assertEqual(fish_buckets, expected_buckets_day_2)

        expected_buckets_day_7 = {0: 0, 1: 1, 2: 1, 3: 3, 4: 2, 5: 2, 6: 1, 7: 0, 8: 0}
        fish_buckets = next_day(fish_buckets)
        fish_buckets = next_day(fish_buckets)
        fish_buckets = next_day(fish_buckets)
        fish_buckets = next_day(fish_buckets)
        fish_buckets = next_day(fish_buckets)
        self.assertEqual(fish_buckets, expected_buckets_day_7)

    def test_count_fish(self):
        self.assertEqual(
            count_fish(
                fish_buckets={0: 0, 1: 1, 2: 1, 3: 2, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0}
            ),
            5,
        )
        self.assertEqual(
            count_fish(
                fish_buckets={0: 1, 1: 2, 2: 1, 3: 0, 4: 0, 5: 0, 6: 1, 7: 0, 8: 1}
            ),
            6,
        )
        self.assertEqual(
            count_fish(
                fish_buckets={0: 0, 1: 1, 2: 1, 3: 3, 4: 2, 5: 2, 6: 1, 7: 0, 8: 0}
            ),
            10,
        )

    def test_simulate_days_sample(self):
        filename = "input-sample.txt"
        with open(filename) as f:
            input = f.readlines()

        fish_buckets = parse_input(input=input)
        fish_buckets = simulate_days(fish_buckets=fish_buckets, days=18)
        self.assertEqual(count_fish(fish_buckets), 26)

        fish_buckets = parse_input(input=input)
        fish_buckets = simulate_days(fish_buckets=fish_buckets, days=80)
        self.assertEqual(count_fish(fish_buckets), 5934)

        fish_buckets = parse_input(input=input)
        fish_buckets = simulate_days(fish_buckets=fish_buckets, days=256)
        self.assertEqual(count_fish(fish_buckets), 26984457539)

    def test_simulate_days_full(self):
        filename = "input.txt"
        with open(filename) as f:
            input = f.readlines()

        fish_buckets = parse_input(input=input)
        fish_buckets = simulate_days(fish_buckets=fish_buckets, days=18)
        self.assertEqual(count_fish(fish_buckets), 1565)

        fish_buckets = parse_input(input=input)
        fish_buckets = simulate_days(fish_buckets=fish_buckets, days=80)
        self.assertEqual(count_fish(fish_buckets), 352195)

        fish_buckets = parse_input(input=input)
        fish_buckets = simulate_days(fish_buckets=fish_buckets, days=256)
        self.assertEqual(count_fish(fish_buckets), 1600306001288)


if __name__ == "__main__":
    unittest.main()
