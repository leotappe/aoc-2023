"""
Advent of Code 2023
Day 4
Part 1
"""


def main():
    answer = 0

    with open('input.txt', 'r') as f:
        for line in f.readlines():
            _, data = line.strip().split(':')
            winning, have = [[int(n.strip()) for n in numbers.strip().split(' ') if n]
                             for numbers in data.split('|')]
            count = len([n for n in have if n in winning])
            if count > 0:
                answer += 2**(count - 1)

    print(answer)


if __name__ == '__main__':
    main()
