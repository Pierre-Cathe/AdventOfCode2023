

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
    new_platform = ['' for x in range(len(platform))]
    for x in range(len(platform)):
        new_platform[x] = ''.join([platform[(len(platform)-t)-1][x] for t in range(len(platform))])
    return new_platform


def cycle(platform):
    for i in range(4):
        roll_north(platform)
        platform = rotate_clockwise(platform)
    return platform


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
    # roll_north(platform)
    iterations = 0
    seen_platforms = []
    loads = []
    while iterations < 1_000_000_000:
        platform = cycle(platform)
        iterations += 1
        string_rep = '\n'.join(platform)
        #print(string_rep + '\n')
        if ''.join(platform) in seen_platforms:
            print(iterations)
            print(seen_platforms.index(''.join(platform)))
            break
        seen_platforms.append(''.join(platform))
        loads.append(calculate_load(platform))
    start_of_loop = seen_platforms.index(''.join(platform)) + 1
    period = iterations - start_of_loop
    looping_iterations = 1_000_000_000 - start_of_loop
    loop_modulus = looping_iterations % period
    platform_at_billion_string_form = seen_platforms[start_of_loop + loop_modulus]
    platform_at_billion = []
    for x in range(len(platform)):
        platform_at_billion.append(platform_at_billion_string_form[x*len(platform):x*len(platform) + len(platform)])

    load = loads[start_of_loop+loop_modulus-1]
    print('\n'.join(platform_at_billion))
    print(load)

    pass

if __name__ == '__main__':
    run()
