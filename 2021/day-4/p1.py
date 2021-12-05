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
        board = [row.strip().split() for row in input[start_row:end_row]]
        boards.append(board)

    print("boards:")
    pprint(boards)

    return draws, boards


def check_board_for_match(board, item):
    for row, board_row in enumerate(board):
        for col, value in enumerate(board_row):
            if int(value) == item:
                return (row, col)

def play_bingo(input):
    print("Time to play some.... BINGO!")
    draws, boards = parse_input(input)

    for draw in draws:
        print(f"Ball drawn: {draw}")
        for count, board in enumerate(boards):
            match = check_board_for_match(board=board, item=draw)
            if match is not None:
                print(f"Match on {draw} found for board {count} at {match[0]},{match[1]}")
