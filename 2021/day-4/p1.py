#!/usr/bin/env python3

from pprint import pprint


def parse_input(input):
    draws = [int(x) for x in input[0].split(",")]

    boards = []
    num_boards = (len(input) - 2) // 5
    print(f"number of boards: {num_boards}")

    for i in range(num_boards):
        start_row = 2 + 6 * i
        end_row = start_row + 5
        boards.append([row.strip().split() for row in input[start_row:end_row]])

    print("boards:")
    pprint(boards)

    return draws, boards
