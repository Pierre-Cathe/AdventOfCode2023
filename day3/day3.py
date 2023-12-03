
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


def get_part_numbers(filename):
    part_numbers = []
    schematic = []
    with open(filename) as input:
        for line in input:
            schematic.append(line.rstrip())
    for line_index in range(len(schematic)):
        previous_line = ''
        current_line = schematic[line_index]
        next_line = ''
        if line_index != 0:
            previous_line = schematic[line_index-1]
        if line_index != len(schematic)-1:
            next_line = schematic[line_index+1]
        is_reading_number = False
        number_indexes = [None, None]

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



if __name__ == '__main__':
    all_part_numbers = get_part_numbers(FILENAME)
    print(sum(all_part_numbers))

