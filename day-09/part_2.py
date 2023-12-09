"""
Advent of Code 2023
Day 9
Part 2
"""


def predict_previous_value(history):
    if all(n == 0 for n in history):
        return 0
    return history[0] - predict_previous_value([nxt - curr for nxt, curr in zip(history[1:], history[:-1])])


def main():
    answer = 0

    with open('input.txt', 'r') as f:
        for line in f.readlines():
            history = [int(n) for n in line.strip().split(' ')]
            answer += predict_previous_value(history)
    
    print(answer)


if __name__ == '__main__':
    main()
