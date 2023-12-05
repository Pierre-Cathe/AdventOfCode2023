

FILENAME = './input'


def clean_up_numbers(raw_numbers):
    return [int(number) for number in raw_numbers.split(' ') if number != '']

def parse_card_value(line):
    card_title, all_numbers = line.split(': ')
    card_id = ''
    for item in card_title.split(' '):
        if item != '':
            card_id = item
    raw_winning_numbers, raw_numbers_you_have = all_numbers.split('|')
    winning_numbers = clean_up_numbers(raw_winning_numbers)
    numbers_you_have = clean_up_numbers(raw_numbers_you_have)
    numbers_you_have_that_are_winning = [number for number in numbers_you_have if number in winning_numbers]
    if len(numbers_you_have_that_are_winning) > 0:
        return pow(2, len(numbers_you_have_that_are_winning) - 1)
    return 0


def run():
    card_values = []
    with open(FILENAME) as data:
        for line in data:
            card_value = parse_card_value(line.rstrip())
            card_values.append(card_value)
    print(sum(card_values))


if __name__ == '__main__':
    run()
