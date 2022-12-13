def part_one(input_file):
    with open(input_file) as f:
        data = f.read().splitlines()

    pairs = []
    for i in range(0, len(data), 3):
        pair1 = eval(data[i])
        pair2 = eval(data[i+1])
        pairs.append([pair1, pair2])
    print(pairs)

        

part_one('example.txt')