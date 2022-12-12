import re
class Monkey():
    def __init__(self, number, items, operation, divisible_by, true_monkey, false_monkey):
        self.number = number
        self.items = items
        self.operation = operation
        self.divisible_by = divisible_by
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
    
    def add_items(self,item):
        self.items.append(item)

def process_monkey_data(monkey_data):
    monkey_number = int(re.search(r'\d+', monkey_data[0])[0])
    items = monkey_data[1][18:].split(',')
    items = [int(x) for x in items]
    operation = monkey_data[2][19:]
    divisible_by = int(monkey_data[3][22:])
    true_monkey = int(re.search(r'\d+', monkey_data[4])[0])
    false_monkey = int(re.search(r'\d+', monkey_data[5])[0])
    this_monkey = Monkey(monkey_number, items, operation, divisible_by, true_monkey, false_monkey)
    return this_monkey

    pass
def part_one(input_file):
    with open(input_file) as f:
        data = f.read().splitlines()
    monkeys = []
    for i in range(0, len(data), 7):
        monkey = process_monkey_data(data[i:i+6])
        monkeys.append(monkey)

    for _ in range(1):
        for monkey in monkeys:
            for item in monkey.items:
                old = item
                print(monkey.operation)
                new = eval(monkey.operation)
                print(new)
                worry = new//3
                print(worry)
                print(worry % monkey.divisible_by)
                if worry % monkey.divisible_by == 0:
                    monkeys[monkey.true_monkey].items.append(item)
                else:
                    monkeys[monkey.false_monkey].items.append(item)
            monkey.items = []
    for monkey in monkeys:
        print(monkey.items)
    
        


part_one('example.txt')
