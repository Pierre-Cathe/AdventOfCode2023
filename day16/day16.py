

FILENAME = './input'
FILENAME = './example'

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
            x += direction[0]
            y += direction[1]
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



def run():
    contraption = parse_data(FILENAME)
    seen_tiles_and_directions = set()
    simulate_beam(contraption, 0, 0, Directions.RIGHT, seen_tiles_and_directions)
    energised_tiles = []
    for x, y, direction in seen_tiles_and_directions:
        if (x, y) not in energised_tiles:
            energised_tiles.append((x, y))
    print(len(energised_tiles))


if __name__ == '__main__':
    run()
