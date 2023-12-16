"""
Advent of Code 2023
Day 15
Part 2
"""
import dataclasses



@dataclasses.dataclass
class Lense:
    label: str
    focal_length: int


def HASH(s):
    h = 0

    for c in s:
        h += ord(c)
        h *= 17
        h %= 256

    return h


def main():
    with open('input.txt', 'r') as f:
        initialization_sequence = f.readline().strip().split(',')

    boxes = [[] for _ in range(256)]

    for step in initialization_sequence:
        if '-' in step:
            label = step[:-1]
            box_number = HASH(label)
            boxes[box_number] = [lense for lense in boxes[box_number] if lense.label != label]
        else:
            label, focal_length = step.split('=')
            focal_length = int(focal_length)
            box_number = HASH(label)
            lense = next((lense for lense in boxes[box_number] if lense.label == label), None)

            if lense:
                lense.focal_length = focal_length
            else:
                boxes[box_number].append(Lense(label, focal_length))

    print(sum(sum((box_number + 1) * slot_number * lense.focal_length
                  for slot_number, lense in enumerate(lenses, start=1))
                  for box_number, lenses in enumerate(boxes)))


if __name__ == '__main__':
    main()
