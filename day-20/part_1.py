"""
Advent of Code 2023
Day 20
Part 1

Assumption: pulses are not sent simultaneously, but shortly after each other.
"""
import collections


class FlipFlopModule:
    def __init__(self, destination_names):
        self.destination_names = destination_names
        self.on = False

    def send(self):
        return self.on

    def receive(self, pulse, sender):
        if not pulse:
            self.on = not self.on
            return True

        return False


class ConjunctionModule:
    def __init__(self, destination_names):
        self.destination_names = destination_names
        self.most_recent_pulses = {}
    
    def send(self):
        return not all(self.most_recent_pulses.values())

    def receive(self, pulse, sender):
        self.most_recent_pulses[sender] = pulse
        return True


class BroadcastModule:
    def __init__(self, destination_names):
        self.destination_names = destination_names
        self.last_received_pulse = None

    def send(self):
        return self.last_received_pulse
    
    def receive(self, pulse, sender):
        self.last_received_pulse = pulse
        return True


class UntypedModule:
    def __init__(self):
        self.destination_names = []

    def receive(self, pulse, sender):
        return False


def main():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    modules = {}
    names = set()
    conjunction_names = set()

    for line in lines:
        module, destinations = line.split(' -> ')
        destinations = destinations.split(', ')

        match module[0]:
            case '%':
                modules[module[1:]] = FlipFlopModule(destinations)
            case '&':
                modules[module[1:]] = ConjunctionModule(destinations)
                conjunction_names.add(module[1:])
            case _:
                modules[module] = BroadcastModule(destinations)

        names |= set(destinations)

    for name in names:
        if name not in modules:
            modules[name] = UntypedModule()

    for name, module in modules.items():
        for dest_name in module.destination_names:
            if dest_name in conjunction_names:
                modules[dest_name].most_recent_pulses[name] = False

    high = 0
    low = 0

    for _ in range(1000):
        pulses = collections.deque([(False, 'button', 'broadcaster')])

        while pulses:
            pulse, sender_name, dest_name = pulses.pop()

            if pulse:
                high += 1
            else:
                low += 1

            dest = modules[dest_name]

            if dest.receive(pulse, sender_name):
                new_pulse = dest.send()

                for name in dest.destination_names:
                    pulses.appendleft((new_pulse, dest_name, name))

    print(low * high)


if __name__ == '__main__':
    main()
