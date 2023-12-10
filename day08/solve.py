import itertools
import math
import operator
import re
from functools import reduce
from typing import Iterable

from utils import perf_timer, read_lines


def read_data(filename: str) -> tuple[Iterable[int], dict[str : tuple[str, str]]]:
    lines = read_lines(filename)
    directions = ["LR".index(i) for i in lines[0].strip()]
    network = dict(
        (node, (left, right))
        for node, left, right in [re.findall(r"[\d\w]{3}", line) for line in lines[2:]]
    )
    return directions, network


def count_turns(directions, network, start, end):
    current_node = start
    for step_number, instruction in enumerate(itertools.cycle(directions)):
        if current_node.endswith(end):
            return step_number
        current_node = network[current_node][instruction]


def part1(filename="input.txt"):
    directions, network = read_data(filename=filename)
    answer = count_turns(directions, network, "AAA", "ZZZ")
    print(f"part 1 for {filename}: {answer}")
    return answer


def part2(filename="input.txt"):
    directions, network = read_data(filename=filename)
    start_nodes = list(filter(lambda key: key[-1] == "A", network.keys()))
    cycle_lengths = [
        count_turns(directions, network, start_node, "Z") for start_node in start_nodes
    ]
    answer = math.lcm(*cycle_lengths)
    print(f"part 2 for {filename}: {answer}")
    return answer


if __name__ == "__main__":
    assert part1("example1.txt") == 2
    assert part1("example2.txt") == 6
    assert part1() == 13301
    assert part2("example3.txt") == 6
    assert part2() == 7309459565207
