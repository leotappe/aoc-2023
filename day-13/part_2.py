"""
Advent of Code 2023
Day 13
Part 2
"""


def horizontal(grid):
    for i, _ in enumerate(grid[:-1]):
        if sum(sum(above != below for above, below in zip(row_above, row_below)) for row_above, row_below in zip(grid[i::-1], grid[i + 1:])) == 1:
            return i + 1
    return None


def vertical(grid):
    for i, _ in enumerate(grid[0][:-1]):
        if sum(sum(left != right for left, right in zip(row[i::-1], row[i + 1:])) for row in grid) == 1:
            return i + 1
    return None


def solve(grid):
    if (num := vertical(grid)) is not None:
        return num    
    if (num := horizontal(grid)) is not None:
        return 100 * num
    raise ValueError("Grid doesn't contain a reflection line")


def main():
    answer = 0

    with open('input.txt', 'r') as f:
        grid = []
        for line in f.readlines():
            if line.strip():
                grid.append(line.strip())
            else:
                answer += solve(grid)
                grid = []

    print(answer + solve(grid))


if __name__ == '__main__':
    main()
