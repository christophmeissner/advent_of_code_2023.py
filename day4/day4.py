from utils import read_lines


def part1():
    lines = read_lines("input.txt")
    total = 0
    for card in lines:
        count = wins(card)
        if count:
            total += 2 ** (count - 1)
    return total


def wins(card):
    winning, scratched = (l.split() for l in card.split(": ")[-1].split(" | "))
    winning = set(map(int, winning))
    return len(set(filter(lambda i: i in winning, map(int, scratched))))


def part2():
    lines = read_lines("input.txt")

    pile = dict(zip(range(len(lines)), (1,) * len(lines)))
    for i, card in enumerate(lines):
        count = wins(card)
        for n in range(count):
            pile[i + n + 1] += pile[i]

    return sum(pile.values())


if __name__ == "__main__":
    print(f"part 1: {part1()}")
    print(f"part 2: {part2()}")
