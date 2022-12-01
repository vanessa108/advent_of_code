with open('Day1/input.txt') as f:
    data = f.read().splitlines()

elf_food = []
i = 0
elf_array = []
while i < len(data):
    if data[i] == '':
        elf_array = [int(x) for x in elf_array]

        elf_food.append(sum(elf_array))
        elf_array = []
    else:
        elf_array.append(data[i])
    i += 1

elf_array = [int(x) for x in elf_array]
elf_food.append(sum(elf_array))

elf_food.sort()
print(elf_food)
print(sum(elf_food[-3:]))


