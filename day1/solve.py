import utils


def part1(filename="input.txt"):
    """
    On each line, the calibration value can be found by combining the first digit and
    the last digit (in that order) to form a single two-digit number.

    For example:

    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet

    In this example, the calibration values of these four lines are 12, 38, 15, and 77.
    Adding these together produces 142.
    """
    answer = 0
    for line in utils.read_lines(filename):
        digits = list(filter(lambda c: c.isdigit(), line))
        answer += int(digits[0]) * 10 + int(digits[-1])
    print(f"part 1 for {filename}: {answer}")
    return answer


def part2(filename="input.txt"):
    """
    Your calculation isn't quite right. It looks like some of the digits are actually
    spelled out with letters: one, two, three, four, five, six, seven, eight, and nine
    also count as valid "digits".

    Equipped with this new information, you now need to find the real first and last
    digit on each line. For example:

    two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen

    In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding
    these together produces 281.
    """
    digit_words = (
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    )
    answer = 0
    for line in utils.read_lines(filename):
        found_numbers = []
        for character_index, char in enumerate(line):
            if char.isdigit():
                found_numbers.append(int(char))
            else:
                for digit_word_index, digit_word in enumerate(digit_words[1:], start=1):
                    if line[character_index:].startswith(digit_word):
                        found_numbers.append(digit_word_index)
        answer += found_numbers[0] * 10 + found_numbers[-1]
    print(f"part 2 for {filename}: {answer}")
    return answer


if __name__ == "__main__":
    assert part1("example1.txt") == 142
    assert part1() == 54940

    assert part2("example2.txt") == 281
    assert part2() == 54208
