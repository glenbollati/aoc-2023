#!/usr/bin/python3
import fileinput

file_lines = fileinput.input()
lines = [line for line in file_lines]

def solve(p2):
    tot = 0
    for line in lines:
        seq = [int(x) for x in line.split()]
        ss = [[x for x in seq]]
        zero = False
        while not zero:
            n, s = [], ss[-1]
            zero = True
            for j in range(0, len(s) - 1):
                n.append(s[j + 1] - s[j])
                if n[j] != 0:
                    zero = False
            ss.append(n)
        if p2:
            ss[-1].insert(0, 0)
        else:
             ss[-1].append(0)
        for i in range(len(ss) - 2, -1, -1):
            if p2:
                ds = ss[i+1][0]
                ss[i].insert(0, ss[i][0] - ds)
            else:
                ds = ss[i+1][-1]
                ss[i].append(ss[i][-1] + ds)
        if p2:
            tot += ss[0][0]
        else:
            tot += ss[0][-1]
    print(tot)

solve(False) # 1725987467
solve(True)  # 971
