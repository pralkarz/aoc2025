import math

with open("day08/in08.txt") as in08:
    data = in08.readlines()


def get_distance(box1, box2):
    return math.sqrt(
        (box2[0] - box1[0]) ** 2 + (box2[1] - box1[1]) ** 2 + (box2[2] - box1[2]) ** 2
    )


def get_distances(boxes):
    distances = {}
    for idx, box1 in enumerate(boxes):
        for jdx, box2 in enumerate(boxes[idx + 1 :], start=idx + 1):
            distances[(idx, jdx)] = get_distance(box1, box2)

    return dict(sorted(distances.items(), key=lambda item: item[1]))


def connect(indices, circuits):
    found = []
    for idx, circuit in enumerate(circuits):
        if indices[0] in circuit or indices[1] in circuit:
            circuit.add(indices[0])
            circuit.add(indices[1])
            found.append(idx)

    if not found:
        circuits.append(set(indices))

    # Merge the circuits that can be merged.
    if len(found) > 0:
        for f in found[::-1][:-1]:
            circuits[found[0]] |= circuits[f]
            del circuits[f]

    return circuits


def part1(data):
    boxes = []
    for box in data:
        boxes.append(tuple(int(n) for n in box.strip().split(",")))

    sorted_distances = get_distances(boxes)
    sorted_distances_keys = list(sorted_distances)

    circuits = []
    for i in range(1000):
        circuits = connect(sorted_distances_keys[i], circuits)

    result = sorted(circuits, key=len)[::-1]
    return len(result[0]) * len(result[1]) * len(result[2])


def part2(data):
    boxes = []
    for box in data:
        boxes.append(tuple(int(n) for n in box.strip().split(",")))

    sorted_distances = get_distances(boxes)
    sorted_distances_keys = list(sorted_distances)

    circuits = []
    i = 0
    while not len(circuits) or len(circuits[0]) < len(boxes):
        to_connect = sorted_distances_keys[i]
        circuits = connect(to_connect, circuits)
        i += 1

    idx, jdx = to_connect
    return boxes[idx][0] * boxes[jdx][0]


print("Part one:", part1(data))
print("Part two:", part2(data))

