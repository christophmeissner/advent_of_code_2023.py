from collections import defaultdict

from utils import read_lines


def winning_numbers(card):
    winning, scratched = map(
        lambda l: set(map(int, l)),
        (l.split() for l in card.split(": ")[-1].split(" | ")),
    )

    return winning & scratched


def part1(filename="input.txt"):
    lines = read_lines(filename)
    answer = 0
    for card in lines:
        count = len(winning_numbers(card))
        if count:
            answer += 2 ** (count - 1)
    print(f"part1 for {filename}: {answer}")
    return answer


def part2(filename="input.txt"):
    lines = read_lines(filename)

    pile = defaultdict(int)
    for i, card in enumerate(lines):
        pile[i] += 1
        for n in range(len(winning_numbers(card))):
            pile[i + n + 1] += pile[i]
    answer = sum(pile.values())
    print(f"part2 for {filename}: {answer}")
    return answer


if __name__ == "__main__":
    assert part1("example1.txt") == 13
    assert part1() == 32609

    assert part2("example2.txt") == 30
    assert part2() == 14624680
