#!/usr/bin/env python3

from pprint import pprint


def parse_input(input):
    fish = [int(x) for x in input[0].split(",")]
    return fish


def next_day(fish):
    new_fish = 0
    for i, f in enumerate(fish):
        if f == 0:
            new_fish += 1
            fish[i] = 6
        else:
            fish[i] -= 1

    fish = fish + [8 for x in range(new_fish)]
    return fish


def simulate_days(fish, days):
    for day in range(days):
        fish = next_day(fish)
        print(f"{day=}, fish={len(fish)}")

    return fish
