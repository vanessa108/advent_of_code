with open('tests/2_given.txt') as f:
    data = f.read().splitlines()

def part_1(data):
    forward = 0
    depth = 0
    for line in data:
        if 'forward' in line:
            forward += int(line[-1])
        elif 'down' in line:
            depth += int(line[-1])
        else:
            depth -= int(line[-1])
    return forward * depth

def part_2(data):
    hor_pos = 0
    depth = 0
    aim = 0
    for line in data:
        if 'forward' in line:
            units = int(line[-1])
            hor_pos += units
            depth += units * aim
        elif 'down' in line:
            aim += int(line[-1])
        else:
            aim -= int(line[-1])
    return hor_pos * depth

print("Part 1:", part_1(data))
print("Part 2:", part_2(data))