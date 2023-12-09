import math

FILENAME = './input'
# FILENAME = './example3'


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


def steps_until_end_ghost(network, instructions):
    steps = 0
    current_nodes = [x for x in network.keys() if x[-1] == 'A']
    print(current_nodes)
    print(instructions)
    has_found_end = False
    counters = [[] for node in current_nodes]
    current_counters = [0 for node in current_nodes]
    while steps <= len(instructions) * len(network):
        # if steps % (283*1000) == 0:
        #     print(steps//283)
        for instruction in instructions:
            steps += 1
            direction = 'left' if instruction == 'L' else 'right'
            has_found_end = True
            for i in range(len(current_nodes)):
                current_nodes[i] = network[current_nodes[i]][direction]
                if current_nodes[i][-1] == 'Z':
                    counters[i].append(current_counters[i] + 1)
                    current_counters[i] = 0
                else:
                    current_counters[i] += 1
                if has_found_end and current_nodes[i][-1] != 'Z':
                    has_found_end = False
            if has_found_end:
                break
    for counter in counters:
        print(counter)
    return [counter[0] for counter in counters]


def run():
    network, instructions = parse_data(FILENAME)
    print(steps_until_end(network, instructions))
    periods = steps_until_end_ghost(network, instructions)
    print(periods)

    steps = periods[0]
    keep_going = True
    while keep_going:
        if steps % periods[1] == 0 and steps % periods[2] == 0 and steps % periods[3] == 0 and steps % periods[4] == 0 and steps % periods[5] == 0:
            keep_going = False
        else:
            steps += periods[0]
    print(steps)


if __name__ == '__main__':
    run()
