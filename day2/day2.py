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


def get_games_from_file(filename):
    games = []
    with open(filename) as input:
        for line in input:
            games.append(parse_game(line.rstrip()))
    return games


def get_id_if_valid(game, limits):
    game_id, showings = game
    for showing in showings:
        for color, color_value in showing.items():
            if limits[color] < color_value:
                return 0
    return game_id


if __name__ == "__main__":
    all_games = get_games_from_file(INPUT_FILE)
    all_valid_games = list(map(partial(get_id_if_valid, limits=PART_1_LIMITS), all_games))
    print(sum(all_valid_games))