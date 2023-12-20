"""
Advent of Code 2023
Day 18
Part 2
"""


DELTA = {
    '0': (1, 0),    # Right
    '1': (0, 1),    # Up
    '2': (-1, 0),   # Left
    '3': (0, -1),   # Down
}


def compute_simple_polygon_area(vertices):
    return sum(x * y_next - x_next * y for (x, y), (x_next, y_next) in zip(vertices, vertices[1:] + vertices[:1])) // 2


def main():
    instructions = []

    with open('input.txt', 'r') as f:
        for line in f.readlines():
            _, _, code = line.strip().split(' ')
            code = code[2:-1]
            distance = int(code[:-1], base=16)
            direction = DELTA[code[-1]]
            instructions.append((direction, distance))
    
    vertices = []
    x, y = 0, 0
    num_blocks = 0

    for (dx, dy), length in instructions:
        x += length * dx
        y += length * dy
        vertices.append((x, y))
        num_blocks += length

    print(compute_simple_polygon_area(vertices) + (num_blocks - 4) // 2 + 3)


if __name__ == '__main__':
    main()
