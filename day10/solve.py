from utils import read_lines

TILES = "|-LJ7F.S"
PRETTY_TILES = "│─└┘┐┌ █"

UP, DOWN, LEFT, RIGHT = (0, -1), (0, 1), (-1, 0), (1, 0)
DIRECTIONS = [UP, DOWN, LEFT, RIGHT]
PIPES = {
    "|": {UP, DOWN},
    "-": {LEFT, RIGHT},
    "L": {UP, RIGHT},
    "J": {UP, LEFT},
    "7": {DOWN, LEFT},
    "F": {DOWN, RIGHT},
}


def print_maze(lines):
    for line in lines:
        print("".join(map(lambda c: PRETTY_TILES[TILES.index(c)], line)))


def flip(direction):
    return direction[0] * -1, direction[1] * -1


def part1(filename="input.txt"):
    with open(filename) as input_file:
        content = input_file.read()
    lines = content.split("\n")

    start_index = content.index("S")
    start_xy = start_index % (len(lines[0]) + 1), content[:start_index].count("\n")

    # find direction of any pipe connected to S
    start_direction = None
    for direction in DIRECTIONS:
        x, y = start_xy[0] + direction[0], start_xy[1] + direction[1]
        if 0 <= y < len(lines) and 0 <= x < len(lines[0]):
            if lines[y][x] in PIPES:
                if flip(direction) in PIPES[lines[y][x]]:
                    start_direction = direction
                    break

    # count steps for loop
    direction = start_direction
    x, y = start_xy[0] + direction[0], start_xy[1] + direction[1]
    steps = 1
    while (x, y) != start_xy:
        next_connections = set(PIPES[lines[y][x]])
        next_connections.remove(flip(direction))
        direction = next_connections.pop()
        x, y = x + direction[0], y + direction[1]
        steps += 1

    answer = int(steps / 2)
    print(f"part1 for {filename}: {answer}")
    return answer


def part2(filename="input.txt"):
    lines = read_lines(filename)
    answer = 0
    for line in lines:
        pass
    print(f"part2 for {filename}: {answer}")
    return answer


if __name__ == "__main__":
    assert part1("example1.txt") == 4
    assert part1("example2.txt") == 8
    assert part1() == 6890

    assert part2("example2.txt") == 0
    part2()
