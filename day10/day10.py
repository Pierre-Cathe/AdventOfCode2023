

FILENAME = './input'
# FILENAME = './example1'

NEIGHBOURS = {
    '|': ((-1, 0), (1, 0)),
    '-': ((0, -1), (0, 1)),
    'L': ((-1, 0), (0, 1)),
    'J': ((-1, 0), (0, -1)),
    '7': ((1, 0), (0, -1)),
    'F': ((1, 0), (0, 1)),
    '.': ((0, 0), (0, 0))
}


def read_maze(filename):
    maze = []
    start_pos = (0, 0)
    line_index = 0
    with open(filename) as data:
        for raw_line in data:
            line = raw_line.rstrip()
            maze.append(line)
            if 'S' in line:
                start_pos = (line_index, line.index('S'))
            else:
                line_index += 1
    return maze, start_pos


def add_coords(coords1, coords2):
    return (coords1[0] + coords2[0], coords1[1] + coords2[1])


def connects_to(node, node_pos, neighbour_pos):
    for neighbour_dir in NEIGHBOURS[node]:
        if add_coords(node_pos, neighbour_dir) == neighbour_pos:
            return True
    return False


def explore_loop(start_pos, neighbour_pos, maze):
    loop = [start_pos]
    current_pos = start_pos
    next_pos = neighbour_pos
    while next_pos != start_pos:
        loop.append(next_pos)
        current_pos = next_pos
        current_node = maze[current_pos[0]][current_pos[1]]
        prev_node_dir = (loop[-2][0] - current_pos[0], loop[-2][1] - current_pos[1])
        next_dir = None
        for direction in NEIGHBOURS[current_node]:
            if direction != prev_node_dir:
                next_dir = direction
                break
        next_pos = add_coords(current_pos, next_dir)
    return loop


def show_loop(loop, maze):
    lines = []
    for x in range(len(maze)):
        line = []
        for y in range(len(maze[0])):
            if (x, y) in loop:
                line.append(maze[x][y])
            else:
                line.append('.')
        lines.append(''.join(line))
    print('\n'.join(lines))


def run():
    maze, start_pos = read_maze(FILENAME)
    print(start_pos)

    loop = []
    for neighbour_dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        neighbour_pos = add_coords(start_pos, neighbour_dir)
        if connects_to(maze[neighbour_pos[0]][neighbour_pos[1]], neighbour_pos, start_pos):
            loop = explore_loop(start_pos, neighbour_pos, maze)
            break
    show_loop(loop, maze)
    print(len(loop) // 2)


if __name__ == '__main__':
    run()
