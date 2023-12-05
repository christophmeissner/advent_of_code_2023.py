def read_lines(filename):
    with open(filename) as inputfile:
        return list(l.strip() for l in inputfile)
