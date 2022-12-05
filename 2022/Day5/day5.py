with open('input.txt') as f:
    data = f.read().splitlines()
stack_row = 7
# 2

def get_stacks():
    original_stacks = list(data[stack_row+1])
    stack_labels = [x for x in original_stacks if x != ' ']

    stack_indexes = {}
    stacks = {}

    for label in stack_labels:
        stack_index = original_stacks.index(label)
        stack_indexes[stack_index] = label
        stacks[label] = []


    for i in range(stack_row+1):
        row = data[i]
        for key, value in stack_indexes.items():
            stack_item = row[key]
            if stack_item != ' ':
                stacks[value].append(stack_item)
    for key, value in stacks.items():
        stacks[key] = value[::-1]
    return stacks

def process_instruction(instruction):
    instruction = instruction.replace('move', '')
    instruction = instruction.replace('from', ',')
    instruction = instruction.replace('to', ',')
    instruction = instruction.split(',')
    instruction = [x.strip() for x in instruction]
    return instruction
def part_one():
    stacks = get_stacks()
    for i in range(stack_row + 3, len(data)):
        instruction = data[i]
        num, start_stack, target_stack = process_instruction(instruction)

        for _ in range(int(num)):
            item = stacks[start_stack].pop()
            stacks[target_stack].append(item)
    top = ''
    for stack in stacks.values():
        top += stack[-1]
    print(top)

def part_two():
    stacks = get_stacks()
    for i in range(stack_row + 3, len(data)):
        instruction = data[i]
        num, start_stack, target_stack = process_instruction(instruction)
        moved_items = []
        for _ in range(int(num)):
            item = stacks[start_stack].pop()
            moved_items.append(str(item))
        moved_items = moved_items[::-1]
        stacks[target_stack] = stacks[target_stack] + moved_items

    top = ''
    for stack in stacks.values():
        top += stack[-1]
    print(top)

part_two()

