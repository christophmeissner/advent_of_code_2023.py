import functools
from collections import defaultdict

import utils


def part1(filename="input.txt"):
    bag = {"red": 12, "green": 13, "blue": 14}
    answer = 0
    for line in utils.read_lines(filename):
        game, rounds = line.split(": ")
        game = int(game.split()[-1])
        rounds = rounds.split("; ")
        for round in rounds:
            for ball_count, color in [c.split() for c in round.split(", ")]:
                if int(ball_count) > bag[color]:
                    break
            else:
                continue
            break
        else:
            answer += game
    print(f"part 1 for {filename}: {answer}")
    return answer


def part2(filename="input.txt"):
    answer = 0
    for line in utils.read_lines(filename):
        max_colors = defaultdict(int)
        for round in line.split(": ")[-1].split("; "):
            for ball_count, color in [c.split() for c in round.split(", ")]:
                max_colors[color] = max(max_colors[color], int(ball_count))
        answer += functools.reduce(lambda a, b: a * b, max_colors.values())
    print(f"part 2 for {filename}: {answer}")
    return answer


if __name__ == "__main__":
    assert part1("example1.txt") == 8
    assert part1() == 2348

    assert part2("example2.txt") == 2286
    assert part2() == 76008
