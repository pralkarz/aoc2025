with open("day04/in04.txt") as in04:
    data = [line.strip() for line in in04.readlines()]

# (y, x)
OFFSETS_TO_CHECK = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)


def is_reachable(x, y, grid):
    neighbors = 0

    for offset in OFFSETS_TO_CHECK:
        y2 = y + offset[0]
        x2 = x + offset[1]

        if x2 >= 0 and x2 < len(grid[0]) and y2 >= 0 and y2 < len(grid):
            if grid[y2][x2] == "@":
                neighbors += 1

        if neighbors >= 4:
            return False

    return True


def part1(grid):
    out = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "@":
                out += is_reachable(x, y, grid)
    return out


def part2(grid):
    out = 0
    while True:
        removed = 0
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == "@" and is_reachable(x, y, grid):
                    grid[y] = grid[y][:x] + "." + grid[y][x + 1 :]
                    removed += 1

                    out += 1

        if removed == 0:
            break

    return out


print("Part one:", part1(data))
print("Part two:", part2(data))
