import itertools

from utils import read_lines


def part1(filename="input.txt"):
    lines = read_lines(filename)
    new_values = []
    histories = [list(map(int, line.split())) for line in lines]
    for history in histories:
        levels = [history]
        while any(levels[-1]):
            current_level = []
            for left, right in itertools.pairwise(levels[-1]):
                current_level.append(right - left)
            levels.append(current_level)

        last_level = levels[-1]
        last_level.append(0)
        for level in levels[-2::-1]:
            level.append(last_level[-1] + level[-1])
            last_level = level
        new_values.append(levels[0][-1])

    answer = sum(new_values)
    print(f"part1 for {filename}: {answer}")
    return answer


def part2(filename="input.txt"):
    lines = read_lines(filename)
    new_values = []
    histories = [list(map(int, line.split())) for line in lines]
    for history in histories:
        levels = [history]
        while any(levels[-1]):
            current_level = []
            for left, right in itertools.pairwise(levels[-1]):
                current_level.append(right - left)
            levels.append(current_level)

        last_level = levels[-1]
        last_level.insert(0, 0)
        for level in levels[-2::-1]:
            level.insert(0, level[0] - last_level[0])
            last_level = level
        new_values.append(levels[0][0])

        # for i, level in enumerate(levels):
        #     print((" " * i) + " ".join(map(str, level)))

    answer = sum(new_values)
    print(f"part1 for {filename}: {answer}")
    return answer


if __name__ == "__main__":
    assert part1("example1.txt") == 114
    assert part1() == 1939607039

    assert part2("example1.txt") == 2
    assert part2() == 1041
