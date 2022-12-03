import string

with open('input.txt') as f:
    rucksacks = f.read().splitlines()

alphabet = list(string.ascii_lowercase + string.ascii_uppercase)

def part_one():
    priority_sum = 0 
    for rucksack in rucksacks:
        half_one = rucksack[:len(rucksack)//2]
        half_two = rucksack[len(rucksack)//2:]
        half_one = set(half_one)
        half_two = set(half_two)
        common = half_one & half_two
        common = list(common)[0]
        priority_sum += alphabet.index(common) + 1

    print(priority_sum)

def part_two():
    priority_sum = 0
    for i in range(0,len(rucksacks), 3):
        elf_group = rucksacks[i:i+3]
        elf_group = [set(sack) for sack in elf_group]
        common = elf_group[0] & elf_group[1] & elf_group[2]
        common = list(common)[0]
        priority_sum += alphabet.index(common) + 1
    print(priority_sum)
part_two()