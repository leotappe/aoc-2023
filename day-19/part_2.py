"""
Advent of Code 2023
Day 19
Part 2
"""
import operator
import math


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


def compute_accepting_configurations(name, workflows):
    if name == 'R':
        return []

    if name == 'A':
        return [{
            'x': (1, 4000),
            'm': (1, 4000),
            'a': (1, 4000),
            's': (1, 4000)
        }]   

    workflow = workflows[name]
    intervals = {
        'x': (1, 4000),
        'm': (1, 4000),
        'a': (1, 4000),
        's': (1, 4000)
    }
    accepting_configurations = []

    for condition, target in zip(workflow.conditions, workflow.targets):
        yes_intervals = intervals.copy()
        start, end = intervals[condition.category]

        if condition.op == operator.lt:
            yes_intervals[condition.category] = (start, condition.threshold - 1)
            intervals[condition.category] = (condition.threshold, end)
        else:
            yes_intervals[condition.category] = (condition.threshold + 1, end)
            intervals[condition.category] = (start, condition.threshold)

        recursive_configurations = compute_accepting_configurations(target, workflows)
        accepting_configurations += compute_pruned_configurations(recursive_configurations, yes_intervals)

    recursive_configurations = compute_accepting_configurations(workflow.final_target, workflows)
    accepting_configurations += compute_pruned_configurations(recursive_configurations, intervals)

    return accepting_configurations


def compute_pruned_configurations(configurations, intervals):
    pruned = []

    for configuration in configurations:
        adapted_configuration = {}

        for category, (config_start, config_end) in configuration.items():
            start, end = intervals[category]

            if start > config_end or end < config_start:
                adapted_configuration = None
                break

            adapted_configuration[category] = (max(start, config_start), min(config_end, end))
        
        if adapted_configuration is not None:
            pruned.append(adapted_configuration)

    return pruned


def main():
    workflows = {}

    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        separator_index = lines.index('')
        workflow_lines, _ = lines[:separator_index], lines[separator_index + 1:]

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

    accepting_configurations = compute_accepting_configurations('in', workflows)
    print(sum(math.prod(end - start + 1 for start, end in configuration.values()) for configuration in accepting_configurations))


if __name__ == '__main__':
    main()
