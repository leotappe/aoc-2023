"""
Advent of Code 2023
Day 3
Part 1
"""


def parse_number(grid, i, j):
    number = int(grid[i][j])

    while j + 1 < len(grid[i]) and grid[i][j + 1].isdigit():
        number = 10 * number + int(grid[i][j + 1])
        j += 1

    return number


def is_start_of_number(grid, i, j):
    return grid[i][j].isdigit() and (j == 0 or not grid[i][j - 1].isdigit())


def is_part(c):
    return not c.isdigit() and c != '.'


def is_adjacent_to_part(grid, i, j, length):
    for row in range(max(0, i - 1), min(len(grid), i + 2)):
        for col in range(max(0, j - 1), min(len(grid[i]), j + length + 1)):
            if is_part(grid[row][col]):
                return True

    return False


def main():
    with open('input.txt', 'r') as f:
        grid = [line.strip() for line in f.readlines()]
    
    answer = 0

    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            if is_start_of_number(grid, i, j):
                number = parse_number(grid, i, j)
                if is_adjacent_to_part(grid, i, j, len(str(number))):
                    answer += number

    print(answer)


if __name__ == '__main__':
    main()
