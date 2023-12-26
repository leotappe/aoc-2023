"""
Advent of Code 2023
Day 21
Part 1
"""


def main():
    with open('input.txt', 'r') as f:
        grid = [line.strip() for line in f.readlines()]

    start = next((i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == 'S')
    possible_positions = {start}

    for _ in range(64):
        next_possible_positions = set()

        for r, c in possible_positions:
            for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0]) and grid[r + dr][c + dc] in ['.', 'S']:
                    next_possible_positions.add((r + dr, c + dc))
        
        possible_positions = next_possible_positions
    
    print(len(possible_positions))


if __name__ == '__main__':
    main()
