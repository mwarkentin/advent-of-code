#!/usr/bin/env python3

from pprint import pprint


def parse_input(input):
    notes = []
    for line in input:
        note = [x.strip() for x in line.split(" | ")]
        notes.append(note)

    pprint(notes)
    return notes
