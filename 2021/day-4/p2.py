#!/usr/bin/env python3

from pprint import pprint


def parse_input(input):
    lines = input.rstrip().split("\n\n")
    print(lines)
    draws = [int(x) for x in lines[0].split(",")]

    boards = []
    num_boards = (len(lines) - 1)
    print(f"number of boards: {num_boards}")

    for line in lines[1:]:
        board = [row.split() for row in line.split("\n")]
        print(board)
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
    winning_boards = set()
    for draw in draws:
        print(f"Ball drawn: {draw}")
        for count, board in enumerate(boards):
            match = check_board_for_match(board=board, item=draw)
            if match is not None:
                print(
                    f"Match on {draw} found for board {count} at {match[0]},{match[1]}"
                )
                # Set position to 0 to track matches since we only care about unmatched positions
                board[match[0]][match[1]] = 0
                winner = check_winner(board=board)
                if winner:
                    print(f"Winner found, board {count}:")
                    pprint(board)
                    winning_boards.add(count)
                    print("Winning boards:", winning_boards)
                    print(len(winning_boards), len(boards), len(winning_boards) == len(boards))
                    if len(winning_boards) == len(boards):
                        return board, draw
    return board, draw


def sum_board(board):
    return sum(sum(board, []))


def play_bingo(input):
    print("Time to play some.... BINGO!")
    draws, boards = parse_input(input)
    print(len(draws))

    winning_board, winning_draw = draw_balls(draws=draws, boards=boards)
    if winning_board is not None:
        board_sum = sum_board(board=winning_board)
        final_score = board_sum * winning_draw
        print(f"FINAL SCORE is..... {final_score}")
    else:
        exit("No winner found...")
