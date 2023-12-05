

FILENAME = './input'
# FILENAME = './example'


def clean_up_numbers(raw_numbers):
    return [int(number) for number in raw_numbers.split(' ') if number != '']

def parse_card(line):
    card_title, all_numbers = line.split(': ')
    card_id = ''
    for item in card_title.split(' '):
        if item != '':
            card_id = item
    raw_winning_numbers, raw_numbers_you_have = all_numbers.split('|')
    winning_numbers = clean_up_numbers(raw_winning_numbers)
    numbers_you_have = clean_up_numbers(raw_numbers_you_have)
    numbers_you_have_that_are_winning = [number for number in numbers_you_have if number in winning_numbers]
    return card_id, winning_numbers, numbers_you_have, numbers_you_have_that_are_winning

def get_card_value(numbers_you_have_that_are_winning):
    if len(numbers_you_have_that_are_winning) > 0:
        return pow(2, len(numbers_you_have_that_are_winning) - 1)
    return 0


def run():
    card_values = []
    card_amounts = []
    line_index = 0
    with open(FILENAME) as data:
        for line in data:
            if len(card_amounts) <= line_index:
                card_amounts.append(1)
            else:
                card_amounts[line_index] += 1

            card_id, winning_numbers, numbers_you_have, numbers_you_have_that_are_winning = parse_card(line.rstrip())
            card_value = get_card_value(numbers_you_have_that_are_winning)
            card_values.append(card_value)


            for i in range(1, len(numbers_you_have_that_are_winning)+1):
                if len(card_amounts) <= line_index + i:
                    card_amounts.append(card_amounts[line_index])
                else:
                    card_amounts[line_index+i] += card_amounts[line_index]
            line_index += 1


    print(sum(card_values))
    print(len(card_amounts))
    print(sum(card_amounts))


if __name__ == '__main__':
    run()
