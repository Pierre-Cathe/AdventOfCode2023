

FILENAME = './input'
# FILENAME = './example'


def parse_data(filename):
    platform = []
    with open(filename) as data:
        for line in data:
            platform.append(line.rstrip())
    return platform


def set_rock_at_coords(x, y, rock, platform):
    platform[x] = platform[x][:y] + rock + platform[x][y+1:]


def roll_north(platform):
    most_recent_rock_encountered = [-1 for y in range(len(platform[0]))]
    for x in range(len(platform)):
        for y in range(len(platform[0])):
            current_char = platform[x][y]
            if current_char == '#':
                most_recent_rock_encountered[y] = x
            elif current_char == 'O':
                if most_recent_rock_encountered[y] != x-1:
                    set_rock_at_coords(most_recent_rock_encountered[y]+1, y, 'O', platform)
                    set_rock_at_coords(x, y, '.', platform)
                    most_recent_rock_encountered[y] = most_recent_rock_encountered[y]+1
                else:
                    most_recent_rock_encountered[y] = x
    return platform


def rotate_clockwise(platform):
    pass


def cycle(platform):


def calculate_load(platform):
    load = 0
    line_load = 1
    for x in range(len(platform)-1, -1, -1):
        for y in range(len(platform[0])):
            if platform[x][y] == 'O':
                load += line_load
        line_load += 1
    return load


def run():
    platform = parse_data(FILENAME)
    seen_platform = []
    roll_north(platform)
    for line in platform:
        print(line)
    load = calculate_load(platform)
    print(load)


if __name__ == '__main__':
    run()