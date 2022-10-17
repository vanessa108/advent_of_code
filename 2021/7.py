with open('tests/7_given.txt') as f:
    data = f.read().split(',')
    data = list(map(int, data))

def part_1(data):
    data.sort()
    median_pos = round(len(data)/2)
    fuel_cost = sum(abs(data[median_pos]- x) for x in data)
    return fuel_cost

def part_2(data):
    # using triangle number formula to calculate costs
    cheapest_fuel_cost = 1000000000
    cheapest_pos = 0
    tri_num = lambda n : (n*(n+1))/2
    for pos in range(max(data)):
        fuel_cost = 0
        for crab in data:
            distance = abs(pos-crab)
            fuel_cost += tri_num(distance)
        if fuel_cost < cheapest_fuel_cost:
            cheapest_fuel_cost = fuel_cost
            cheapest_pos = pos
    print(cheapest_pos)
    return cheapest_fuel_cost

print("Part 1:", part_1(data))
print("Part 2:", part_2(data))