#!/usr/bin/python3
import fileinput

file_lines = fileinput.input()
lines = [line[:-1] for line in file_lines]

def p1():
    acc = 0
    for line in lines:
        digs = [char for char in line if char.isdigit()]
        num = digs[0] + digs[len(digs) - 1]
        acc += int(num)
    print(acc)

def p2():
    acc = 0
    digits = {
        "one": "1", "two": "2", "three": "3",
        "four": "4", "five": "5", "six": "6",
        "seven": "7", "eight": "8", "nine": "9"
    }
    for line in lines:
        digs = []
        for i, char in enumerate(line):
            if char.isdigit():
                digs.append(char)
                continue
            for string, integer in digits.items():
                if line[i:].startswith(string):
                    digs.append(integer)
        acc += int(digs[0] + digs[len(digs) - 1])

    print(acc)

p1()
p2()
