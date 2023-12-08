"""
Advent of Code 2023
Day 8
Part 1
"""
import itertools


def main():
    adjacency = {}

    with open('input.txt', 'r') as f:
        instructions = f.readline().strip()
        f.readline()

        for line in f.readlines():
            node, edges = line.strip().split(' = ')
            left, right = edges[1:-1].split(', ')
            adjacency[node] = {'L': left, 'R': right}
    
    node = 'AAA'

    for step, direction in enumerate(itertools.cycle(instructions), start=1):
        node = adjacency[node][direction]

        if node == 'ZZZ':
            break

    print(step)


if __name__ == '__main__':
    main()
