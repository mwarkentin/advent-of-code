#!/usr/bin/env python3

from pprint import pprint


def parse_input(input):
    fish = [int(x) for x in input[0].split(",")]
    fish_buckets = {}

    for f in range(9):
        fish_buckets[f] = 0

    for f in fish:
        fish_buckets[f] += 1

    print(f"{fish}, {fish_buckets}")
    return fish_buckets


def next_day(fish_buckets):
    new_fish_buckets = {}
    for f in range(9):
        try:
            new_fish_buckets[f] = fish_buckets[f + 1]
        except KeyError:
            # Generate X new fish with counter = 8
            new_fish_buckets[f] = fish_buckets[0]

    # Reset 0 fish to 6
    # Have to add since 7 fish also become 6...
    new_fish_buckets[6] += fish_buckets[0]

    return new_fish_buckets


def simulate_days(fish_buckets, days):
    for day in range(days):
        fish_buckets = next_day(fish_buckets)
        print(f"{day=}, {fish_buckets=}")

    return fish_buckets


def count_fish(fish_buckets):
    fish_values = fish_buckets.values()
    total_fish = sum(fish_values)
    print(f"{total_fish=}")
    return total_fish
