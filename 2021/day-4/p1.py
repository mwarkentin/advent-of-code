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
        board = [[int(item) for item in row] for row in board]
        boards.append(board)

    print("boards:")
    pprint(boards)

    return draws, boards


def check_board_for_match(board, item):
    for row, board_row in enumerate(board):
        for col, value in enumerate(board_row):
            if int(value) == item:
                return (row, col)

def check_winner(board):
    # Check for full row
    for row in board:
        print(row)
        if not any(row):
            print("Found a FULL ROW!", row)
            return True

    # Check for full column
    for x in range(5):
        col = [row[x] for row in board]
        print(col)
        if not any(col):
            print("Found a FULL COLUMN!", col)
            return True

    return False

def draw_balls(draws, boards):
    for draw in draws:
        print(f"Ball drawn: {draw}")
        for count, board in enumerate(boards):
            match = check_board_for_match(board=board, item=draw)
            if match is not None:
                print(f"Match on {draw} found for board {count} at {match[0]},{match[1]}")
                # Set position to 0 to track matches since we only care about unmatched positions
                board[match[0]][match[1]] = 0
                winner = check_winner(board=board)
                if winner:
                    print(f"Winner found, board {count}:")
                    pprint(board)
                    return board, draw
    return None, None

def sum_board(board):
    return sum(sum(board, []))

def play_bingo(input):
    print("Time to play some.... BINGO!")
    draws, boards = parse_input(input)

    winning_board, winning_draw = draw_balls(draws=draws, boards=boards)
    if winning_board is not None:
        board_sum = sum_board(board=winning_board)
        final_score = board_sum * winning_draw
        print(f"FINAL SCORE is..... {final_score}")
    else:
        exit("No winner found...")

