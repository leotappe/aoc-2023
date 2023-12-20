"""
Advent of Code 2023
Day 18
Part 1
"""
import collections


DELTA = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0)
}


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


def main():
    instructions = []

    with open('input.txt', 'r') as f:
        for line in f.readlines():
            direction, distance, _ = line.strip().split(' ')
            instructions.append((direction, int(distance)))
    
    r, c = 0, 0
    r_min = r_max = r
    c_min = c_max = c
    
    for direction, distance in instructions:
        dr, dc = DELTA[direction]
        r += distance * dr
        c += distance * dc
        r_min = min(r_min, r)
        r_max = max(r_max, r)
        c_min = min(c_min, c)
        c_max = max(c_max, c)
    
    num_rows = r_max - r_min + 3
    num_cols = c_max - c_min + 3
    grid = [['.' for _ in range(num_cols)] for _ in range(num_rows)]

    r, c = -r_min + 1, -c_min + 1
    grid[r][c] = '#'

    for direction, distance in instructions:
        dr, dc = DELTA[direction]

        for _ in range(distance):
            r += dr
            c += dc
            grid[r][c] = '#'

    neighbors = collections.defaultdict(list)

    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell != '.':
                continue

            for dr, dc in DELTA.values():
                if 0 <= r + dr < num_rows and 0 <= c + dc < num_cols and grid[r + dr][c + dc] == '.':
                    neighbors[(r, c)].append((r + dr, c + dc))
    
    print(num_rows * num_cols - len(compute_reachable_vertices(neighbors, (0, 0))))


if __name__ == '__main__':
    main()
