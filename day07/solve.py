from collections import Counter
from utils import read_lines


def hand_order(hand, jokers=False):
    card_order = jokers and "J23456789TQKA" or "23456789TJQKA"
    counter = Counter(hand)
    if jokers and "J" in counter:
        joker_count = counter.pop("J")
        if counter:
            items = sorted(
                counter.items(),
                key=lambda card: (card[1], card_order.index(card[0])),
                reverse=True,
            )
            most_common_card = items[0][0]
        else:
            # when hand == "JJJJJ", counter will have no more cards after popping
            most_common_card = card_order[-1]
        counter[most_common_card] += joker_count
    return sorted(counter.values(), reverse=True) + [card_order.index(c) for c in hand]


def solve(filename, jokers):
    hand_tuple = lambda l: (hand_order(l[0], jokers), l[0], int(l[1]))
    hand_bids = (line.split() for line in read_lines(filename))
    hands = sorted(map(hand_tuple, hand_bids))

    answer = 0
    for i, (order, hand, bid) in enumerate(hands, start=1):
        answer += bid * i

    return answer


def part1(filename="input.txt"):
    answer = solve(filename, jokers=False)
    print(f"part 1 for {filename}: {answer}")
    return answer


def part2(filename="input.txt"):
    answer = solve(filename, jokers=True)
    print(f"part 2 for {filename}: {answer}")
    return answer


if __name__ == "__main__":
    assert part1("example1.txt") == 6440
    assert part1() == 253638586

    assert part2("example1.txt") == 5905
    assert part2() == 253253225
