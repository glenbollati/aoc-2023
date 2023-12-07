#!/usr/bin/python3
import fileinput

file_lines = fileinput.input()
lines = [line for line in file_lines]
seeds = [int(x) for x in lines[0].split(":")[1].split()]

mappings = {
    "seed": [],
    "soil": [],
    "fertilizer": [],
    "water": [],
    "light": [],
    "temperature": [],
    "humidity": []
}

def fillmap():
    currkey = None
    for line in lines[1:]:
        if len(line) == 0:
            continue

        if line[0].isdigit():
            vals = tuple([int(x) for x in line.split()])
            mappings[currkey].append(vals)
            continue

        for key in mappings:
            if line.startswith(key):
                currkey = key

def getnext(idx, key):
    for entry in mappings[key]:
        dst, src, rng = entry
        if idx < src or idx > (src + rng):
            continue
        offset = idx - src
        return dst + offset
    return idx

def p1(seeds):
    res = None
    for seed in seeds:
        idx = seed
        for key in mappings:
            idx = getnext(idx, key)
        res = min(res, idx) if res else idx
    print(res)

fillmap()
p1(seeds) # 382895070

def split_ranges(seeds, key):
    groups = mappings[key]
    out = []
    while seeds:
        ss, se = seeds.pop()
        mapped = False
        for (dst, src, rng) in groups:
            ms, me = src, src + rng
            overlap = (max(ss, ms), min(se, me))
            if overlap[0] >= overlap[1]:
                continue # no overlap

            mapped = True
            out.append((overlap[0] - src + dst, overlap[1] - src + dst))

            # push any leftovers (left and right of overlap) back onto the stack
            # for processing
            if (overlap[0] > ss):
                seeds.append((ss, overlap[0]))
            if (overlap[1] < se):
                seeds.append((overlap[1], se))
            break

        if not mapped:
            out.append((ss, se))
    return out

def p2(seeds):
    # convert to ranges in format (low, high)
    seeds = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
    for key in mappings:
        seeds = split_ranges(seeds, key)
    print(min(seeds)[0])
            
p2(seeds) # 17729182
