"""
Advent of Code 2023
Day 12
Part 2
"""


class DP:
    def __init__(self, row, counts):
        self.row = row
        self.counts = counts
        self.cache = {}

    def solve(self, i, j, k):
        if (i, j, k) in self.cache:
            return self.cache[(i, j, k)]
        if i < 0 or self.row[i] == '.':
            self.cache[(i, j, k)] = 0
        elif k > 0:
            self.cache[(i, j, k)] = self.solve(i - 1, j, k - 1)
        elif j == 0:
            self.cache[(i, j, k)] = 1 if all(spring != '#' for spring in self.row[:i]) else 0
        elif i < 2 or self.row[i - 1] == '#':
            self.cache[(i, j, k)] = 0
        else:
            answer = 0
            for l in range(i - 2, -1, -1):
                answer += self.solve(l, j - 1, self.counts[j - 1] - 1)
                if self.row[l] == '#':
                    break
            self.cache[(i, j, k)] = answer
        return self.cache[(i, j, k)]


def main():
    answer = 0

    with open('input.txt', 'r') as f:
        for line in f.readlines():
            row, counts = line.strip().split(' ')
            row = f'{row}?{row}?{row}?{row}?{row}'
            counts = [int(n) for n in counts.split(',')] * 5
            dp = DP(row, counts)
            answer += sum(dp.solve(i, len(counts) - 1, counts[-1] - 1)
                          for i, _ in enumerate(row)
                          if all(spring != '#' for spring in row[i + 1:]))

    print(answer)


if __name__ == '__main__':
    main()
