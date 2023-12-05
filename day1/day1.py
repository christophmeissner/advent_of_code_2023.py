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


if __name__ == "__main__":
    print(f"part 1: {part1()}")
