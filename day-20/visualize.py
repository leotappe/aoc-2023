import sys
import graphviz


def main():
    filename = sys.argv[1]
    dot = graphviz.Digraph()

    with open(filename, 'r') as f:
        for line in f.readlines():
            module, destinations = line.strip().split(' -> ')
            destinations = destinations.split(', ')

            match module[0]:
                case '%':
                    name = module[1:]
                    dot.node(name)
                case '&':
                    name = module[1:]
                    dot.node(name, shape='square')
                case _:
                    name = module
                    dot.node(name, shape='star')

            for destination in destinations:
                dot.edge(name, destination)

    dot.render(f'{filename.removesuffix(".txt")}.gv')


if __name__ == '__main__':
    main()