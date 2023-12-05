"""
Advent of Code 2023
Day 5
Part 1
"""
import dataclasses


@dataclasses.dataclass
class RangeMapping:
    destination_start: int
    source_start: int
    length: int


class Map:
    def __init__(self, name):
        self.name = name
        self.range_mappings = []

    def add_range_mapping(self, mapping: RangeMapping):
        self.range_mappings.append(mapping)

    def map(self, key):
        for mapping in self.range_mappings:
            if mapping.source_start <= key < mapping.source_start + mapping.length:
                return mapping.destination_start + key - mapping.source_start
        return key


def main():
    maps = []

    with open('input.txt', 'r') as f:
        _, seeds = f.readline().split(':')
        seeds = [int(n) for n in seeds.split(' ') if n]

        for line in f.readlines():
            if ':' in line:
                maps.append(Map(line[:-2]))
            elif line == '\n':
                continue
            else:
                mapping = RangeMapping(*[int(n) for n in line.strip().split(' ')])
                maps[-1].add_range_mapping(mapping)

    locations = []

    for value in seeds:
        for m in maps:
            value = m.map(value)

        locations.append(value)

    print(min(locations))


if __name__ == '__main__':
    main()
