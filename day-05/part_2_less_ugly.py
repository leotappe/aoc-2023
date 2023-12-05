"""
Advent of Code 2023
Day 5
Part 2
Less ugly solution
"""
import dataclasses


@dataclasses.dataclass
class Interval:
    start: int
    end: int

    def __and__(self, other):
        return Interval(max(self.start, other.start), min(self.end, other.end))

    def __add__(self, offset):
        return Interval(self.start + offset, self.end + offset)
    
    def __bool__(self):
        return self.start <= self.end


def cut(whole: Interval, piece: Interval):
    left = Interval(whole.start, min(piece.start - 1, whole.end))
    right = Interval(max(piece.end + 1, whole.start), whole.end)
    return left, right


@dataclasses.dataclass
class IntervalTranslation:
    domain: Interval
    offset: int


class Map:
    def __init__(self):
        self.translations = []

    def add_interval_translation(self, translation: IntervalTranslation):
        self.translations.append(translation)
        self.translations.sort(key=lambda translation: translation.domain.start)

    def map(self, interval: Interval) -> list[Interval]:
        result = []

        for translation in self.translations:
            if intersection := interval & translation.domain:
                result.append(intersection + translation.offset)

            left, interval = cut(interval, translation.domain)

            if left:
                result.append(left)
    
        if interval:
            result.append(interval)

        return result


def main():
    maps = []

    with open('input.txt', 'r') as f:
        _, intervals = f.readline().split(':')
        intervals = [int(n) for n in intervals.split(' ') if n]
        intervals = [Interval(start, start + length - 1) for start, length in zip(intervals[::2], intervals[1::2])]

        for line in f.readlines():
            if ':' in line:
                maps.append(Map())
            elif line == '\n':
                continue
            else:
                destination_start, source_start, length = [int(n) for n in line.strip().split(' ')]
                domain = Interval(source_start, source_start + length - 1)
                offset = destination_start - source_start
                maps[-1].add_interval_translation(IntervalTranslation(domain, offset))

    for m in maps:
        next_intervals = []

        for interval in intervals:
            next_intervals += m.map(interval)

        intervals = next_intervals

    print(min(interval.start for interval in intervals))


if __name__ == '__main__':
    main()
