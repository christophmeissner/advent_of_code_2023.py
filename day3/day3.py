import string

from utils import read_lines

is_digit = lambda s: s in string.digits
is_symbol = lambda s: not is_digit(s) and s != "."
is_gear = lambda s: s == "*"

assert is_symbol("$") is True
assert is_digit("$") is False
assert is_symbol("1") is False
assert is_digit("2") is True
assert is_symbol(".") is False
assert is_digit(".") is False

directions = (
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    # (0, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
)


def is_connected(coordinate, matrix, test):
    column, line = coordinate
    max_y = len(matrix) - 1
    for dx, dy in directions:
        x, y = dx + column, dy + line
        if y > max_y or y < 0:
            continue
        max_x = len(matrix[y]) - 1
        if x > max_x or x < 0:
            continue
        if test(matrix[y][x]):
            return (y, x)
    return None


def part1():
    lines = read_lines("input.txt")
    total = 0
    for y, line in enumerate(lines):
        current_number = 0
        has_symbol = False
        for x, char in enumerate(line + "."):
            if is_digit(char):
                current_number = current_number * 10 + int(char)
                if not has_symbol:
                    has_symbol = is_connected((x, y), lines, is_symbol)
            elif not current_number == 0:
                if has_symbol:
                    total += current_number
                current_number = 0
                has_symbol = False
    return total


def part2():
    lines = read_lines("input.txt")
    gears = dict()
    for y, line in enumerate(lines):
        current_number = 0
        gear = None
        for x, char in enumerate(line + "."):
            if is_digit(char):
                current_number = current_number * 10 + int(char)
                if not gear:
                    gear = is_connected((x, y), lines, is_gear)
            elif not current_number == 0:
                if gear:
                    number_list = gears.get(gear, [])
                    number_list.append(current_number)
                    gears[gear] = number_list
                current_number = 0
                gear = None
    return sum(
        map(lambda g: g[0] * g[1], filter(lambda v: len(v) == 2, gears.values()))
    )


if __name__ == "__main__":
    print(f"part 1: {part1()}")
    print(f"part 2: {part2()}")
