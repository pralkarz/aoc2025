with open("day06/in06.txt") as in06:
    data = in06.read()


def part1(data):
    data = data.split("\n")

    numbers = data[1:-2]
    operators = data[-2].split()

    results = [int(n) for n in data[0].split()]
    for line in numbers:
        line = [int(n) for n in line.split()]
        for idx, n in enumerate(line):
            match operators[idx]:
                case "+":
                    results[idx] += n
                case "*":
                    results[idx] *= n

    return sum(results)


def part2(data):
    data = data.split("\n")

    numbers = data[:-2]
    operators = data[-2].split()

    column = 0
    results = []
    for idx, c in enumerate(numbers[0]):
        ceph = c + "".join(col[idx] for col in numbers[1:])

        if len(ceph.strip()) == 0:
            column += 1
            continue

        if len(results) <= column:
            results.append(int(ceph))
        else:
            match operators[column]:
                case "+":
                    results[column] += int(ceph)
                case "*":
                    results[column] *= int(ceph)

    return sum(results)


print("Part one:", part1(data))
print("Part two:", part2(data))
