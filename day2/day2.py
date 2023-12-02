INPUT_FILE = './input'
PART_1_LIMITS = {'red': 12, 'green': 13, 'blue': 14}


def is_showing_valid(showing, limits):
    for color_group in showing.split(', '):
        color_value, color = color_group.split(' ')
        if limits[color] < int(color_value):
            return False
    return True


def check_valid_game(line, limits):
    game_title, game_showings = line.split(': ')
    game_id = int(game_title.split(' ')[1])
    for showing in game_showings.split('; '):
        if not is_showing_valid(showing, limits):
            return None
    return game_id


def get_valid_games_from_file(filename, limits):
    valid_games = []
    with open(filename) as input:
        for line in input:
            game_id = check_valid_game(line.rstrip(), limits)
            if game_id is not None:
                valid_games.append(game_id)
    return valid_games


if __name__ == "__main__":
    valid_games = get_valid_games_from_file(INPUT_FILE, PART_1_LIMITS)
    print(sum(valid_games))