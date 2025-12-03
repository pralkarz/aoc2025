with open("day01/in01.txt") as in01:
    data = in01.readlines()


def part1(data):
    out = 0
    dial = 50

    for rotation in data:
        direction = rotation[0]
        n = int(rotation[1:])

        if direction == "L":
            dial -= n
        else:
            dial += n

        if dial % 100 == 0:
            out += 1

    return out


def part2(data):
    out = 0
    dial = 50

    for rotation in data:
        direction = rotation[0]
        n = int(rotation[1:])

        if direction == "L":
            dial -= n
            if dial <= 0:
                out += abs(dial) // 100
                if n + dial != 0:
                    out += 1

        else:
            dial += n
            if dial >= 100:
                out += dial // 100

        dial = dial % 100

    return out


print("Part one:", part1(data))
print("Part two:", part2(data))
