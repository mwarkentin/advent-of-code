#!/usr/bin/env python

import unittest

from p1 import (
    parse_input,
)


class TestProblemOne(unittest.TestCase):
    def test_parse_intput(self):
        """
        Test input parsing to get draws and boards
        """
        filename = "input-sample.txt"
        with open(filename) as f:
            input = f.readlines()

        expected_draws = [
            7,
            4,
            9,
            5,
            11,
            17,
            23,
            2,
            0,
            14,
            21,
            24,
            10,
            16,
            13,
            6,
            15,
            25,
            12,
            22,
            18,
            20,
            8,
            19,
            3,
            26,
            1,
        ]
        self.assertEqual(parse_input(input=input), expected_draws)


if __name__ == "__main__":
    unittest.main()
