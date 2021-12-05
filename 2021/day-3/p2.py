#!/usr/bin/env python

from collections import Counter


def get_most_common_bit(diagnostic_report, position):
    bits = [row[position] for row in diagnostic_report]
    bit_count = Counter(bits)
    return int(bit_count.most_common(1)[0][0])


def get_least_common_bit(diagnostic_report, position):
    bits = [row[position] for row in diagnostic_report]
    bit_count = Counter(bits)
    return int(bit_count.most_common(1)[0][0]) ^ 1


def filter_report(report, num, position):
    return [row.strip() for row in report if row[position] == num]

def get_oxygen_generator_rating(report, position):
    mcb = get_most_common_bit(report, position)
    filtered_report = filter_report(report, str(mcb), position)

    if len(filtered_report) == 1:
        return filtered_report[0]
    else:
        return get_oxygen_generator_rating(filtered_report, position + 1)

def get_co2_scrubber_rating(report, position):
    lcb = get_least_common_bit(report, position)
    filtered_report = filter_report(report, str(lcb), position)

    if len(filtered_report) == 1:
        return filtered_report[0]
    else:
        return get_co2_scrubber_rating(filtered_report, position + 1)

def get_life_support_rating(report):
    oxygen_rating = int(get_oxygen_generator_rating(report, 0), 2)
    co2_rating = int(get_co2_scrubber_rating(report, 0), 2)

    return oxygen_rating * co2_rating
