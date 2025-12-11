with open("day11/in11.txt") as in11:
    data = in11.readlines()


def count(start, graph):
    if start == "out":
        return 1

    result = 0
    for output in graph[start]:
        result += count(output, graph)

    return result


def part1(data):
    graph = {}
    for line in data:
        device, outputs = line.split(": ")
        graph[device] = outputs.split()

    return count("you", graph)


print("Part one:", part1(data))
