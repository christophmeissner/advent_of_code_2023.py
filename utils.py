import itertools
from time import perf_counter


def read_lines(filename):
    with open(filename) as inputfile:
        return list(line.strip() for line in inputfile)


def batched(iterable, n):
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError("n must be at least one")
    it = iter(iterable)
    while batch := tuple(itertools.islice(it, n)):
        yield batch


def offset_range(range_in, offset):
    return range(range_in.start + offset, range_in.stop + offset)


class perf_timer:
    def __init__(self, name=None, verbose=False):
        self.name = name
        self.verbose = verbose

    def __enter__(self):
        self.start = perf_counter()
        self.end = None
        return self

    def __exit__(self, type, value, traceback):
        self.end = perf_counter()
        if self.verbose:
            print(f"Time: {self.elapsed:.10f} seconds")

    @property
    def elapsed(self):
        p = perf_counter()
        return (self.end or p) - self.start
