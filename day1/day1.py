import string


def part1():
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
    with open("input.txt") as inputfile:
        number = 0
        for line in inputfile:
            digits = list(filter(lambda c: c.isdigit(), line))
            linenum = int(digits[0]) * 10 + int(digits[-1])
            number += linenum
        return number


def part2():
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
    words = (
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
    digit_words = dict(zip(words + tuple(string.digits[1:]), string.digits[1:] * 2))

    with open("input.txt") as inputfile:
        number = 0
        for line in (line.rstrip() for line in inputfile):
            left, right = dict(), dict()
            for d in digit_words.keys():
                ridx = line.rfind(d)
                if not ridx == -1:
                    right[d] = ridx
                lidx = line.find(d)
                if not lidx == -1:
                    left[d] = lidx
            minleft = min(left, key=left.get)
            maxright = max(right, key=right.get)
            linenum = int(digit_words[minleft]) * 10 + int(digit_words[maxright])
            number += linenum
        return number


if __name__ == "__main__":
    print(f"part 1: {part1()}")
    print(f"part 2: {part2()}")
