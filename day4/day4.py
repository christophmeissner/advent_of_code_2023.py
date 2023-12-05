from utils import read_lines


def part1():
    lines = read_lines("input.txt")
    total = 0
    for card in lines:
        winning, scratched = (l.split() for l in card.split(": ")[-1].split(" | "))
        winning = set(map(int, winning))
        count = len(set(filter(lambda i: i in winning, map(int, scratched))))
        if count:
            total += 2 ** (count - 1)
    return total


def part2():
    pass


if __name__ == "__main__":
    print(f"part 1: {part1()}")
    print(f"part 2: {part2()}")
