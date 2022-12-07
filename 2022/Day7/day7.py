
def calculate_size(filesystem, directory) -> int:
    folders, files = filesystem[directory]
    size  = 0
    for file in files:
        size += int(file[1])
    for folder in folders:
        size += calculate_size(filesystem, folder)
    return size

def build_filesystem(data):
    filesystem = {}
    directories_visited = []
    filesystem['/'] = [[], [] ]
    for line in data:
        if line.startswith('$'):
            if 'cd' in line:
                if '..' in line:
                    directories_visited.pop()
                    current_directory = '/'.join(directories_visited)
                else:
                    directories_visited.append(line[5:])
                    current_directory = '/'.join(directories_visited)
        else:
            if 'dir' in line:
                filesystem[current_directory][0].append(current_directory + '/' + line[4:])
                filesystem[current_directory + '/' + line[4:]] = [[], [] ]
            else:
                size, name = line.split(' ')
                filesystem[current_directory][1].append((name, size))
    return filesystem

def part_one(input_file):
    with open(input_file) as f:
        data = f.read().splitlines()
    filesystem = build_filesystem(data)
    total_size_larger_10000 = 0
    directory_sizes = {}
    for key in filesystem.keys():
        size = calculate_size(filesystem, key)
        directory_sizes[key] = size
        if size <= 100000:
            total_size_larger_10000 += size
    print(f"Sum of folders with size below 100000: {total_size_larger_10000}")

def part_two(input_file):
    with open(input_file) as f:
        data = f.read().splitlines()
    filesystem = build_filesystem(data)
    directory_sizes = {}
    for key in filesystem.keys():
        size = calculate_size(filesystem, key)
        directory_sizes[key] = size
    total_amount = directory_sizes['/']
    unused = 70000000 - total_amount
    amount_required = 30000000 - unused
    directory_sizes = directory_sizes.items()
    valid_sizes = list(filter(lambda x: x[1] > amount_required, directory_sizes))
    valid_sizes.sort(key=lambda x: x[1])
    print(f"Size of folder to be deleted: {valid_sizes[0][1]}")


part_one('input.txt')
part_two('input.txt')
