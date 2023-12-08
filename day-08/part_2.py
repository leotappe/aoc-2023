"""
Advent of Code 2023
Day 8
Part 2
"""
import itertools
import math


def main():
    adjacency = {}

    with open('input.txt', 'r') as f:
        instructions = f.readline().strip()
        f.readline()

        for line in f.readlines():
            node, edges = line.strip().split(' = ')
            left, right = edges[1:-1].split(', ')
            adjacency[node] = {'L': left, 'R': right}
    
    nodes = [node for node in adjacency if node[-1] == 'A']
    lengths = [None] * len(nodes)

    for step, direction in enumerate(itertools.cycle(instructions), start=1):
        nodes = [adjacency[node][direction] for node in nodes]

        for i, node in enumerate(nodes):
            if node[-1] == 'Z' and lengths[i] is None:
                lengths[i] = step

        if all(length is not None for length in lengths):
            break

    print(math.lcm(*lengths))


if __name__ == '__main__':
    main()
