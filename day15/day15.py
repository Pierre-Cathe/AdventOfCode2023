from collections import OrderedDict

FILENAME = './input'
# FILENAME = './example'


def parse_data(filename):
    instructions = []
    with open(filename) as data:
        for line in data:
            instructions.extend(line.rstrip().split(','))
    return instructions


def h_a_s_h(string_to_hash):
    current_value = 0
    for char in string_to_hash:
        ascii_value = ord(char)
        current_value += ascii_value
        current_value *= 17
        current_value = current_value % 256
    return current_value


def run_instruction(instruction, boxes):

    label = instruction.split('-')[0]
    if '=' in label:
        label, focal_length = label.split('=')
        box_index = h_a_s_h(label)
        lenses = boxes[box_index]
        lenses[label] = int(focal_length)
    else:
        box_index = h_a_s_h(label)
        lenses = boxes[box_index]
        if label in lenses:
            del(lenses[label])


def run():
    instructions = parse_data(FILENAME)
    hashes = [h_a_s_h(instruction) for instruction in instructions]
    print(sum(hashes))

    boxes = {i: OrderedDict() for i in range(256)}
    for instruction in instructions:
        run_instruction(instruction, boxes)
    total_focusing_power = 0
    for box_index, lenses in boxes.items():
        lens_index = 1
        for lens_label, lens_focal_length in lenses.items():
            focusing_power = (1 + box_index) * (lens_index) * lens_focal_length
            total_focusing_power += focusing_power
            lens_index += 1
    print(total_focusing_power)


if __name__ == '__main__':
    run()
