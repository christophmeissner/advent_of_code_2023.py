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


if __name__ == "__main__":
    print(f"part 1: {part1()}")
