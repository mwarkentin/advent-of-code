#!/usr/bin/env python3

from pprint import pprint

easy_digit_segments = [2, 4, 3, 7]


def parse_input(input):
    notes = []
    for line in input:
        note = [x.strip() for x in line.split(" | ")]
        notes.append(note)
    return notes

def count_easy_digits(notes):
    easy_digits = 0
    for note in notes:
        for digit in note[1].split(" "):
            num_segments = len(digit)
            if num_segments in easy_digit_segments:
                easy_digits += 1

    return easy_digits

def decode_note(notes):
    mapping_to_combo = {}
    mapping_to_digit = {}
    for note in notes:
        for d in note[0].split(" "):
            digit = "".join(sorted(d))
            print(digit, len(digit))
            if len(digit) == 2:
                mapping_to_combo[1] = digit
                mapping_to_digit[digit] = 1

            if len(digit) == 3:
                mapping_to_combo[7] = digit
                mapping_to_digit[digit] = 7

            if len(digit) == 4:
                mapping_to_combo[4] = digit
                mapping_to_digit[digit] = 4

            if len(digit) == 7:
                mapping_to_combo[8] = digit
                mapping_to_digit[digit] = 8

    print(mapping_to_combo)
    print(mapping_to_digit)
    # for digit in note[0].split(" "):
    #     print(digit)

    # if len(digit) == 2:
    #     return 1

    # if len(digit) == 3:
    #     return 7

    # if len(digit) == 4:
    #     return 4

    # if len(digit) == 7:
    #     return 8
