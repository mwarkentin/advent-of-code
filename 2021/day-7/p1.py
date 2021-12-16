#!/usr/bin/env python3

from pprint import pprint


def parse_input(input):
    crabs = sorted([int(x) for x in input[0].split(",")])
    crab_buckets = {}
    max_x = crabs[-1] + 1

    for x in range(max_x):
        crab_buckets[x] = 0

    for crab in crabs:
        crab_buckets[crab] += 1

    return crab_buckets, max_x


def calc_fuel_to_position(crabs, position):
    fuel_cost = 0
    for x, num in crabs.items():
        x_diff = abs(x - position)
        fuel_cost += x_diff * num

    return fuel_cost


def find_lowest_fuel_cost(crabs, max_x):
    fuel_costs = []
    for x in range(max_x):
        fuel_costs.append(calc_fuel_to_position(crabs=crabs, position=x))

    return min(fuel_costs)
