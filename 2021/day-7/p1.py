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
