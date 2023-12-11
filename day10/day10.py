

FILENAME = './input'
# FILENAME = './example5'

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
    for line in lines :
        print(line)


def is_right_facing(pipe):
    return pipe in '-LF'


def is_down_facing(pipe):
    return pipe in '|7F'


def is_left_facing(pipe):
    return pipe in '-J7'


def is_up_facing(pipe):
    return pipe in '|LJ'


def get_start_pipe(loop, maze, start_pos):
    neighbor1_dir = (loop[1][0] - start_pos[0], loop[1][1] - start_pos[1])
    neighbor2_dir = (loop[-1][0] - start_pos[0], loop[-1][1] - start_pos[1])
    for pipe, directions in NEIGHBOURS.items():
        if directions == (neighbor1_dir, neighbor2_dir) or directions == (neighbor2_dir, neighbor1_dir):
            return pipe
    raise ValueError()


# Determine, for each vertical and horizontal transition, if it is inside or outside the loop
# Squares fully inside the loop are surrounded with "inside" transitions
def find_inside_squares(loop, maze, start_pos):
    start_pipe = get_start_pipe(loop, maze, start_pos)
    inside_squares = []
    for x in range(len(maze)):
        full_pipes_met = 0
        half_pipes_met = []

        for y in range(len(maze[0])):
            current_pipe = maze[x][y]
            if current_pipe == 'S':
                current_pipe = start_pipe
                maze[x] = maze[x][:y] + start_pipe + maze[x][y + 1:]
            if (x, y) not in loop:
                if full_pipes_met % 2 == 1:
                    inside_squares.append((x, y))
            else:
                if current_pipe == '|':
                    full_pipes_met += 1
                elif current_pipe in 'F7LJ':
                    if len(half_pipes_met) == 0:
                        half_pipes_met.append(current_pipe)
                    else:
                        if is_up_facing(current_pipe) != is_up_facing(half_pipes_met[0]):
                            full_pipes_met += 1
                        half_pipes_met = []

    return inside_squares


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

    inside_squares = find_inside_squares(loop, maze, start_pos)
    print(inside_squares)
    print(len(inside_squares))


if __name__ == '__main__':
    run()
