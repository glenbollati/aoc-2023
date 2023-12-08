#!/usr/bin/python3

import fileinput, math

file_lines = fileinput.input()
lines = [line.rstrip() for line in file_lines]

mr = len(lines) - 1
mc = len(lines[0]) - 1

def isadj(r, c, lines):
    tocheck = [(r - 1, c - 1), (r - 1, c), (r - 1, c + 1), (r, c - 1), (r, c + 1), (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)]
    for x in tocheck:
        nr, nc = x[0], x[1]
        if nr < 0 or nr > mr or nc < 0 or nc > mc or lines[nr][nc] == '.' or lines[nr][nc].isdigit():
            continue
        return True
    return False

def maybe_gear_ratio(r, c, lines):
    tocheck = [(r - 1, c - 1), (r - 1, c), (r - 1, c + 1), (r, c - 1), (r, c + 1), (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)]
    for x in tocheck:
        nr, nc = x[0], x[1]
        if nr < 0 or nr > mr or nc < 0 or nc > mc or lines[nr][nc] != '*':
            continue
        return x
    return None

# p1
acc, num, adj = 0, "", False
for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char.isdigit():
            num += char
            adj = True if adj else isadj(row, col, lines)
        if not char.isdigit() or col == mc: # possibly have number 
            acc += int(num) if num != "" and adj else 0
            num = ""
            adj = False

print(acc) # 559667

# p2
num, adj, gears = "", None, {}
for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char.isdigit():
            num += char
            adj = adj if adj else maybe_gear_ratio(row, col, lines)
        if not char.isdigit() or col == mc: # possibly have number 
            n = int(num) if num != "" and adj else None
            if n and adj:
                if adj in gears:
                    gears[adj] += [n]
                else:
                    gears[adj] = [n]
            adj = None
            num = ""
acc = 0 
for n in [n for n in gears if len(gears[n]) == 2]:
    acc += math.prod(gears[n])

print(acc); # 86841457
