#!/usr/bin/env python3

import unittest

from p1 import (
    parse_input,
    check_board_for_match,
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
        expected_boards = [
            [
                ["22", "13", "17", "11", "0"],
                ["8", "2", "23", "4", "24"],
                ["21", "9", "14", "16", "7"],
                ["6", "10", "3", "18", "5"],
                ["1", "12", "20", "15", "19"],
            ],
            [
                ["3", "15", "0", "2", "22"],
                ["9", "18", "13", "17", "5"],
                ["19", "8", "7", "25", "23"],
                ["20", "11", "10", "24", "4"],
                ["14", "21", "16", "12", "6"],
            ],
            [
                ["14", "21", "17", "24", "4"],
                ["10", "16", "15", "9", "19"],
                ["18", "8", "23", "26", "20"],
                ["22", "11", "13", "6", "5"],
                ["2", "0", "12", "3", "7"],
            ],
        ]

        parsed_input = parse_input(input=input)

        self.assertEqual(parsed_input[0], expected_draws)
        self.assertEqual(parsed_input[1], expected_boards)

    def test_check_board_for_match_with_match(self):
        """
        Test input parsing to get draws and boards
        """

        board = [
            ["22", "13", "17", "11", "0"],
            ["8", "2", "23", "4", "24"],
            ["21", "9", "14", "16", "7"],
            ["6", "10", "3", "18", "5"],
            ["1", "12", "20", "15", "19"],
        ]

        self.assertEqual(
            check_board_for_match(board=board, item="23"),
            (
                1,
                2,
            ),
        )

        self.assertEqual(
            check_board_for_match(board=board, item="5"),
            (
                3,
                4,
            ),
        )

    def test_check_board_for_match_with_match(self):
        """
        Test input parsing to get draws and boards
        """

        board = [
            ["22", "13", "17", "11", "0"],
            ["8", "2", "23", "4", "24"],
            ["21", "9", "14", "16", "7"],
            ["6", "10", "3", "18", "5"],
            ["1", "12", "20", "15", "19"],
        ]

        self.assertIsNone(check_board_for_match(board=board, item="99"))


if __name__ == "__main__":
    unittest.main()
