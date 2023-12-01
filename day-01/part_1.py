"""
Advent of Code 2023
Day 1
Part 1
"""


def compute_calibration_value(line: str):
    first_digit, last_digit = None, None
    
    for c in line:
        if '0' <= c <= '9':
            if first_digit is None:
                first_digit = ord(c) - ord('0')
            last_digit = ord(c) - ord('0')

    return 10 * first_digit + last_digit    


def main():
    answer = 0

    with open('input.txt', 'r') as f:
        for line in f.readlines():
            answer += compute_calibration_value(line.strip())

    print(answer)


if __name__ == '__main__':
    main()
