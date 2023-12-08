#!/usr/bin/python3

import fileinput

file_lines = fileinput.input()
lines = [line.rstrip() for line in file_lines]

def gather_cards():
    cards = {}
    acc = 0

    for l in lines:
        tmp, mine = l.split(" | ", 2)
        tmp = tmp.split(": ", 2)
        cardnum = int(tmp[0].split()[1])
        wn = [int(w) for w in tmp[1].split()]
        mn = [int(m) for m in mine.split()]
        matches = [x for x in mn if x in wn]
        cards[cardnum] = [x for x in range(cardnum + 1, cardnum + len(matches) + 1)]

    return cards

def process_card(cards, card):
    count = 1
    children = cards[card]

    if len(children) > 0:
        for c in children:
            count += process_card(cards, c)

    return count

def p1(cards):
    points = 0
    for c in cards:
        points += (1 << len(cards[c]) - 1) if len(cards[c]) > 0 else 0
    print(points)

def p2(cards):
    count = 0
    for c in cards:
        count += process_card(cards, c)
    print(count)

cards = gather_cards()
p1(cards) # 27845
p2(cards) # 9496801
