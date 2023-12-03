from functools import partial

INPUT_FILE = './input'
PART_1_LIMITS = {'red': 12, 'green': 13, 'blue': 14}


def parse_showing(showing):
    color_values = {}
    for color_group in showing.split(', '):
        color_value, color = color_group.split(' ')
        color_values[color] = int(color_value)
    return color_values


def parse_game(line):
    game_title, game_showings = line.split(': ')
    game_id = int(game_title.split(' ')[1])
    showings = []
    for showing in game_showings.split('; '):
        showings.append(parse_showing(showing))
    return game_id, showings


def parse_games_from_file(filename):
    games = []
    with open(filename) as data:
        for line in data:
            games.append(parse_game(line.rstrip()))
    return games


def get_id_if_valid(game, limits):
    game_id, showings = game
    for showing in showings:
        for color, color_value in showing.items():
            if limits[color] < color_value:
                return 0
    return game_id


def get_minimal_set_power(game):
    minimal_set = {}
    _, showings = game
    for showing in showings:
        for color, color_value in showing.items():
            if not color in minimal_set:
                minimal_set[color] = color_value
            if color_value > minimal_set[color]:
                minimal_set[color] = color_value
    set_power = 1
    for _, color_value in minimal_set.items():
        set_power *= color_value
    return set_power


if __name__ == "__main__":
    all_games = parse_games_from_file(INPUT_FILE)
    all_valid_games = list(map(partial(get_id_if_valid, limits=PART_1_LIMITS), all_games))
    print(sum(all_valid_games))
    game_minimal_sets_powers = list(map(get_minimal_set_power, all_games))
    print(sum(game_minimal_sets_powers))