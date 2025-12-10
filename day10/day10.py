from itertools import combinations, combinations_with_replacement

with open("day10/in10.txt") as in10:
    data = in10.readlines()


def simulate(num_lights, presses):
    state = [False for i in range(num_lights)]

    for press in presses:
        for button in press:
            state[button] = not state[button]

    return state


def part1(data):
    out = 0
    for machine in data:
        split = machine.split()
        target_lights = [True if light == "#" else False for light in split[0][1:-1]]
        button_wirings = [
            tuple(int(n) for n in wiring[1:-1].split(",")) for wiring in split[1:-1]
        ]

        for i in range(1, len(button_wirings) + 1):
            for presses in combinations(button_wirings, i):
                if simulate(len(target_lights), presses) == target_lights:
                    out += i
                    break
            # I love Python.
            else:
                continue
            break

    return out


print("Part one:", part1(data))
