"""
Advent of Code 2023
Day 19
Part 1
"""
import operator


SYMBOL_TO_OPERATOR = {
    '<': operator.lt,
    '>': operator.gt
}


class Condition:
    def __init__(self, category, op, threshold):
        self.category = category
        self.op = op
        self.threshold = threshold

    def __call__(self, part):
        return self.op(part[self.category], self.threshold) 


class Workflow:
    def __init__(self):
        self.conditions = []
        self.targets = []
        self.final_target = None

    def process(self, part):
        for condition, target in zip(self.conditions, self.targets):
            if condition(part):
                return target
        return self.final_target


def main():
    workflows = {}
    parts = []

    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        separator_index = lines.index('')
        workflow_lines, part_lines = lines[:separator_index], lines[separator_index + 1:]

        for line in workflow_lines:
            name, rules = line.split('{')
            workflow = Workflow()
            rules = rules[:-1]
            
            for rule in rules.split(','):
                if ':' in rule:
                    condition, target = rule.split(':')
                    category, op, threshold = condition[0], SYMBOL_TO_OPERATOR[condition[1]], int(condition[2:])
                    workflow.conditions.append(Condition(category, op, threshold))
                    workflow.targets.append(target)
                else:
                    workflow.final_target = rule

            workflows[name] = workflow

        for line in part_lines:
            part = {}

            for description in line[1:-1].split(','):
                category, value = description.split('=')
                part[category] = int(value)

            parts.append(part)

    answer = 0

    for part in parts:
        name = 'in'

        while name not in ['A', 'R']:
            name = workflows[name].process(part)
        
        if name == 'A':
            answer += sum(part.values())

    print(answer)


if __name__ == '__main__':
    main()
