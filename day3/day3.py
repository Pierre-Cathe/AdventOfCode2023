
FILENAME = './input'
# FILENAME = './example'
NUMBERS = "0123456789"
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def is_part_number(number_indexes, current_line, previous_line, next_line):
    start_index = 0 if number_indexes[0] == 0 else number_indexes[0] - 1
    end_index = len(current_line) if number_indexes[1] == len(current_line) else number_indexes[1] + 1
    for char in previous_line[start_index:end_index] + current_line[start_index] + current_line[end_index-1] + next_line[start_index:end_index]:
        if char not in NUMBERS + "." + LETTERS:
            return True
    return False


def get_part_numbers_in_line(current_line, previous_line, next_line):
    is_reading_number = False
    number_indexes = [None, None]
    part_numbers = []

    for char_index in range(len(current_line)):
        current_char = current_line[char_index]
        if current_char in NUMBERS and not is_reading_number:
            is_reading_number = True
            number_indexes[0] = char_index
        elif (current_char not in NUMBERS or char_index == len(current_line) - 1) and is_reading_number:
            is_reading_number = False
            number_indexes[1] = char_index
            if current_char in NUMBERS:
                number_indexes[1] += 1
            if is_part_number(number_indexes, current_line, previous_line, next_line):
                part_number = int(current_line[number_indexes[0]:number_indexes[1]])
                part_numbers.append(part_number)
    return part_numbers


def compute_gear_ratio(char_index, current_line, previous_line, next_line):
    adjacent_numbers = {}
    for line_index in (-1, 0, 1):
        line = [previous_line, current_line, next_line][line_index]
        for i in (-1, 0, 1):
            current_index = char_index + i
            if current_index == -1:
                continue
            if current_index == len(current_line):
                continue
            if line == '':
                continue
            if line[current_index] in NUMBERS:
                number_builder = line[current_index]
                number_coords = (line_index, current_index, current_index + 1)
                search_before = True
                search_index = current_index
                while search_before:
                    search_index -= 1
                    if search_index < 0:
                        break
                    search_char = line[search_index]
                    if search_char in NUMBERS:
                        number_builder = search_char + number_builder
                        number_coords = (number_coords[0], search_index, number_coords[2])
                    else:
                        search_before = False

                search_after = True
                search_index = current_index
                while search_after:
                    search_index += 1
                    if search_index == len(line):
                        break
                    search_char = line[search_index]
                    if search_char in NUMBERS:
                        number_builder = number_builder + search_char
                        number_coords = (number_coords[0], number_coords[1], search_index + 1)
                    else:
                        search_after = False
                adjacent_numbers[number_coords] = int(number_builder)
    if len(adjacent_numbers) == 2:
        product = 1
        for _, value in adjacent_numbers.items():
            product *= value
        return product
    return None


def get_gear_ratios_in_line(current_line, previous_line, next_line):
    gear_ratios = []

    for char_index in range(len(current_line)):
        current_char = current_line[char_index]
        if current_char == '*':
            gear_ratio = compute_gear_ratio(char_index, current_line, previous_line, next_line)
            if gear_ratio is not None:
                gear_ratios.append(gear_ratio)

    return gear_ratios


def run():
    all_part_numbers = []
    all_gear_ratios = []
    schematic = []
    with open(FILENAME) as data:
        for line in data:
            schematic.append(line.rstrip())
    for line_index in range(len(schematic)):
        previous_line = ''
        current_line = schematic[line_index]
        next_line = ''
        if line_index != 0:
            previous_line = schematic[line_index - 1]
        if line_index != len(schematic) - 1:
            next_line = schematic[line_index + 1]

        all_part_numbers.extend(get_part_numbers_in_line(current_line, previous_line, next_line))
        all_gear_ratios.extend(get_gear_ratios_in_line(current_line, previous_line, next_line))

    print(sum(all_gear_ratios))


if __name__ == '__main__':
    run()


