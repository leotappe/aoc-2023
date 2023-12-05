"""
Advent of Code 2023
Day 5
Part 2
"""
import dataclasses


@dataclasses.dataclass
class Range:
    start: int
    length: int

    def __and__(self, other):
        start = max(self.start, other.start)
        end = min(self.start + self.length, other.start + other.length)
        length = end - start
        return Range(start, length)


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
        self.range_mappings.sort(key=lambda mapping: mapping.source_start)


    def map(self, range: Range):
        curr_range = Range(range.start, range.length)
        resulting_ranges = []

        for mapping in self.range_mappings:
            if mapping.source_start + mapping.length <= curr_range.start:
                continue

            if mapping.source_start >= range.start + range.length:
                break
        
            if curr_range.start < mapping.source_start:
                resulting_ranges.append(Range(curr_range.start, mapping.source_start - curr_range.start))

            source_intersection = curr_range & Range(mapping.source_start, mapping.length)
            resulting_ranges.append(Range(source_intersection.start + mapping.destination_start - mapping.source_start, source_intersection.length))

            new_start = source_intersection.start + source_intersection.length
            new_length = curr_range.length - (new_start - curr_range.start)
            curr_range = Range(new_start, new_length)

            if curr_range.start >= range.start + range.length:
                break

        if curr_range.start < range.start + range.length:
            resulting_ranges.append(curr_range)

        return resulting_ranges


def main():
    maps = []

    with open('example.txt', 'r') as f:
        _, ranges = f.readline().split(':')
        ranges = [int(n) for n in ranges.split(' ') if n]
        ranges = [Range(start, length) for start, length in zip(ranges[::2], ranges[1::2])]

        for line in f.readlines():
            if ':' in line:
                maps.append(Map(line[:-2]))
            elif line == '\n':
                continue
            else:
                mapping = RangeMapping(*[int(n) for n in line.strip().split(' ')])
                maps[-1].add_range_mapping(mapping)

    for m in maps:
        next_ranges = []
        for r in ranges:
            next_ranges += m.map(r)
        ranges = next_ranges

    print(min(r.start for r in ranges))


if __name__ == '__main__':
    main()
