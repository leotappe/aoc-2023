"""
Advent of Code 2023
Day 22
Part 2
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


def chain_reaction(index, adj, support):
    support = support[:]
    falling = []

    for other_index in adj[index]:
        support[other_index] -= 1

        if support[other_index] == 0:
            falling.append(other_index)

    fallen = 0

    while falling:
        index = falling.pop()
        fallen += 1

        for other_index in adj[index]:
            support[other_index] -= 1

            if support[other_index] == 0:
                falling.append(other_index)

    return fallen


def main():
    bricks = []

    with open('example.txt', 'r') as f:
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

    adj = [[] for _ in bricks]
    support = [0] * len(bricks)

    for i, brick in enumerate(bricks):
        for j, other_brick in enumerate(bricks):
            if is_directly_above(brick, other_brick):
                adj[j].append(i)
                support[i] += 1

    answer = 0

    for i, _ in enumerate(bricks):
        answer += chain_reaction(i, adj, support)

    print(answer)


if __name__ == '__main__':
    main()
