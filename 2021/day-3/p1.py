#!/usr/bin/env python

from collections import Counter


def get_most_common_bit(diagnostic_report, position):
    bits = [row[position] for row in diagnostic_report]
    print(bits)
    bit_count = Counter(bits)
    print(bit_count.most_common(1))
    print(bit_count.most_common(1)[0][0])
    return int(bit_count.most_common(1)[0][0])


def get_least_common_bit(diagnostic_report, position):
    bits = [row[position] for row in diagnostic_report]
    print(bits)
    bit_count = Counter(bits)
    print(bit_count.most_common(1))
    print(bit_count.most_common(1)[0][0])
    return int(bit_count.most_common(1)[0][0]) ^ 1
