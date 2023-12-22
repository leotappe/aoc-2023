"""
Advent of Code 2023
Day 20
Part 2

Explanation:
There are 4 "independent" components of the graph - see input.gv.pdf.
They all consist of 12 flip-flops and a single conjunction (call it the
'representative' of the component).
The output of each representative goes through an inverter to a final
conjunction that directly feeds into rx.
Thus, we're looking for the first time that the most recent outputs of the
representatives from each component are all low.

It can easily be seen that each time a representative fires low, it fires high
shortly after (during the same button press). So at the beginning of each
button press, the most recent output of all representatives is high.
This means we're looking for a button press where all representatives fire low
at least once.

We also know that each component only has 2**24 possible states after a button
press (12 "most recent input configurations" for the representative, as well
as 2**12 configurations for the 12 flip-flops). This means that after at most
2**24 button presses, we'll start to cycle.

Additional analysis shows that each component cycles back to its initial state,
and moreover that each representative fires low exactly once during its
component's cycle. Thus, the only possible solution is the LCM of the first
button presses that cause the representatives to fire low.

Code is decently ugly, but I'm too lazy to clean it up.
"""
import collections
import itertools
import math


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

    def state(self):
        return self.on


class ConjunctionModule:
    def __init__(self, destination_names):
        self.destination_names = destination_names
        self.most_recent_pulses = {}
    
    def send(self):
        return not all(self.most_recent_pulses.values())

    def receive(self, pulse, sender):
        self.most_recent_pulses[sender] = pulse
        return True

    def state(self):
        return tuple(self.most_recent_pulses[sender] for sender in sorted(self.most_recent_pulses.keys()))


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


def compute_state_identifier(component, modules):
    return tuple(modules[name].state() for name in component)


class Component:
    def __init__(self, representative, members):
        self.representative = representative
        self.members = members
        self.cycle_length = None
        self.first_visit = {}


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

    components = [
        ['tx', 'dx', 'ph', 'mb', 'jc', 'kt', 'ct', 'kd', 'pp', 'jp', 'vr', 'hp', 'pz'],
        ['nv', 'th', 'hx', 'xb', 'jf', 'bc', 'xm', 'gv', 'nr', 'cj', 'vh', 'jh', 'mh'],
        ['bx', 'fx', 'sk', 'hr', 'ff', 'xc', 'nx', 'fn', 'kn', 'mv', 'fk', 'rv', 'rn'],
        ['jq', 'qt', 'lj', 'dt', 'zb', 'fb', 'vp', 'lp', 'jm', 'xk', 'nk', 'vk', 'jt']
    ]

    representatives = ['pz', 'mh', 'rn', 'jt']
    first_visits = [{compute_state_identifier(component, modules): 0} for component in components]
    cycle_lengths = [None] * 4
    low_fires = [set() for _ in representatives]

    for press in itertools.count(1):
        pulses = collections.deque([(False, 'button', 'broadcaster')])

        while pulses:
            pulse, sender_name, dest_name = pulses.pop()
            dest = modules[dest_name]

            if sender_name in representatives and not pulse:
                low_fires[representatives.index(sender_name)].add(press)

            if dest.receive(pulse, sender_name):
                new_pulse = dest.send()

                for name in dest.destination_names:
                    pulses.appendleft((new_pulse, dest_name, name))

        for i, (component, first_visit) in enumerate(zip(components, first_visits)):
            if cycle_lengths[i] is not None:
                continue

            identifier = compute_state_identifier(component, modules)
            if identifier in first_visit:
                cycle_lengths[i] = press - first_visit[identifier]
                print(f'Component {i}: cycle of length {cycle_lengths[i]} between {first_visit[identifier]} and {press}')
            else:
                first_visit[identifier] = press

        if all(c is not None for c in cycle_lengths):
            break

    print(low_fires)
    print(math.lcm(*(l.pop() for l in low_fires)))


if __name__ == '__main__':
    main()
