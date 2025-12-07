with open("day07/in07.txt") as in07:
    data = [line.strip() for line in in07.readlines()]


def part1(grid):
    beams = set()
    for idx, c in enumerate(grid[0]):
        if c == "S":
            beams.add(idx)
            break

    y = 1
    out = 0
    while y < len(grid):
        new_beams = beams.copy()
        for beam in beams:
            if grid[y][beam] == "^":
                out += 1
                new_beams.remove(beam)
                new_beams.add(beam - 1)
                new_beams.add(beam + 1)
        beams = new_beams.copy()

        y += 1

    return out


def count_timelines(beam, y, grid, cache):
    while y < len(grid):
        if grid[y][beam] == "^":
            if (beam, y) in cache:
                return cache[(beam, y)]

            cache[(beam, y)] = count_timelines(
                beam - 1, y, grid, cache
            ) + count_timelines(beam + 1, y, grid, cache)

            return cache[(beam, y)]

        y += 1

    return 1


def part2(grid):
    beam = None
    for idx, c in enumerate(grid[0]):
        if c == "S":
            beam = idx
            break

    return count_timelines(beam, 1, grid, {})


print("Part one:", part1(data))
print("Part two:", part2(data))
