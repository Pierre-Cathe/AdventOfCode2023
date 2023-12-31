from tqdm import tqdm

FILENAME = './input'
# FILENAME = './example'


class Directions:
    RIGHT, LEFT, UP, DOWN = (0, 1), (0, -1), (-1, 0), (1, 0)


def parse_data(filename):
    contraption = []
    with open(filename) as data:
        for line in data:
            contraption.append(line.rstrip())
    return contraption


def simulate_beam(contraption, x, y, direction, seen_tiles_and_directions):
    if (x, y, direction) not in seen_tiles_and_directions:
        seen_tiles_and_directions.add((x, y, direction))
    else:
        return
    match contraption[x][y]:
        case '.':

            tile = contraption[x][y]
            while tile == '.':
                seen_tiles_and_directions.add((x, y, direction))
                x += direction[0]
                y += direction[1]
                if 0 <= x < len(contraption) and 0 <= y < len(contraption[0]):
                    tile = contraption[x][y]
                else:
                    break
            if 0 <= x < len(contraption) and 0 <= y < len(contraption[0]):
                simulate_beam(contraption, x, y, direction, seen_tiles_and_directions)
        case '/':
            match direction:
                case Directions.UP:
                    direction = Directions.RIGHT
                case Directions.DOWN:
                    direction = Directions.LEFT
                case Directions.LEFT:
                    direction = Directions.DOWN
                case Directions.RIGHT:
                    direction = Directions.UP
            x += direction[0]
            y += direction[1]
            if 0 <= x < len(contraption) and 0 <= y < len(contraption[0]):
                simulate_beam(contraption, x, y, direction, seen_tiles_and_directions)
        case '\\':
            match direction:
                case Directions.UP:
                    direction = Directions.LEFT
                case Directions.DOWN:
                    direction = Directions.RIGHT
                case Directions.LEFT:
                    direction = Directions.UP
                case Directions.RIGHT:
                    direction = Directions.DOWN
            x += direction[0]
            y += direction[1]
            if 0 <= x < len(contraption) and 0 <= y < len(contraption[0]):
                simulate_beam(contraption, x, y, direction, seen_tiles_and_directions)
        case '-':
            match direction:
                case Directions.UP | Directions.DOWN:
                    y1, y2 = y + 1, y - 1
                    if 0 <= x < len(contraption) and 0 <= y1 < len(contraption[0]):
                        simulate_beam(contraption, x, y1, Directions.RIGHT, seen_tiles_and_directions)
                    if 0 <= x < len(contraption) and 0 <= y2 < len(contraption[0]):
                        simulate_beam(contraption, x, y2, Directions.LEFT, seen_tiles_and_directions)
                case Directions.RIGHT | Directions.LEFT:
                    x += direction[0]
                    y += direction[1]
                    if 0 <= x < len(contraption) and 0 <= y < len(contraption[0]):
                        simulate_beam(contraption, x, y, direction, seen_tiles_and_directions)
        case '|':
            match direction:
                case Directions.RIGHT | Directions.LEFT:
                    x1, x2 = x + 1, x - 1
                    if 0 <= x1 < len(contraption) and 0 <= y < len(contraption[0]):
                        simulate_beam(contraption, x1, y, Directions.DOWN, seen_tiles_and_directions)
                    if 0 <= x2 < len(contraption) and 0 <= y < len(contraption[0]):
                        simulate_beam(contraption, x2, y, Directions.UP, seen_tiles_and_directions)
                case Directions.UP | Directions.DOWN:
                    x += direction[0]
                    y += direction[1]
                    if 0 <= x < len(contraption) and 0 <= y < len(contraption[0]):
                        simulate_beam(contraption, x, y, direction, seen_tiles_and_directions)


def compute_energised_tiles(contraption, start_x, start_y, start_dir):
    seen_tiles_and_directions = set()
    simulate_beam(contraption, start_x, start_y, start_dir, seen_tiles_and_directions)
    energised_tiles = []
    for x, y, direction in seen_tiles_and_directions:
        if (x, y) not in energised_tiles:
            energised_tiles.append((x, y))
    return len(energised_tiles)


def run():
    contraption = parse_data(FILENAME)
    total_energised_tiles = []
    for x in tqdm(range(len(contraption))):
        total_energised_tiles.append(compute_energised_tiles(contraption, x, 0, Directions.RIGHT))
        total_energised_tiles.append(compute_energised_tiles(contraption, x, len(contraption[0])-1, Directions.LEFT))
    for y in tqdm(range(len(contraption[0]))):
        total_energised_tiles.append(compute_energised_tiles(contraption, 0, y, Directions.DOWN))
        total_energised_tiles.append(compute_energised_tiles(contraption, len(contraption)-1, y, Directions.UP))
    print(max(total_energised_tiles))


if __name__ == '__main__':
    run()
