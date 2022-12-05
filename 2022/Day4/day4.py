with open('input.txt') as f:
    section_assignments = f.read().splitlines()

def part_one():
    overlap_count = 0
    for assignment in section_assignments:
        elf_assignments = assignment.split(',')
        elf_1, elf_2 = [elf.split('-') for elf in elf_assignments]
        elf_1 = [int(x) for x in elf_1]
        elf_2 = [int(x) for x in elf_2]
        current_range = range(elf_1[0], elf_1[1]+1)
        if elf_2[0] in current_range and elf_2[1] in current_range:
            overlap_count += 1
        else:
            current_range = range(elf_2[0], elf_2[1]+1)
            if elf_1[0] in current_range and elf_1[1] in current_range:
                overlap_count += 1
    print(overlap_count)
    
def part_two():
    overlap_count = 0
    for assignment in section_assignments:
        elf_assignments= assignment.split(',')
        elf_1, elf_2 = [elf.split('-') for elf in elf_assignments]
        elf_1 = [int(x) for x in elf_1]
        elf_2 = [int(x) for x in elf_2]

        elf_1_arr = set(range(elf_1[0], elf_1[1]+1))
        elf_2_arr = set(range(elf_2[0], elf_2[1]+1))
        overlap = elf_1_arr & elf_2_arr
        if len(overlap) > 0:
            overlap_count += 1
    print(overlap_count)

part_two()