#!/usr/bin/python3
import fileinput

FIVE_OF_A_KIND  = 0 # AAAAA
FOUR_OF_A_KIND  = 1 # AAAA8
FULL_HOUSE      = 2 # 22333 
THREE_OF_A_KIND = 3 # TTT98
TWO_PAIRS       = 4 # 22334
ONE_PAIR        = 5 # AA234
HIGH_CARD       = 6 # 23456
KIND_COUNT      = 7

def p2_hand_kind_test():
    tests = {
        "T8JJJ": FOUR_OF_A_KIND,
        "TT8JJ": FOUR_OF_A_KIND,
        "TTT8J": FOUR_OF_A_KIND,
        "TT88J": FULL_HOUSE,
        "TT8KJ": THREE_OF_A_KIND,
        "T8KDJ": ONE_PAIR,
        "T8KDE": HIGH_CARD,
        "TJJJJ": FIVE_OF_A_KIND,
        "JJJJJ": FIVE_OF_A_KIND,
        "T8KJJ": THREE_OF_A_KIND,
        "TTKDJ": THREE_OF_A_KIND,
        "MMMDM": FOUR_OF_A_KIND,
        "DDDDD": FIVE_OF_A_KIND,
        "AAAAA": FIVE_OF_A_KIND,
        "ABCDE": HIGH_CARD,
    }
    for test in tests:
        want, got = tests[test], p2_hand_kind(test)
        if want != got:
            print("failed on test:", test, "got:", got, "wanted:", want)


file_lines = fileinput.input()
lines = [line for line in file_lines]

def p1_hand_kind(hand):
    cards = {}
    for c in hand:
        cards[c] = 1 if c not in cards else cards[c] + 1

    if len(cards) == 1:
        return FIVE_OF_A_KIND

    if len(cards) == 2:
        return FOUR_OF_A_KIND if 4 in cards.values() else FULL_HOUSE

    if len(cards) == 3:
        return THREE_OF_A_KIND if 3 in cards.values() else TWO_PAIRS
    
    if len(cards) == 4:
        return ONE_PAIR

    return HIGH_CARD

def p2_hand_kind(hand):
    if 'J' not in hand or hand == "JJJJJ":
        return p1_hand_kind(hand)

    cards = {}
    for c in hand:
        cards[c] = 1 if c not in cards else cards[c] + 1

    ret = KIND_COUNT
    for c in cards:
        tmp = hand
        if c != 'J':
            tmp = tmp.replace("J", c)
            ret = min(ret, p1_hand_kind(tmp))

    return ret;

def hand_convert(hand, map_from, map_to):
    return "".join([map_to[map_from.index(c)] for c in hand])

def run(hand_kind_fn, map_from, map_to):
    ranked = {}
    hands = {}
    for line in lines:
        hand, bid = line.split()
        kind, conv = hand_kind_fn(hand), hand_convert(hand, map_from, map_to)
        if kind in ranked:
            ranked[kind].append((conv, int(bid)))
        else:
            ranked[kind] = [(conv, int(bid))]

    rs = []
    for r in sorted(ranked):
        rs.extend(sorted(ranked[r]))
    
    tot = 0
    for i, val in enumerate(rs):
        rank = len(rs) - i
        bid = val[1]
        tot += (rank * bid)

    print(tot)

p2_hand_kind_test()

run(p1_hand_kind, "AKQJT98765432", "ABCDEFGHIJKLM") # 251029473
run(p2_hand_kind, "AKQT98765432J", "ABCDEFGHIJKLM") # 251003917
