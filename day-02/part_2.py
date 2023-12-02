"""
Advent of Code 2023
Day 2
Part 2
"""


def parse(line):
    game, observations = line.split(':')
    _, game_id = game.split(' ')
    game_id = int(game_id)
    observations = observations.split(';')
    dicts = []

    for observation in observations:
        counts = {}

        for part in observation.split(','):
            count, color = part.strip().split(' ')
            counts[color] = int(count)
    
        dicts.append(counts)

    return game_id, dicts


def compute_power(observations: list[dict]):
    min_counts = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    power = 1
    
    for color in min_counts:
        for counts in observations:
            if color in counts:
                min_counts[color] = max(counts[color], min_counts[color])

        power *= min_counts[color]

    return power


def main():
    answer = 0

    with open('input.txt', 'r') as f:
        for line in f.readlines():
            _, observations = parse(line.strip())
            answer += compute_power(observations)

    print(answer)


if __name__ == '__main__':
    main()
