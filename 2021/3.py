with open('tests/3_given.txt') as f:
    data = f.read().splitlines()

def part_1(data):
    # create empty list with length of bits
    sum_bit = [0] * len(data[0])
    num_lines = len(data)
    for line in data:
        split_bits = list(line)
        sum_bit = [b1 + b2 for b1, b2 in zip(sum_bit, map(int,split_bits))]
    # determine most common bit
    mcb = [1 if x > num_lines/2 else 0 for x in sum_bit]
    lcb = [1 if x ==0 else 0 for x in mcb]
    mcb_str = ''.join(map(str, mcb))
    lcb_str = ''.join(map(str, lcb))
    gamma = int(mcb_str, base=2)
    epsilon = int(lcb_str, base=2)

    return gamma * epsilon

def part_2(data):
    oxygen = int(find_oxygen(data), base=2)
    co2 = int(find_co2(data), base=2)
    return oxygen*co2

def mcb(values, pos):
    count_1s = 0
    for line in values:
        count_1s += int(line[pos])
    if count_1s >= len(values)/2:
        return 1
    else:
        return 0
def remove_values(mcb, pos, values):
    filtered_values = []
    for line in values:
        if int(line[pos]) == mcb:
            filtered_values.append(line)
    return filtered_values
def find_oxygen(data):
    for i in range(0, len(data[0])):
        this_mcb = mcb(data, i)
        data = remove_values(this_mcb, i, data)
        if len(data) == 1:
            return data[0]

def lcb(values, pos):
    count_1s = 0
    for line in values:
        count_1s += int(line[pos])
    if count_1s < len(values)/2:
        return 1
    else:
        return 0

def find_co2(data):
    for i in range(0, len(data[0])):
        this_lcb = lcb(data, i)
        data = remove_values(this_lcb, i, data)
        if len(data) == 1:
            return data[0]

print("Part 1:", part_1(data))
print("Part 2:", part_2(data))