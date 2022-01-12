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

