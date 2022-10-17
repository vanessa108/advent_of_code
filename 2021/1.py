with open('tests/1_given.txt') as f:
    data = f.read().splitlines()

data = [int(x) for x in data]

def part_1(data):
    count_increase = 0
    for i in range(0, len(data)-1):
        if data[i+1] > data[i]:
            count_increase += 1
    return count_increase

def part_2(data):
    count_increase = 0
    prev_win = data[0] + data[1] + data[2] 
    for i in range(1, len(data)- 2):
        this_win = data[i] + data[i+1] + data[i+2]
        if this_win > prev_win:
            count_increase += 1
        prev_win = this_win
    return count_increase

print("Part 1:", part_1(data))
print("Part 2:", part_2(data))