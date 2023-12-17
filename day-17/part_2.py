"""
Advent of Code 2023
Day 17
Part 2
"""
import collections
import heapq


LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)


def left(direction):
    if direction == LEFT:
        return DOWN
    if direction == RIGHT:
        return UP
    if direction == UP:
        return LEFT
    if direction == DOWN:
        return RIGHT


def right(direction):
    if direction == LEFT:
        return UP
    if direction == RIGHT:
        return DOWN
    if direction == UP:
        return RIGHT
    if direction == DOWN:
        return LEFT


def dijkstra(s, adj):
    heap = [(0, s)]
    distances = {s: 0}

    while heap:
        d_u, u = heapq.heappop(heap)

        if d_u > distances[u]:
            continue

        for c, v in adj[u]:
            d_v = d_u + c

            if v not in distances or d_v < distances[v]:
                distances[v] = d_v
                heapq.heappush(heap, (d_v, v))

    return distances


def main():
    with open('input.txt', 'r') as f:
        grid = [[int(n) for n in line.strip()] for line in f.readlines()]

     # Node: (row, col, direction, #consecutive)
    adj = collections.defaultdict(list)

    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            for direction in [LEFT, RIGHT, UP, DOWN]:
                for num_consecutive in range(1, 11):
                    # Left, Right
                    if num_consecutive >= 4:
                        for di, dj in [left(direction), right(direction)]:
                            if 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[0]):
                                adj[(i, j, direction, num_consecutive)].append((grid[i + di][j + dj], (i + di, j + dj, (di, dj), 1)))

                    # Straight
                    di, dj = direction
                    if num_consecutive < 10 and 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[0]):
                        adj[(i, j, direction, num_consecutive)].append((grid[i + di][j + dj], (i + di, j + dj, (di, dj), num_consecutive + 1)))

    start = (0, 0, (), 0)
    adj[start].append((grid[0][1], (0, 1, RIGHT, 1)))
    adj[start].append((grid[1][0], (1, 0, DOWN, 1)))

    goal = (len(grid), len(grid[0]), (), 0)

    for direction in [LEFT, RIGHT, UP, DOWN]:
        for num_consecutive in range(4, 11):
            adj[(len(grid) - 1, len(grid[0]) - 1, direction, num_consecutive)].append((0, goal))

    distances = dijkstra(start, adj)
    print(distances[goal])


if __name__ == '__main__':
    main()
