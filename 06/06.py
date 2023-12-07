#!/usr/bin/python3
import fileinput

file_lines = fileinput.input()
lines = [line for line in file_lines]

times = [int(x) for x in lines[0].split(":")[1].split()]
distances = [int(x) for x in lines[1].split(":")[1].split()]

def bsearch(t, target):
    held = [x for x in range(0, t)]
    left, right = 0, 0

    L, R = 0, len(held)
    while L < R:
        m = (L + R) // 2
        res = (t - held[m]) * held[m]
        if res <= target:
            L = m + 1
        else:
            R = m
    left = L

    L, R = left, len(held)
    while L < R:
        m = (L + R) // 2
        res = (t - held[m]) * held[m]
        if res <= target:
            R = m
        else:
            L = m + 1
    right = R - 1

    return 1 + (right - left)

def p2():
    time = int("".join([str(x) for x in times]))
    distance = int("".join([str(x) for x in distances]))
    print(bsearch(time, distance))

def p1():
    result = 1
    for i, t in enumerate(times):
        result *= bsearch(t, distances[i])

    print(result)

p1() # 74698
p2() # 27563421
