"""
Advent of Code 2023
Day 1
Part 2
"""


MAP = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
} | {
    str(i) : i
    for i in range(10)
}


def compute_calibration_value(line: str):
    first_digit, last_digit = None, None
    
    for i, _ in enumerate(line):
        for k, v in MAP.items():
            if line[i:].startswith(k):
                if first_digit is None:
                    first_digit = v
                last_digit = v

    return 10 * first_digit + last_digit    


def main():
    answer = 0

    with open('input.txt', 'r') as f:
        for line in f.readlines():
            answer += compute_calibration_value(line.strip())

    print(answer)


if __name__ == '__main__':
    main()
