

FILENAME = './input'
# FILENAME = './example2'


def add_to_network(network, line):
    node, neighbors = line.split(' = ')
    left, right = neighbors.replace('(', '').replace(')', '').split(', ')
    network[node] = {'left': left, 'right': right}


def parse_data(filename):
    network = {}
    instructions = ''
    with open(filename) as data:
        for raw_line in data:
            line = raw_line.rstrip()
            if instructions == '':
                instructions = line
            elif line.rstrip() != '':
                add_to_network(network, line)
    return network, instructions


def steps_until_end(network, instructions):
    steps = 0
    current_node = 'AAA'
    has_found_end = False
    while not has_found_end:
        for instruction in instructions:
            direction = 'left' if instruction == 'L' else 'right'
            current_node = network[current_node][direction]
            steps += 1
            if current_node == 'ZZZ':
                has_found_end = True
                break
    return steps


def run():
    network, instructions = parse_data(FILENAME)
    steps = steps_until_end(network, instructions)
    print(steps)


if __name__ == '__main__':
    run()
