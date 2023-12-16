"""
Advent of Code 2023
Day 15
Part 1
"""


def HASH(s):
    h = 0

    for c in s:
        h += ord(c)
        h *= 17
        h %= 256

    return h


def main():
    with open('input.txt', 'r') as f:
        initialization_sequence = f.readline().strip()
    
    print(sum(HASH(step) for step in initialization_sequence.split(',')))


if __name__ == '__main__':
    main()
