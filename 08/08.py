#!/usr/bin/python3
import fileinput, math

file_lines = fileinput.input()
lines = [line for line in file_lines]

net = {} # {AAA: (BBB, CCC), ...}

move_types = "LR"
moves = [move_types.index(x) for x in lines[0] if x == 'R' or x == 'L']
nodes = lines[2:]
for node in nodes:
    this, children = node.split("=")
    left, right = children.split(",")
    net[this[:-1]] = (left[2:], right[1:-2])

def navigate(start, ends):
    pos = start
    steps = 0
    mi, mmax = -1, len(moves) - 1

    while pos not in ends:
        mi = mi + 1 if mi < mmax else 0
        pos = net[pos][moves[mi]]
        steps += 1

    return steps

def p1():
    print(navigate("AAA", ["ZZZ"]))

def p2():
    starts = [n for n in net if n.endswith("A")]
    ends = [n for n in net if n.endswith("Z")]
    moves = []
    for s in starts:
        moves.append(navigate(s, ends))

    print(math.lcm(*moves))

p1() # 14257
p2() # 16187743689077
