"""
Advent of Code 2023
Day 3
Part 2
"""
import math


def parse_number(grid, i, j):
    number = int(grid[i][j])

    while j + 1 < len(grid[i]) and grid[i][j + 1].isdigit():
        number = 10 * number + int(grid[i][j + 1])
        j += 1

    return number


def is_start_of_number(grid, i, j):
    return grid[i][j].isdigit() and (j == 0 or not grid[i][j - 1].isdigit())


def generate_adjacent_star_positions(grid, i, j, length):
    for row in range(max(0, i - 1), min(len(grid), i + 2)):
        for col in range(max(0, j - 1), min(len(grid), j + length + 1)):
            if grid[row][col] == '*':
                yield row, col


def main():
    with open('input.txt', 'r') as f:
        grid = [line.strip() for line in f.readlines()]
    
    stars_to_adjacent_numbers = [[[] for _ in row] for row in grid]

    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            if is_start_of_number(grid, i, j):
                number = parse_number(grid, i, j)

                for r, c in generate_adjacent_star_positions(grid, i, j, len(str(number))):
                    stars_to_adjacent_numbers[r][c].append(number)

    print(sum(math.prod(numbers)
              for row in stars_to_adjacent_numbers
              for numbers in row
              if len(numbers) == 2))


if __name__ == '__main__':
    main()
