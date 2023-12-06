

FILENAME = './input'


def clean_up_numbers(raw_numbers):
    return [int(number) for number in raw_numbers.split(' ') if number != '']


def parse_races(filename):
    with open(filename) as data:
        for raw_line in data:
            line = raw_line.rstrip()
            numbers = clean_up_numbers(line.split(':')[1])
            if 'Time' in line:
                races = numbers
            if 'Distance' in line:
                for i in range(len(numbers)):
                    races[i] = (races[i], numbers[i])
    return races


def can_beat_record(time_pressed, time_available, record_distance):
    distance_made = time_pressed * (time_available - time_pressed)
    return distance_made > record_distance


def compute_number_of_ways_to_win(race):
    time_available, record_distance = race
    possible_wins = 0
    for time_pressed in range(int(time_available/2), 0, -1):
        if can_beat_record(time_pressed, time_available, record_distance):
            possible_wins += 2
        else:
            break
    if time_available % 2 == 0:
        possible_wins -= 1
    return possible_wins


def run():
    races = parse_races(FILENAME)
    print(races)

    number_of_ways_to_win = []
    product = 1
    for race in races:
        ways_to_win = compute_number_of_ways_to_win(race)
        number_of_ways_to_win.append(ways_to_win)
        product *= ways_to_win
    print(number_of_ways_to_win)
    print(product)



if __name__ == '__main__':
    run()
