"""
Advent of Code 2023
Day 7
Part 1
"""
import functools


def five_of_a_kind(hand):
    return len(set(hand)) == 1


def four_of_a_kind(hand):
    return any(hand.count(c) == 4 for c in hand)


def full_house(hand):
    return any(hand.count(c) == 3 for c in hand) and any(hand.count(c) == 2 for c in hand)


def three_of_a_kind(hand):
    return any(hand.count(c) == 3 for c in hand) and all(hand.count(c) != 2 for c in hand)


def two_pair(hand):
    return not three_of_a_kind(hand) and len(set(hand)) == 3


def one_pair(hand):
    return len(set(hand)) == 4


def high_card(hand):
    return len(set(hand)) == 5


def lexicographical_compare(left, right):
    order = 'AKQJT98765432'
    for l, r in zip(left, right):
        if order.index(l) < order.index(r):
            return 1
        if order.index(l) > order.index(r):
            return -1
    return 0


def cmp(left, right):
    hand_kinds = [
        five_of_a_kind,
        four_of_a_kind,
        full_house,
        three_of_a_kind,
        two_pair,
        one_pair,
        high_card
    ]

    for hand_kind in hand_kinds:
        if hand_kind(left) and not hand_kind(right):
            return 1
        if not hand_kind(left) and hand_kind(right):
            return -1

    return lexicographical_compare(left, right)


def main():
    hands_to_bids = {}

    with open('input.txt', 'r') as f:
        for line in f.readlines():
            hand, bid = line.strip().split(' ')
            hands_to_bids[hand] = int(bid)

    ranking = sorted(hands_to_bids.keys(), key=functools.cmp_to_key(cmp))
    print(sum(rank * hands_to_bids[hand] for rank, hand in enumerate(ranking, start=1)))


if __name__ == '__main__':
    main()
