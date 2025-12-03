with open("day03/in03.txt") as in03:
    data = [line.strip() for line in in03.readlines()]


def get_largest_joltage(battery, n):
    largest_joltage = ""
    window_size = len(battery) - n
    while len(largest_joltage) < n:
        next_digit = int(battery[0])
        next_digit_idx = 0
        for idx, digit in enumerate(battery[1 : 1 + window_size], start=1):
            if (new_digit := int(digit)) > next_digit:
                next_digit = new_digit
                next_digit_idx = idx

        largest_joltage += battery[next_digit_idx]
        window_size -= next_digit_idx
        
        battery = battery[next_digit_idx + 1 :]

    return int(largest_joltage)


def part1(data):
    out = 0

    for battery in data:
        out += get_largest_joltage(battery, 2)

    return out


def part2(data):
    out = 0

    for battery in data:
        out += get_largest_joltage(battery, 12)

    return out


print("Part one:", part1(data))
print("Part two:", part2(data))
