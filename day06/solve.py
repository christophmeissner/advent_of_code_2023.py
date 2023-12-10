import functools
import math
import operator

from utils import read_lines


def count(time, dist):
    minimum = int((time - math.sqrt((time**2) - (dist * 4))) / 2.0)
    dist = (time - minimum) * minimum  # actual dist, when button pressed for min_p
    maximium = ((math.sqrt((time**2) - (4 * dist)) + time) / 2.0) - 1
    answer = int(maximium - minimum)
    return answer


def part1(filename="input.txt"):
    lines = read_lines(filename)
    times = map(int, lines[0].split(": ")[-1].split())
    distances = map(int, lines[1].split(": ")[-1].split())
    answer = functools.reduce(
        operator.mul, [count(time, dist) for time, dist in zip(times, distances)]
    )
    print(f"part2 for {filename}: {answer}")
    return answer


def part2(filename="input.txt"):
    lines = read_lines(filename)
    answer = 0
    time = int("".join(lines[0].split(": ")[-1].split()))
    dist = int("".join(lines[1].split(": ")[-1].split()))
    answer += count(time, dist)

    print(f"part2 for {filename}: {answer}")
    return answer


if __name__ == "__main__":
    assert part1("example1.txt") == 288
    assert part1() == 131376

    assert part2("example1.txt") == 71503
    assert part2() == 34123437
