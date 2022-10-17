with open('tests/8_example.txt') as f:
    data = f.read().splitlines()

#inputs = {'in_sig':[], 'output':[]}
lines = [line.split('|') for line in data]
in_sig = [line[0] for line in lines]
output = [line[1] for line in lines]
in_sig = [signal.split() for signal in in_sig]
output = [signal.split() for signal in output]

def part_1(output):
    unique_segment_num = [2, 3, 4, 7]
    count_num = 0
    for row in output:
        for digit in row:
            if len(digit) in unique_segment_num:
                count_num += 1
    return count_num

def filter_by_segment_count(digits, segment_count):
    return list(filter(lambda digit: len(digit) == segment_count, digits))

def find_one(digits):
    return filter_by_segment_count(digits, 2)[0]

print(find_one(in_sig[3]))