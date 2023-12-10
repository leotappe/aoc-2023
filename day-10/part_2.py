"""
Advent of Code 2023
Day 10
Part 2
"""
import collections


def compute_reachable_vertices(neighbors, start):
    reachable = {start}
    stack = [start]

    while stack:
        u = stack.pop()

        for v in neighbors[u]:
            if v not in reachable:
                reachable.add(v)
                stack.append(v)

    return reachable


def compute_pipe_neighbors(grid):
    neighbors = collections.defaultdict(list)

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'S':
                start = (i, j)
            if i < len(grid) - 1 and cell in 'S|7F' and grid[i + 1][j] in 'S|LJ':
                neighbors[(i, j)].append((i + 1, j))
            if i > 0 and cell in 'S|LJ' and grid[i - 1][j] in 'S|7F':
                neighbors[(i, j)].append((i - 1, j))
            if j < len(row) - 1 and cell in 'S-LF' and row[j + 1] in 'S-J7':
                neighbors[(i, j)].append((i, j + 1))
            if j > 0 and cell in 'S-J7' and row[j - 1] in 'S-LF':
                neighbors[(i, j)].append((i, j - 1))

    return neighbors, start


def compute_empty_space_neighbors(high_res_grid):
    neighbors = collections.defaultdict(list)

    for i, row in enumerate(high_res_grid):
        for j, cell in enumerate(row):
            if cell != '.':
                continue
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= i + di < len(high_res_grid) and 0 <= j + dj < len(row) and high_res_grid[i + di][j + dj] == '.':
                    neighbors[(i, j)].append((i + di, j + dj))
    
    return neighbors


def main():
    with open('input.txt', 'r') as f:
        grid = [list(line.strip()) for line in f.readlines()]

    # Compute loop in original grid
    neighbors, start = compute_pipe_neighbors(grid)
    loop = compute_reachable_vertices(neighbors, start)

    # Compute outside in high-resolution grid
    high_res_grid = [['.' for _ in range(2 * len(grid[0]) + 1)] for _ in range(2 * len(grid) + 1)]

    for i, j in loop:
        high_res_grid[2 * i + 1][2 * j + 1] = '#'
        for k, l in neighbors[(i, j)]:
            high_res_grid[i + k + 1][j + l + 1] = '#'

    high_res_neighbors = compute_empty_space_neighbors(high_res_grid)
    high_res_outside = compute_reachable_vertices(high_res_neighbors, (0, 0))

    # Deduce outside in original grid
    outside = {(i, j) for i, row in enumerate(grid) for j, _ in enumerate(row) if (2 * i + 1, 2 * j + 1) in high_res_outside}

    # Inside is everything that is not outside and not loop
    print(len(grid) * len(grid[0]) - len(loop) - len(outside))


if __name__ == '__main__':
    main()
