import re
import math
class Monkey():
    def __init__(self, number, items, operation, divisible_by, true_monkey, false_monkey):
        self.number = number
        self.items = items
        self.operation = operation
        self.divisible_by = divisible_by
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspection_count = 0
    

def process_monkey_data(monkey_data):
    monkey_number = int(re.search(r'\d+', monkey_data[0])[0])
    items = monkey_data[1][18:].split(',')
    items = [int(x) for x in items]
    operation = monkey_data[2][19:]
    divisible_by = int(re.search(r'\d+', monkey_data[3])[0])
    true_monkey = int(re.search(r'\d+', monkey_data[4])[0])
    false_monkey = int(re.search(r'\d+', monkey_data[5])[0])
    this_monkey = Monkey(monkey_number, items, operation, divisible_by, true_monkey, false_monkey)
    return this_monkey

    pass
def part_one(input_file):
    num_rounds =  20
    with open(input_file) as f:
        data = f.read().splitlines()
    monkeys = []
    for i in range(0, len(data), 7):
        monkey = process_monkey_data(data[i:i+6])
        monkeys.append(monkey)
    for _ in range(num_rounds):
        for monkey in monkeys:
            for item in monkey.items:
                monkey.inspection_count += 1
                old = item
                new = eval(monkey.operation)
                worry = new//3
                if worry % monkey.divisible_by == 0:
                    monkeys[monkey.true_monkey].items.append(worry)
                else:
                    monkeys[monkey.false_monkey].items.append(worry)
            monkey.items = []

    #         # print(monkeys[0].items)
    #         # print(monkeys[3].items)
    monkey_inspections = []
    for monkey in monkeys:
        monkey_inspections.append(monkey.inspection_count)
    monkey_inspections.sort(reverse=True)
    print(f'Monkey Business:{monkey_inspections[0] * monkey_inspections[1]}')
        
    
def part_two(input_file):
    num_rounds =  10000
    with open(input_file) as f:
        data = f.read().splitlines()
    monkeys = []
    monkey_modulo = 1
    for i in range(0, len(data), 7):
        monkey = process_monkey_data(data[i:i+6])
        monkeys.append(monkey)
        monkey_modulo *= monkey.divisible_by
    for _ in range(num_rounds):
        for monkey in monkeys:
            for item in monkey.items:
                monkey.inspection_count += 1
                old = item
                new = eval(monkey.operation)
                worry = new % monkey_modulo
                if worry % monkey.divisible_by == 0:
                    monkeys[monkey.true_monkey].items.append(worry)
                else:
                    monkeys[monkey.false_monkey].items.append(worry)
            monkey.items = []
    monkey_inspections = []
    for monkey in monkeys:
        monkey_inspections.append(monkey.inspection_count)
    monkey_inspections.sort(reverse=True)
    print(f'Monkey Business:{monkey_inspections[0] * monkey_inspections[1]}')        


part_one('input.txt')
part_two('input.txt')