from utils import batched, offset_range, read_lines


def make_mapping(dest, source, length):
    def mapping(value):
        if source <= value < source + length:
            return value - (source - dest)

    return mapping


def part1(filename="input.txt"):
    lines = read_lines(filename)
    seeds = list(map(int, lines[0].split()[1:]))
    stages = []
    current_stage = []
    for line in lines[2:] + [""]:
        if line and line[0].isdigit():
            dest, source, length = map(int, line.split())
            current_stage.append(make_mapping(dest, source, length))
        elif current_stage:
            stages.append(current_stage)
            current_stage = []

    locations = []
    for seed in seeds:
        # print(f"seed = {seed}")
        output = seed
        for s_idx, stage in enumerate(stages):
            stage_input = output
            # print(f"seed {seed}: stage {s_idx}({stage_input})")
            for m_idx, mapping in enumerate(stage):
                mapped = mapping(stage_input)
                if mapped:
                    # print(f"seed {seed}: stage {s_idx}({stage_input}) -> {mapped}")
                    output = mapped
                    break
        locations.append(output)
        # print(f"seed = {seed} -> {output}")

    answer = min(locations)
    print(f"part 1 for {filename}: {answer}")
    return answer


class Stage:
    def __init__(self, name):
        self.name = name
        self.mappings = dict()

    def add_mapping(self, dest, source, length):
        r = range(source, source + length)
        self.mappings[r] = -(source - dest)

    def remap_ranges(self, seed_ranges):
        seed_ranges = seed_ranges.copy()
        output = dict()
        while len(seed_ranges):
            i_r, i_o = seed_ranges.popitem()
            for m_r, m_o in self.mappings.items():
                mapped_range = unmapped_range = None
                if i_r.start in m_r and i_r[-1] in m_r:
                    mapped_range = range(i_r.start, i_r.stop)
                elif i_r.start in m_r:
                    mapped_range = range(i_r.start, m_r.stop)
                    unmapped_range = range(m_r.stop, i_r.stop)
                elif i_r[-1] in m_r:
                    mapped_range = range(m_r.start, i_r.stop)
                    unmapped_range = range(i_r.start, m_r.start)
                if mapped_range:
                    output[offset_range(mapped_range, m_o)] = i_o + m_o
                    if unmapped_range:
                        seed_ranges[unmapped_range] = i_o
                    break
            else:
                output[i_r] = i_o
        return output


def part2(filename="input.txt"):
    lines = read_lines(filename)

    seed_ranges = dict(
        (range(start_seed, start_seed + length), 0)
        for start_seed, length in batched(map(int, lines[0].split()[1:]), 2)
    )

    stages = []
    current_stage = None
    for line in lines[2:] + [""]:
        if line:
            if line[0].isdigit():
                dest, source, length = map(int, line.split())
                current_stage.add_mapping(dest, source, length)
            else:
                current_stage = Stage(name=line.split()[0])
        else:
            stages.append(current_stage)
            current_stage = None

    for stage in stages:
        seed_ranges = stage.remap_ranges(seed_ranges)

    result = min(map(lambda i: i[0].start, seed_ranges.items()))
    print(f"part 2 for {filename}: {result}")
    return result


if __name__ == "__main__":
    assert part1("example1.txt") == 35
    assert part1() == 535088217

    assert part2("example2.txt") == 35
    assert part2("example1.txt") == 46
    assert part2() == 51399228
