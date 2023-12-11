"""
Advent of Code 2023
Day 11
Part 1
"""
import itertools


def distance(a, b, expanded):
    return sum(abs(b_i - a_i) + abs(e[b_i] - e[a_i]) for a_i, b_i, e in zip(a, b, expanded))


def main():
    with open('input.txt', 'r') as f:
        grid = [line.strip() for line in f.readlines()]

    expanded_rows = [0]
    expanded_columns = [0]

    for row in grid:
        expanded_rows.append(expanded_rows[-1])
        if all(c != '#' for c in row):
            expanded_rows[-1] += 1

    for j, _ in enumerate(grid[0]):
        expanded_columns.append(expanded_columns[-1])
        if all(row[j] != '#' for row in grid):
            expanded_columns[-1] += 1

    expanded = [expanded_rows, expanded_columns]
    galaxies = [(i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == '#']
    print(sum(distance(a, b, expanded) for a, b in itertools.combinations(galaxies, 2)))


if __name__ == '__main__':
    main()
