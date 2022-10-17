with open('tests/6_given.txt') as f:
    data = f.read().split(',')
    data = list(map(int, data))

def part_1(fish_list, days):
    for i in range(0, days):
        fish_list = update_fish(fish_list)
    num_fish = len(fish_list)
    return num_fish   

def update_fish(fish_list):
    for i in range(len(fish_list)):
        if fish_list[i] == 0:
            fish_list[i] = 6
            fish_list.append(8)
        else:
            fish_list[i] -= 1
    return fish_list

def part_2(fish_list, days):
    fish_days = [fish_list.count(x) for x in range(9)]
    for day in range(days):
        num_birth = fish_days[0]
        fish_days.append(num_birth)
        fish_days = fish_days[1:]
        fish_days[6] += num_birth
    return sum(fish_days)
    
    
print("Part 1:", part_1(data,80))
print("Part 2:", part_2(data, 256))