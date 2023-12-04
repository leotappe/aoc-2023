"""
Advent of Code 2023
Day 4
Part 2
"""


def main():
    matches = []

    with open('input.txt', 'r') as f:
        for line in f.readlines():
            _, data = line.strip().split(':')
            winning, have = [[int(n.strip()) for n in numbers.strip().split(' ') if n]
                             for numbers in data.split('|')]
            matches.append(len([n for n in have if n in winning]))

    counts = [1] * len(matches)

    for i, (count, match) in enumerate(zip(counts, matches)):
        for j in range(i + 1, min(i + match + 1, len(counts))):
            counts[j] += count

    print(sum(counts))


if __name__ == '__main__':
    main()
