def part1():
    bag = {"red": 12, "green": 13, "blue": 14}
    with open("input.txt") as inputfile:
        total = 0
        for line in (l.strip() for l in inputfile):
            game, draws = line.split(": ")
            draws = draws.split("; ")
            gamenum = int(game.split(" ")[-1])
            print(f"{gamenum} | {draws}")
            add = gamenum
            for drawing in draws:
                for count, color in (d.split(" ") for d in drawing.split(", ")):
                    if int(count) > bag[color]:
                        add = 0
                        break
                if add == 0:
                    break
            else:
                total += gamenum
        return total


def part2():
    with open("input.txt") as inputfile:
        total = 0
        for line in (l.strip() for l in inputfile):
            game, draws = line.split(": ")
            draws = draws.split("; ")
            gamenum = int(game.split(" ")[-1])
            max_colors = dict(red=0, green=0, blue=0)
            for drawing in draws:
                for count, color in (d.split(" ") for d in drawing.split(", ")):
                    max_colors[color] = max(max_colors[color], int(count))
            power = max_colors["red"] * max_colors["green"] * max_colors["blue"]
            print(f"{gamenum} | {draws} | {max_colors} | {power}")
            total += power
        return total


if __name__ == "__main__":
    print(f"part 1: {part1()}")
    print(f"part 2: {part2()}")
