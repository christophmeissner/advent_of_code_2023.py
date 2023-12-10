from collections import defaultdict

from utils import read_lines

is_symbol = lambda s: not (s.isdigit() or s == ".")
is_gear = lambda s: s == "*"

assert is_symbol("$") is True
assert is_symbol("1") is False
assert is_symbol(".") is False
assert is_gear("$") is False
assert is_gear("1") is False
assert is_gear(".") is False
assert is_gear("*") is True

DIRECTIONS = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)


def connects_symbol(coord, lines, test):
    len_y, len_x = len(lines), len(lines[0])
    for neighbor in [(d[0] + coord[0], d[1] + coord[1]) for d in DIRECTIONS]:
        x, y = neighbor
        if 0 <= y < len_y and 0 <= x < len_x and test(lines[y][x]):
            return (x, y)
    return None


assert connects_symbol((0, 0), read_lines("example1.txt"), is_symbol) is None
assert connects_symbol((1, 0), read_lines("example1.txt"), is_symbol) is None
assert connects_symbol((2, 0), read_lines("example1.txt"), is_symbol) == (3, 1)
assert connects_symbol((3, 0), read_lines("example1.txt"), is_symbol) == (3, 1)
assert connects_symbol((4, 0), read_lines("example1.txt"), is_symbol) == (3, 1)
assert connects_symbol((5, 0), read_lines("example1.txt"), is_symbol) is None
assert connects_symbol((2, 1), read_lines("example1.txt"), is_symbol) == (3, 1)
assert connects_symbol((3, 1), read_lines("example1.txt"), is_symbol) is None
assert connects_symbol((4, 1), read_lines("example1.txt"), is_symbol) == (3, 1)
assert connects_symbol((3, 2), read_lines("example1.txt"), is_symbol) == (3, 1)


def part1(filename="input.txt"):
    answer = 0
    lines = read_lines(filename)
    for y, line in enumerate(lines):
        numbers_on_line = []
        current_number, adjacent = "", False
        for x, char in enumerate(line + "."):
            if char.isdigit():
                if not adjacent:
                    adjacent = connects_symbol((x, y), lines, is_symbol)
                current_number += char
            elif current_number:
                if adjacent:
                    numbers_on_line.append(int(current_number))
                current_number, adjacent = "", False
        answer += sum(numbers_on_line)
    print(f"part1 for {filename}: {answer}")
    return answer


def part2(filename="input.txt"):
    lines = read_lines(filename)
    gears = defaultdict(list)
    for y, line in enumerate(lines):
        current_number, gear = "", None
        for x, char in enumerate(line + "."):
            if char.isdigit():
                if gear is None:
                    gear = connects_symbol((x, y), lines, is_gear)
                current_number += char
            elif current_number:
                if gear is not None:
                    gears[gear].append(int(current_number))
                current_number, gear = "", None
    answer = sum(a * b for a, b in filter(lambda t: len(t) == 2, gears.values()))
    print(f"part2 for {filename}: {answer}")
    return answer


if __name__ == "__main__":
    assert part1("example1.txt") == 4361
    part1()

    assert part2("example2.txt") == 467835
    part2()
