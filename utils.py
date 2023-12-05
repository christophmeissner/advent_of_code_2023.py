def read_lines(filename):
    with open("input.txt") as inputfile:
        return list(l.strip() for l in inputfile)
