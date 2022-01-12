#!/usr/bin/env python3

import unittest

from p1 import (
    parse_input,
    count_easy_digits,
)


class TestProblemOne(unittest.TestCase):
    def test_parse_intput(self):
        """
        """
        filename = "input-sample.txt"
        with open(filename) as f:
            input = f.readlines()

        expected_notes = [
            [
                "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb",
                "fdgacbe cefdb cefbgd gcbe",
            ],
            [
                "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec",
                "fcgedb cgb dgebacf gc",
            ],
            [
                "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef",
                "cg cg fdcagb cbg",
            ],
            [
                "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega",
                "efabcd cedba gadfec cb",
            ],
            [
                "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga",
                "gecf egdcabf bgf bfgea",
            ],
            [
                "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf",
                "gebdcfa ecba ca fadegcb",
            ],
            [
                "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf",
                "cefg dcbef fcge gbcadfe",
            ],
            [
                "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd",
                "ed bcgafe cdgba cbgef",
            ],
            [
                "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg",
                "gbdfcae bgc cg cgb",
            ],
            [
                "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc",
                "fgae cfgab fg bagce",
            ],
        ]

        parsed_input = parse_input(input=input)

        self.assertEqual(parsed_input, expected_notes)

    def test_count_easy_digits(self):
        """
        """
        filename = "input-sample.txt"
        with open(filename) as f:
            input = f.readlines()

        notes = parse_input(input)

        easy_digit_count = count_easy_digits(notes=notes)

        self.assertEqual(easy_digit_count, 26)

    def test_count_easy_digits_full(self):
        """
        """
        filename = "input.txt"
        with open(filename) as f:
            input = f.readlines()

        notes = parse_input(input)

        easy_digit_count = count_easy_digits(notes=notes)

        self.assertEqual(easy_digit_count, 383)


if __name__ == "__main__":
    unittest.main()
