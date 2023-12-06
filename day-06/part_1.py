"""
Advent of Code 2023
Day 6
Part 1
"""


def main():
    with open('input.txt', 'r') as f:
        _, times = f.readline().strip().split(':')
        times = [int(n) for n in times.split(' ') if n]
        _, distances = f.readline().strip().split(':')
        distances = [int(n) for n in distances.split(' ') if n]

    answer = 1

    for t, d in zip(times, distances):
        answer *= sum((t - charge_duration) * charge_duration > d for charge_duration in range(1, t))

    print(answer)


if __name__ == '__main__':
    main()
