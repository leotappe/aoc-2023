"""
Advent of Code 2023
Day 21
Part 2

Observations:
1. The grid is a 131x131 square.
2. The start is perfectly in the middle at (65, 65).
3. The border, as well as the 'plus' through the middle, are perfectly clear.
"""
import collections
import itertools


TOP_RIGHT = 0
TOP = 1
TOP_LEFT = 2
LEFT = 3
BOTTOM_LEFT = 4
BOTTOM = 5
BOTTOM_RIGHT = 6
RIGHT = 7
ORIGIN = 8


def bfs(start, grid):
    dists = [[None for _ in row] for row in grid]
    fifo = collections.deque([start])
    r, c = start
    dists[r][c] = 0

    while fifo:
        r, c = fifo.pop()

        for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0]) and grid[r + dr][c + dc] in ['.', 'S'] and dists[r + dr][c + dc] is None:
                dists[r + dr][c + dc] = dists[r][c] + 1
                fifo.appendleft((r + dr, c + dc))
    
    return dists


def solve_ray(grid, steps, dists_from_anchor):
    d = len(grid)

    # Precompute stuff
    max_dist_from_anchor = max(n for row in dists_from_anchor for n in row if n is not None)
    odd = sum(1 for row in dists_from_anchor for n in row if n is not None and n % 2 == 1)
    even = sum(1 for row in dists_from_anchor for n in row if n is not None and n % 2 == 0)

    if steps < d // 2 + 1:
        return 0
    
    steps -= (d // 2 + 1)
    reachable_plots = 0

    # Count plots in completely traversable copies
    if steps < max_dist_from_anchor:
        completely_traversable_copies = 0
    else:
        completely_traversable_copies = (steps - max_dist_from_anchor) // d + 1

    reachable_plots += (completely_traversable_copies // 2) * even
    reachable_plots += (completely_traversable_copies - completely_traversable_copies // 2) * odd

    # Count plots in remaining incompletely traversable copies
    steps -= completely_traversable_copies * d
    parity = (completely_traversable_copies + 1) % 2

    while steps >= d:
        reachable_plots += sum(n % 2 == parity for row in dists_from_anchor for n in row if n is not None and n <= steps)
        steps -= d
        parity = (parity + 1) % 2

    reachable_plots += sum(n % 2 == parity for row in dists_from_anchor for n in row if n is not None and n <= steps)
    return reachable_plots


def solve_quadrant(grid, steps, dists_from_anchor):
    d = len(grid)
    reachable_plots = 0

    # Precompute stuff
    max_dist_from_anchor = max(n for row in dists_from_anchor for n in row if n is not None)
    reachable_up_to = []
    for n in range(max_dist_from_anchor + 1):
        even = sum(m % 2 == 0 for row in dists_from_anchor for m in row if m is not None and m <= n)
        odd = sum(m % 2 == 1 for row in dists_from_anchor for m in row if m is not None and m <= n)
        reachable_up_to.append([even, odd])

    odd = sum(1 for row in dists_from_anchor for n in row if n is not None and n % 2 == 1)
    even = sum(1 for row in dists_from_anchor for n in row if n is not None and n % 2 == 0)

    for row in itertools.count():
        dist_to_anchor = d + 1 + row * d
        if steps < dist_to_anchor:
            break
    
        remaining_steps = steps - dist_to_anchor
        base_parity = (row + 1) % 2

        if remaining_steps < max_dist_from_anchor:
            completely_traversable_copies = 0
        else:
            completely_traversable_copies = (remaining_steps - max_dist_from_anchor) // d + 1

        if base_parity == 1:
            reachable_plots += (completely_traversable_copies // 2) * even
            reachable_plots += (completely_traversable_copies - completely_traversable_copies // 2) * odd
            parity = (completely_traversable_copies + 1) % 2
        else:
            reachable_plots += (completely_traversable_copies // 2) * odd
            reachable_plots += (completely_traversable_copies - completely_traversable_copies // 2) * even
            parity = (completely_traversable_copies) % 2

        remaining_steps -= completely_traversable_copies * d

        while remaining_steps >= d:
            reachable_plots += reachable_up_to[remaining_steps][parity]
            remaining_steps -= d
            parity = (parity + 1) % 2

        reachable_plots += reachable_up_to[remaining_steps][parity]

    return reachable_plots


def main():
    steps = 26501365

    with open('input.txt', 'r') as f:
        grid = [line.strip() for line in f.readlines()]

    R = len(grid)
    C = len(grid[0])

    start = next((r, c) for r, row in enumerate(grid) for c, cell in enumerate(row) if cell == 'S')
    r_start, c_start = start
    dists_from_start = bfs(start, grid)

    dists_from_anchors = {
        ORIGIN: dists_from_start,
        TOP: bfs((R - 1, c_start), grid),
        BOTTOM: bfs((0, c_start), grid),
        LEFT: bfs((r_start, C - 1), grid),
        RIGHT: bfs((r_start, 0), grid),
        TOP_LEFT: bfs((R - 1, C - 1), grid),
        TOP_RIGHT: bfs((R - 1, 0), grid),
        BOTTOM_LEFT: bfs((0, C - 1), grid),
        BOTTOM_RIGHT: bfs((0, 0), grid)
    }

    answer = 0

    for sector in [TOP, BOTTOM, LEFT, RIGHT]:
        reachable_plots = solve_ray(grid, steps, dists_from_anchors[sector])
        print(reachable_plots)
        answer += reachable_plots
    

    for sector in [TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT]:
        reachable_plots = solve_quadrant(grid, steps, dists_from_anchors[sector])
        print(reachable_plots)
        answer += reachable_plots

    reachable_in_origin = sum(n % 2 == 1 for row in dists_from_start for n in row if n is not None and n <= steps)
    print(reachable_in_origin)
    answer += reachable_in_origin

    print('Final answer:')
    print(answer)

    print('Upper bound:')
    print((steps + 1)**2)


if __name__ == '__main__':
    main()
