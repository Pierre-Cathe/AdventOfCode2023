

FILENAME = './input'
# FILENAME = './example'

EXPANSION_FACTOR = 999_999
#EXPANSION_FACTOR = 99


def parse_data(filename):
    universe = []
    with open(filename) as data:
        for raw_line in data:
            universe.append(raw_line.rstrip())
    return universe


def expand(universe):
    expanded_universe = []
    for i in range(len(universe)):
        if '#' not in universe[i]:
            expanded_universe.append(universe[i])
        expanded_universe.append(universe[i])
    for i in range(len(expanded_universe[0])-1, -1, -1):
        col = [line[i] for line in expanded_universe]
        if '#' not in col:
            for j in range(len(expanded_universe)):
                expanded_universe[j] = expanded_universe[j][:i] + '.' + expanded_universe[j][i:]
    return expanded_universe


def get_galaxies_locations(universe):
    galaxies = []
    for x in range(len(universe)):
        for y in range(len(universe[0])):
            if universe[x][y] == '#':
                galaxies.append((x, y))
    return galaxies


def get_manhattan_distance(galaxy_1, galaxy_2):
    x1, y1 = galaxy_1
    x2, y2 = galaxy_2
    return abs(x1 - x2) + abs(y1 - y2)


def expand_galaxies_coords(universe, galaxies, expansion_factor):
    lines_to_expand = []
    cols_to_expand = []
    for i in range(len(universe)):
        if '#' not in universe[i]:
            lines_to_expand.append(i)
    for i in range(len(universe[0])):
        col = [line[i] for line in universe]
        if '#' not in col:
            cols_to_expand.append(i)
    new_galaxies = []
    for galaxy in galaxies:
        x, y = galaxy
        new_x, new_y = x, y
        for line in lines_to_expand:
            if line < x:
                new_x += expansion_factor
        for col in cols_to_expand:
            if col < y:
                new_y += expansion_factor
        new_galaxies.append((new_x, new_y))
    return new_galaxies


def run():
    universe = parse_data(FILENAME)

    # Naive part 1 method
    # expanded_universe = expand(universe)
    # for line in expanded_universe:
    #     print(line)
    # shortest_paths = {}
    # galaxies = get_galaxies_locations(expanded_universe)

    galaxies = get_galaxies_locations(universe)
    galaxies = expand_galaxies_coords(universe, galaxies, EXPANSION_FACTOR)

    shortest_paths = {}
    for starting_galaxy in galaxies:
        for other_galaxy in galaxies:
            if starting_galaxy != other_galaxy:
                if (starting_galaxy, other_galaxy) not in shortest_paths and (other_galaxy, starting_galaxy) not in shortest_paths:
                    distance = get_manhattan_distance(starting_galaxy, other_galaxy)
                    shortest_paths[(starting_galaxy, other_galaxy)] = distance

    paths_sum = 0
    for key, value in shortest_paths.items():
        paths_sum += value
    print(paths_sum)


if __name__ == '__main__':
    run()
