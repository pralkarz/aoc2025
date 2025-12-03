with open("day02/in02.txt") as in02:
    data = in02.read()


def part1(data):
    out = 0

    id_ranges = data.split(",")
    for id_range in id_ranges:
        start, end = id_range.split("-")

        for i in range(int(start), int(end) + 1):
            i = str(i)
            l = len(i)

            if l % 2 != 0:
                continue

            if i[: l // 2] == i[l // 2 :]:
                out += int(i)

    return out


def part2(data):
    out = 0

    id_ranges = data.split(",")
    for id_range in id_ranges:
        start, end = id_range.split("-")

        for i in range(int(start), int(end) + 1):
            i = str(i)
            l = len(i)

            for j in range(l // 2, 0, -1):
                for k in range(j, l, j):
                    if i[k : k + j] != i[k - j : k]:
                        break
                else:
                    out += int(i)
                    break

    return out


print("Part one:", part1(data))
print("Part two:", part2(data))
