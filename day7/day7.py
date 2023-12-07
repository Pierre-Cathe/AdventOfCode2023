from tqdm import tqdm
from functools import cmp_to_key

FILENAME = './input'
# FILENAME = './example'

CARD_VALUES_ASC = '23456789TJQKA'
CARD_VALUES_ASC = 'J23456789TQKA'   # Part 2


FIVE_OF_A_KIND = 6
FOUR_OF_A_KIND = 5
FULL_HOUSE = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
PAIR = 1
HIGH_CARD = 0


def parse(filename):
    game_data = []
    with open(filename) as data:
        for line in data:
            hand, bid = line.rstrip().split(' ')
            game_data.append((hand, bid))
    return game_data


def get_hand_type(hand):
    number_of_copies = [0, 0, 0, 0, 0]
    most_present_non_joker = hand[0]
    max_number_of_copies = 0
    for i in range(len(hand)):
        for card in hand:
            if card == hand[i]:
                number_of_copies[i] += 1
                if number_of_copies[i] > max_number_of_copies and hand[i] != 'J':
                    max_number_of_copies = number_of_copies[i]
                    most_present_non_joker = hand[i]
    number_of_jokers = 0
    if 'J' in hand:
        number_of_jokers = number_of_copies[hand.index('J')]
    for i in range(len(hand)):
        if hand[i] == 'J' or hand[i] == most_present_non_joker:
            number_of_copies[i] = max_number_of_copies + number_of_jokers

    hand_repr = ''.join([str(x) for x in sorted(number_of_copies, reverse=True)])
    match hand_repr:
        case '55555':
            return FIVE_OF_A_KIND
        case '44441':
            return FOUR_OF_A_KIND
        case '33322':
            return FULL_HOUSE
        case '33311':
            return THREE_OF_A_KIND
        case '22221':
            return TWO_PAIR
        case '22111':
            return PAIR
        case '11111':
            return HIGH_CARD
        case _:
            raise ValueError(f"Hand {hand} with repr {hand_repr} was not recognized.")



def compare_games(game1, game2):
    hand1, _ = game1
    hand2, _ = game2
    type_hand1 = get_hand_type(hand1)
    type_hand2 = get_hand_type(hand2)
    if type_hand1 != type_hand2:
        return -1 if type_hand1 < type_hand2 else 1
    for i in range(len(hand1)):
        card1_value = CARD_VALUES_ASC.index(hand1[i])
        card2_value = CARD_VALUES_ASC.index(hand2[i])
        if card1_value != card2_value:
            return -1 if card1_value < card2_value else 1
    return 0


def run():
    print('Reading data')
    game_data = parse(FILENAME)
    # print(game_data)
    print('Sorting data')
    sorted_part_1 = sorted(game_data, key= cmp_to_key(compare_games))
    # print(sorted_part_1)
    winnings = 0
    for i in range(len(sorted_part_1)):
        _, bid = sorted_part_1[i]
        winnings += int(bid) * (i + 1)
    print(winnings)


if __name__ == '__main__':
    run()
