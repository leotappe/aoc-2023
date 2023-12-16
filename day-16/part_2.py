"""
Advent of Code 2023
Day 16
Part 2
"""
import sys


LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)


def compute_new_position(pos, direction):
    r, c = pos
    dr, dc = direction
    return r + dr, c + dc


def generate_new_directions(cell, direction):
    match cell:
        case '.':
            yield direction
        case '/':
            if direction == LEFT:
                yield DOWN
            if direction == RIGHT:
                yield UP
            if direction == UP:
                yield RIGHT
            if direction == DOWN:
                yield LEFT
        case '\\':
            if direction == LEFT:
                yield UP
            if direction == RIGHT:
                yield DOWN
            if direction == UP:
                yield LEFT
            if direction == DOWN:
                yield RIGHT
        case '-':
            if direction in [LEFT, RIGHT]:
                yield direction
            else:
                yield LEFT
                yield RIGHT
        case '|':
            if direction in [UP, DOWN]:
                yield direction
            else:
                yield UP
                yield DOWN

def visit(pos, direction, grid, directions):
    r, c = pos

    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or direction in directions[r][c]:
        return

    directions[r][c].add(direction)

    for new_dir in generate_new_directions(grid[r][c], direction):
        visit(compute_new_position(pos, new_dir), new_dir, grid, directions)


def main():
    with open('input.txt', 'r') as f:
        grid = [line.strip() for line in f.readlines()]

    sys.setrecursionlimit(len(grid) * len(grid[0]) + 10)
    answer = 0

    for r, _ in enumerate(grid):
        directions = [[set() for _ in row] for row in grid]
        visit((r, 0), RIGHT, grid, directions)
        answer = max(answer, sum(sum(len(cell) > 0 for cell in row) for row in directions))

        directions = [[set() for _ in row] for row in grid]
        visit((r, len(grid[0]) - 1), LEFT, grid, directions)
        answer = max(answer, sum(sum(len(cell) > 0 for cell in row) for row in directions))

    for c, _ in enumerate(grid[0]):
        directions = [[set() for _ in row] for row in grid]
        visit((0, c), DOWN, grid, directions)
        answer = max(answer, sum(sum(len(cell) > 0 for cell in row) for row in directions))

        directions = [[set() for _ in row] for row in grid]
        visit((len(grid) - 1, c), UP, grid, directions)
        answer = max(answer, sum(sum(len(cell) > 0 for cell in row) for row in directions))

    print(answer)


if __name__ == '__main__':
    main()
