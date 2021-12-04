#!/usr/bin/env python

# Define a filename.
filename = "input-sample.txt"
sliding_window_size = 3

def get_sliding_window(index, depths, size=sliding_window_size):
    if index + size > len(depths):
        raise ValueError("not enough data for sliding window")
    return sum(depths[index:index+size])


def count_depth_changes(depths):
    depth_counts = {}
    depth_counts["increased"] = 0
    depth_counts["decreased"] = 0
    depth_counts["no_change"] = 0

    for index, depth in enumerate(depths):
        try:
            change = get_sliding_window(depths=depths, index=index+1) - get_sliding_window(depths=depths, index=index)
        except ValueError:
            break

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
with open(filename) as f:
    depths = [int(d) for d in f.readlines()]

depth_counts = count_depth_changes(depths)
print()
print("depth changes", depth_counts)
