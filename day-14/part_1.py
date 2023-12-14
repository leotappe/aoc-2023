"""
Advent of Code 2023
Day 14
Part 1
"""


def slide_north(grid, i, j):
    if grid[i][j] != 'O':
        return
    while i > 0 and grid[i - 1][j] == '.':
        grid[i - 1][j], grid[i][j] = 'O', '.'
        i -= 1


def tilt_north(grid):
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            slide_north(grid, i, j)


def main():
    with open('input.txt', 'r') as f:
        grid = [list(line.strip()) for line in f.readlines()]

    tilt_north(grid)
    print(sum(len(grid) - i for i, row in enumerate(grid) for cell in row if cell == 'O'))


if __name__ == '__main__':
    main()
