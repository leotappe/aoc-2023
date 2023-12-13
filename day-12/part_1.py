"""
Advent of Code 2023
Day 12
Part 1
"""
import itertools


def main():
    answer = 0

    with open('input.txt', 'r') as f:
        for line in f.readlines():
            row, counts = line.strip().split(' ')
            row = list(row)
            counts = [int(n) for n in counts.split(',')]
            
            unknown_positions = [i for i, spring in enumerate(row) if spring == '?']
            num_remaining_damaged = sum(counts) - row.count('#')
            
            for assignment in itertools.combinations(unknown_positions, num_remaining_damaged):
                for i in unknown_positions:
                    row[i] = '.'
                for i in assignment:
                    row[i] = '#'

                contiguous_segments = [segment for segment in ''.join(row).split('.') if segment]
                
                if all(len(segment) == count for segment, count in zip(contiguous_segments, counts)):
                    answer += 1

    print(answer)


if __name__ == '__main__':
    main()
