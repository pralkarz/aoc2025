with open("day05/in05.txt") as in05:
    data = in05.read()


def part1(data):
    out = 0

    ranges, available = data.split("\n\n")

    parsed_ranges = set()
    for r in ranges.split():
        start, end = r.split("-")
        parsed_ranges.add((int(start), int(end)))

    for id in available.split():
        for r in parsed_ranges:
            if int(id) >= r[0] and int(id) <= r[1]:
                out += 1
                break

    return out


def part2(data):
    ranges, _ = data.split("\n\n")

    parsed_ranges = []
    for r in ranges.split():
        parsed_ranges.append([int(n) for n in r.split("-")])

    parsed_ranges.sort(key=lambda r: r[0])
    combined = [parsed_ranges[0]]
    for r in parsed_ranges:
        last = combined[-1]
        if r[0] <= last[1]:
            last[1] = max(last[1], r[1])
        else:
            combined.append(r)

    out = 0
    for r in combined:
        out += r[1] - r[0] + 1

    return out


print("Part one:", part1(data))
print("Part two:", part2(data))
