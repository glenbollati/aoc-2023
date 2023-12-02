#!/usr/bin/python3
import fileinput
import math

file_lines = fileinput.input()
lines = [line[:-1] for line in file_lines]

def p1():
    acc, gid = 0, 0
    colours = { "red": 12, "green": 13, "blue": 14 }
    for line in lines:
        gid += 1
        die = line.split(": ")[1].replace(';', ',').split(', ')
        possible = True
        for d in die:
            val, colour = d.split()
            if int(val) > colours[colour]:
                possible = False
        acc += gid if possible else 0

    print(acc)

def p2():
    acc = 0
    for line in lines:
        die = line.split(": ")[1].replace(';', ',').split(', ')
        mins = {}
        for d in die:
            val, colour = d.split()
            mins[colour] = int(val) if colour not in mins else max(mins[colour], int(val))
        acc += math.prod(mins.values())

    print(acc)

p1()
p2()
