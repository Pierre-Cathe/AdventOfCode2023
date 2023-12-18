from dataclasses import dataclass, field
from typing import Any
from queue import PriorityQueue


@dataclass(order=True)
class Node:
    estimated_value: int
    x: Any = field(compare=False)
    y: Any = field(compare=False)
    straights: Any = field(compare=False)
    direction: Any = field(compare=False)
    prev_node: Any = field(compare=False)
    cost: Any = field(compare=False)

    def get_simple_node(self):
        return self.x, self.y, self.straights, self.direction


class Directions:
    RIGHT, LEFT, UP, DOWN = (0, 1), (0, -1), (-1, 0), (1, 0)


def get_opposite_direction(direction):
    match direction:
        case Directions.LEFT:
            return Directions.RIGHT
        case Directions.RIGHT:
            return Directions.LEFT
        case Directions.UP:
            return Directions.DOWN
        case Directions.DOWN:
            return Directions.UP
    return None


FILENAME = './input'
FILENAME = './example'


def parse_data(filename):
    heat_map = []
    with open(filename) as data:
        for line in data:
            heat_map.append(line.rstrip())
    return heat_map


def generate_neighbors(heat_map, node: Node):
    x, y, straights, direction, cost_so_far = node.x, node.y, node.straights, node.direction, node.cost
    possible_dirs = (Directions.UP, Directions.RIGHT, Directions.DOWN, Directions.LEFT)
    opposite_dir = get_opposite_direction(direction)
    neighbors = []
    for possible_dir in possible_dirs:
        if 0 <= x + possible_dir[0] < len(heat_map) and 0 <= y + possible_dir[1] < len(heat_map[0]):
            new_x, new_y = x+possible_dir[0], y+possible_dir[1]
            new_cost = cost_so_far + int(heat_map[new_x][new_y])
            est_value = new_cost + (len(heat_map)-1) - new_x + (len(heat_map[0])-1) - new_y
            if possible_dir == direction:
                if straights < 3:
                    neighbor = Node(est_value, new_x, new_y, straights+1, possible_dir, node, new_cost)
                    neighbors.append(neighbor)
            elif possible_dir == opposite_dir:
                pass
            else:
                neighbor = Node(est_value, new_x, new_y, 1, possible_dir, node, new_cost)
                neighbors.append(neighbor)
    return neighbors


def display(nodes, heat_map):
    coords = []
    for node in nodes:
        x, y, _, direction = node
        coords.append((x, y))
    sb = []
    for x in range(len(heat_map)):
        for y in range(len(heat_map[0])):
            if (x, y) in coords:
                sb.append('*')
            else:
                sb.append('.')
        sb.append('\n')
    sb.append('\n')
    print(''.join(sb))


def find_best_path(heat_map, start_pos, end_pos, max_contiguous_moves):
    visited_nodes = []
    nodes_to_visit = PriorityQueue()
    start_node = Node(0, 0, 0, 0, None, None, 0)
    for node in generate_neighbors(heat_map, start_node):
        nodes_to_visit.put(node)

    while nodes_to_visit.qsize() != 0:
        display(visited_nodes, heat_map)
        node = nodes_to_visit.get()

        if (node.x, node.y) == (len(heat_map)-1, len(heat_map[0])-1):
            return node
        else:
            visited_nodes.append(node.get_simple_node())
            neighbors = generate_neighbors(heat_map, node)
            for neighbor in neighbors:
                if neighbor.get_simple_node() not in visited_nodes:
                    nodes_to_visit.put(neighbor)
    return None


def run():
    heat_map = parse_data(FILENAME)
    optimal_path_heat_loss = find_best_path(heat_map, (0, 0), (len(heat_map), len(heat_map[0])), 3)
    print(optimal_path_heat_loss)


if __name__ == '__main__':
    run()
