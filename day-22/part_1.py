"""
Advent of Code 2023
Day 22
Part 1
"""


class Brick:
    def __init__(self, minima, maxima):
        self.minima = minima
        self.maxima = maxima

    def __repr__(self):
        return f'{self.minima} -> {self.maxima}'


def is_above(top_brick, bottom_brick):
    if top_brick.minima[-1] <= bottom_brick.maxima[-1]:
        return False

    for top_min, top_max, bottom_min, bottom_max in zip(top_brick.minima[:-1], top_brick.maxima[:-1], bottom_brick.minima[:-1], bottom_brick.maxima[:-1]):
        if top_min > bottom_max or top_max < bottom_min:
            return False
    
    return True


def is_directly_above(top_brick, bottom_brick):
    return is_above(top_brick, bottom_brick) and top_brick.minima[-1] == bottom_brick.maxima[-1] + 1


def main():
    bricks = []

    with open('input.txt', 'r') as f:
        for line in f.readlines():
            minima, maxima = line.strip().split('~')
            minima = [int(n) for n in minima.split(',')]
            maxima = [int(n) for n in maxima.split(',')]
            bricks.append(Brick(minima, maxima))

    bricks.sort(key=lambda brick: brick.minima[-1])

    for i, brick in enumerate(bricks):
        y_min = 1

        for other_brick in bricks[:i]:
            if is_above(brick, other_brick):
                y_min = max(y_min, other_brick.maxima[-1] + 1)
        
        delta = brick.minima[-1] - y_min
        brick.minima[-1] -= delta
        brick.maxima[-1] -= delta

    indices_of_essential_bricks = set()

    for brick in bricks:
        supporting_indices = {i for i, other in enumerate(bricks) if is_directly_above(brick, other)}
        
        if len(supporting_indices) == 1:
            indices_of_essential_bricks |= supporting_indices

    print(len(bricks) - len(indices_of_essential_bricks))


if __name__ == '__main__':
    main()
