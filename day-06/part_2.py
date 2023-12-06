"""
Advent of Code 2023
Day 6
Part 2
"""


def main():
    with open('input.txt', 'r') as f:
        _, time = f.readline().strip().split(':')
        time = int(time.replace(' ', ''))
        _, distance = f.readline().strip().split(':')
        distance = int(distance.replace(' ', ''))

    print(sum((time - charge_duration) * charge_duration > distance for charge_duration in range(1, time)))


if __name__ == '__main__':
    main()
