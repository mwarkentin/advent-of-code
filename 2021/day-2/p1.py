#!/usr/bin/env python

# Define a filename.
filename = "input.txt"

position = {}
position["horizontal"] = 0
position["depth"] = 0

# 0: direction
# 1: multiplier for direction
cmd_list = {}
cmd_list["up"] = ["depth", -1]
cmd_list["down"] = ["depth", 1]
cmd_list["backward"] = ["horizontal", -1]
cmd_list["forward"] = ["horizontal", 1]


def parse_cmd(cmd):
    direction = cmd.split(" ")[0]
    amount = int(cmd.split(" ")[1])

    selected_cmd = cmd_list[direction]

    return [selected_cmd[0], amount * selected_cmd[1]]


with open(filename) as f:
    cmds = f.readlines()

for cmd in cmds:
    vector = parse_cmd(cmd)
    print(vector)
    position[vector[0]] += vector[1]
    print(position)

print("final position multiplication", position["horizontal"] * position["depth"])
