

FILENAME = "./data"
digit_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', *[x for x in '0123456789']]
digit_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    **{x: x for x in '0123456789'}
}

def is_digit(char):
    return char in "0123456789"

def get_digit_at_index_if_exists(line, i):
    maybe_digit = line[i:]
    for digit_representation, digit_value in digit_dict.items():
        if maybe_digit.startswith(digit_representation):
            return digit_value
    return ''

def extract_number_from_first_and_last_digit(line):
    first_digit = ''
    last_digit = ''
    for i in range(len(line)):
        # this code for part 1
        # char = line[i]
        # if is_digit(char):
        #     if first_digit == '':
        #         first_digit = char
        #     last_digit = char

        # this code for part 2
        digit_str = get_digit_at_index_if_exists(line, i)
        if digit_str != '':
            if first_digit == '':
                first_digit = digit_str
            last_digit = digit_str
    return int('' + first_digit + last_digit)


def get_summed_value_from_file(file_name):
    summed_value = 0
    with open(file_name) as data:
        for line in data:
            line_value = extract_number_from_first_and_last_digit(line)
            summed_value += line_value
    return summed_value



if __name__ == "__main__":
    value = get_summed_value_from_file(FILENAME)
    print(value)