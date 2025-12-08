from collections import defaultdict

with open("day09/in09.txt") as in09:
    data = in09.readlines()


def part1(data):
    largest_area = 0
    for idx, red_tile1 in enumerate(data):
        x1, y1 = [int(n) for n in red_tile1.split(",")]
        for red_tile2 in data[idx + 1 :]:
            x2, y2 = [int(n) for n in red_tile2.split(",")]

            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            if area > largest_area:
                largest_area = area

    return largest_area


# Checks whether `point` is inside the `borders` with some fuckery due to the fact that points
# on the border also count, and I couldn't be bother to draw an outline around them to make solving
# this easier for myself.
def is_inside(point, borders, upper_limit):
    ox, oy = point
    p = ox
    walls_hit = 0
    while p < upper_limit + 1:
        if (p, oy) not in borders:
            p += 1
        elif (p, oy) in borders and (p + 1, oy) not in borders:
            walls_hit += 1
            p += 1
        else:
            next_p = p + 1
            while (next_p, oy) in borders:
                next_p += 1
            p = next_p

            # Due to the approach in part 2, we're always expecting to hit at least one wall.
            # This (at least I hope my reasoning is correct) guards against cases such as the below,
            # where `O` are walls, and `X` is the point we're checking:
            # ....O.......O.
            # ....O...XOOOO.
            # ....OOOOOO.
            if p == upper_limit + 1 and walls_hit == 0:
                walls_hit = 1

    return walls_hit % 2 == 1


# Terribly slow (>5 minutes on a very good CPU), but miraculously works. Algorithm roughly
# explained in the code comments.
def part2(data):
    # First, we simply draw the outline, putting every point on the way in the set.
    # This is already slow and takes up a lot of memory. Vertices are used later to (possibly?)
    # speed up the final computation.
    borders = set()
    vertices = []
    for idx, vertex in enumerate(data):
        x1, y1 = [int(n) for n in vertex.split(",")]
        x2, y2 = [int(n) for n in data[(idx + 1) % len(data)].split(",")]

        # These checks were needed when I wanted vertices to be ordered. The current solution
        # doesn't need them to be, so it could be a set, but I'm scared to make too many changes
        # lest it stops working lmao.
        if (x1, y1) not in vertices:
            vertices.append((x1, y1))
        if (x2, y2) not in vertices:
            vertices.append((x2, y2))

        if x1 == x2:
            operator = 1 if y1 < y2 else -1
            for i in range(y1, y2 + operator, operator):
                borders.add((x1, i))
        else:
            operator = 1 if x1 < x2 else -1
            for i in range(x1, x2 + operator, operator):
                borders.add((i, y1))

    # We create a dict with items like `y: List[x]`. One could imagine it like drawing a horizontal
    # line at each y and mapping it to what points lie on the border.
    borders_per_y = defaultdict(list)
    for border in borders:
        borders_per_y[border[1]].append(border[0])

    # For each y, we draw a horizontal line once again, but now we also want to include points that
    # are inside the shape and not necessarily on the border.
    valid_ranges = defaultdict(list)
    for y, xs in borders_per_y.items():
        xs = sorted(xs)

        range_start = xs[0]
        for idx, x in enumerate(xs[:-1]):
            if xs[idx + 1] - x != 1:
                # This handles that. Let's say we're following a border horizontally. When we leave
                # it, and `is_inside` returns `False`, that means we've stepped outside, so we can
                # propagate the range calculated so far. Otherwise, if we're still inside, we
                # continue without any extra modifications.
                if not is_inside((x + 1, y), borders, xs[-1]):
                    valid_ranges[y].append((range_start, x))
                    range_start = xs[idx + 1]

        # After reaching the end, append the last range.
        valid_ranges[y].append((range_start, xs[-1]))

    # We calculate every area (similar to part 1), but also store the vertices used to compute it.
    areas = []
    for idx, vertex1 in enumerate(vertices):
        for vertex2 in vertices[idx + 1 :]:
            x1, y1 = vertex1
            x2, y2 = vertex2
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            areas.append((x1, y1, x2, y2, area))
    # Then we sort the list in a descending order based on the area...
    sorted_areas = sorted(areas, key=lambda item: item[4], reverse=True)

    # ...so that later we can check the areas starting from the largest. This way, the first one
    # we find that satisfies the problem statement, is automatically the largest, so we return it
    # as the answer. The algorithm for checking that goes from top to bottom of the given
    # rectangle, and for each `y` draws a horizontal line from left to right. If all such lines
    # are fully contained within one of the computed ranges for that `y`, the problem statement
    # is satisfied.
    for x1, y1, x2, y2, area in sorted_areas:
        min_y = min(y1, y2)
        max_y = max(y1, y2)
        min_x = min(x1, x2)
        max_x = max(x1, x2)

        for y in range(min_y, max_y + 1):
            valid = False
            for r in valid_ranges[y]:
                if min_x >= r[0] and max_x <= r[1]:
                    valid = True
                    break

            if not valid:
                break
        else:
            return area


print("Part one:", part1(data))
print("Part two:", part2(data))
