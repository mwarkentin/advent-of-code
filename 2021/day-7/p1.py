#!/usr/bin/env python3

from pprint import pprint


def parse_input(input):
    crabs = sorted([int(x) for x in input[0].split(",")])
    crab_buckets = {}

    for x in range(crabs[-1] + 1):
        crab_buckets[x] = 0

    for crab in crabs:
        crab_buckets[crab] += 1

    return crab_buckets

def calc_fuel_to_position(crabs, position):
    fuel_cost = 0
    print(f"{crabs=}")
    for x, num in crabs.items():
        x_diff = abs(x - position)
        print(f"{x=}, {num=}, {x_diff=}")
        fuel_cost += x_diff * num
        print(f"{fuel_cost=}")

    return fuel_cost
