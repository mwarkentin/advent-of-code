#!/usr/bin/env python

from os import path

# Define a filename.
file_path = path.abspath("input.txt")

def count_depth_changes(depths):
    depth_counts = {}
    depth_counts["increased"] = 0
    depth_counts["decreased"] = 0
    depth_counts["no_change"] = 0

    for index, depth in enumerate(depths):
        if index == 0:
            continue

        change = int(depth) - int(depths[index-1])
        if change > 0:
            print(depth, "increased")
            depth_counts["increased"] += 1
        elif change < 0:
            print(depth, "decreased")
            depth_counts["decreased"] += 1
        else:
            print(depth, "no change")
            depth_counts["no_change"] += 1

    return depth_counts

# Open the file as f.
# The function readlines() reads the file.
with open(file_path) as f:
    depths = f.readlines()

depth_counts = count_depth_changes(depths)
print()
print("depth changes", depth_counts)
