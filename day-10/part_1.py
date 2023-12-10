"""
Advent of Code 2023
Day 10
Part 1
"""
import collections


def bfs(neighbors, start):
    distances = {start: 0}
    fifo = collections.deque([start])

    while fifo:
        u = fifo.pop()

        for v in neighbors[u]:
            if v not in distances:
                distances[v] = distances[u] + 1
                fifo.appendleft(v)

    return distances


def main():
    with open('input.txt', 'r') as f:
        grid = [line.strip() for line in f.readlines()]

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

    distances = bfs(neighbors, start)
    print(max(*distances.values()))


if __name__ == '__main__':
    main()
