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

def calculate_gamma_rate_binary(diagnostic_report):
    width = len(diagnostic_report[0].strip())
    full_gamma = ""
    for position in range(width):
        most_common_bit = get_most_common_bit(diagnostic_report, position)
        full_gamma += str(most_common_bit)

    return bin(int(full_gamma, 2))

def calculate_epsilon_rate_binary(diagnostic_report):
    width = len(diagnostic_report[0].strip())
    full_epsilon = ""
    for position in range(width):
        least_common_bit = get_least_common_bit(diagnostic_report, position)
        full_epsilon += str(least_common_bit)

    return bin(int(full_epsilon, 2))
