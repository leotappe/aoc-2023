"""
Advent of Code 2023
Day 2
Part 1
"""


TRUE_COUNTS = {
    'red': 12,
    'green': 13,
    'blue': 14
}


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


def is_possible(observations: list[dict]):
    for counts in observations:
        for color, true_count in TRUE_COUNTS.items():
            if color in counts and counts[color] > true_count:
                return False
    
    return True


def main():
    answer = 0

    with open('input.txt', 'r') as f:
        for line in f.readlines():
            game_id, observations = parse(line.strip())
            
            if is_possible(observations):
                answer += game_id

    print(answer)


if __name__ == '__main__':
    main()
