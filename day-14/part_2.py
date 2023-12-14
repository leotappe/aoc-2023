"""
Advent of Code 2023
Day 14
Part 2
"""


def slide(grid, i, j, di, dj):
    if grid[i][j] != 'O':
        return
    while 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[0]) and grid[i + di][j + dj] == '.':
        grid[i + di][j + dj], grid[i][j] = 'O', '.'
        i += di
        j += dj


def tilt_north(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            slide(grid, i, j, -1, 0)


def tilt_west(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            slide(grid, i, j, 0, -1)


def tilt_south(grid):
    for i in range(len(grid) - 1, -1, -1):
        for j in range(len(grid[i])):
            slide(grid, i, j, 1, 0)


def tilt_east(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i]) - 1, -1, -1):
            slide(grid, i, j, 0, 1)


def cycle(grid):
    tilt_north(grid)
    tilt_west(grid)
    tilt_south(grid)
    tilt_east(grid)


def compute_identifier(grid):
    return tuple((i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == 'O')


def main():
    with open('input.txt', 'r') as f:
        grid = [list(line.strip()) for line in f.readlines()]

    first_visit = {compute_identifier(grid): 0}
    num_cycles = 1000000000

    for iteration in range(1, num_cycles + 1):
        cycle(grid)
        identifier = compute_identifier(grid)

        if identifier in first_visit:
            break

        first_visit[identifier] = iteration

    loop_length = iteration - first_visit[identifier]
    remaining = (num_cycles - iteration) % loop_length

    for _ in range(remaining):
        cycle(grid)
    
    print(sum(len(grid) - i for i, row in enumerate(grid) for cell in row if cell == 'O'))


if __name__ == '__main__':
    main()
