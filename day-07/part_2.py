"""
Advent of Code 2023
Day 7
Part 2
"""
import itertools


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.best_hand_kind = None

    def __lt__(self, other):
        if self.best_hand_kind is None:
            self.best_hand_kind = compute_best_hand_kind(self.cards)
        
        if other.best_hand_kind is None:
            other.best_hand_kind = compute_best_hand_kind(other.cards)
        
        if self.best_hand_kind != other.best_hand_kind:
            return self.best_hand_kind > other.best_hand_kind
        
        return lexicographical_compare(self.cards, other.cards)


def five_of_a_kind(cards):
    return len(set(cards)) == 1


def four_of_a_kind(cards):
    return any(cards.count(c) == 4 for c in cards)


def full_house(cards):
    return any(cards.count(c) == 3 for c in cards) and any(cards.count(c) == 2 for c in cards)


def three_of_a_kind(cards):
    return any(cards.count(c) == 3 for c in cards) and all(cards.count(c) != 2 for c in cards)


def two_pair(cards):
    return not three_of_a_kind(cards) and len(set(cards)) == 3


def one_pair(cards):
    return len(set(cards)) == 4


def high_card(cards):
    return len(set(cards)) == 5


def lexicographical_compare(left, right):
    order = 'AKQT98765432J'
    for l, r in zip(left, right):
        if order.index(l) !=  order.index(r):
            return order.index(l) > order.index(r)
    return False


def compute_best_hand_kind(cards):
    hand_kinds = [
        five_of_a_kind,
        four_of_a_kind,
        full_house,
        three_of_a_kind,
        two_pair,
        one_pair,
        high_card,
    ]

    for rank, hand_kind in enumerate(hand_kinds):
        if any(hand_kind(replacement) for replacement in generate_replacements(cards)):
            return rank

    raise ValueError('Invalid card given')


def generate_replacements(cards):
    potential_replacements = 'AKQT98765432'
    indices_of_jokers = [i for i, c in enumerate(cards) if c == 'J']
    cards = list(cards)

    for combination in itertools.combinations_with_replacement(potential_replacements, len(indices_of_jokers)):
        for i, c in zip(indices_of_jokers, combination):
            cards[i] = c
        yield ''.join(cards)


def main():
    hands = []

    with open('input.txt', 'r') as f:
        for line in f.readlines():
            cards, bid = line.strip().split(' ')
            hands.append(Hand(cards, int(bid)))

    hands.sort()
    print(sum(rank * hand.bid for rank, hand in enumerate(hands, start=1)))


if __name__ == '__main__':
    main()
