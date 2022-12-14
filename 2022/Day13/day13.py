from aocd import submit 

def check_order(left, right):
    if type(left) == int and type(right) == int:
        if left < right:
            return 'right'
        elif left == right:
            return 'equal'
        else:
            return 'wrong'
    elif type(left) == int and type(right) == list:
        return check_order([left], right)
    elif type(left) == list and type(right) == int:
        return check_order(left, [right])
    else:
        if len(left) == 0:
            return 'right'
        elif len(right) == 0:
            return 'wrong'       
        while len(left) > 0:
            valid = check_order(left[0], right[0])
            if valid == 'equal':
                if len(right) == 1 and len(left) > 1:
                    return 'wrong'
                else:
                    left = left[1:]
                    right = right[1:]
            else:
                return valid
        return 'right'


def part_one(input_file):
    with open(input_file) as f:
        data = f.read().splitlines()

    pairs = []
    for i in range(0, len(data), 3):
        pair1 = eval(data[i])
        pair2 = eval(data[i+1])
        pairs.append([pair1, pair2])
    index_sum = 0
    for i, pair in enumerate(pairs):
        valid = check_order(pair[0], pair[1]) 
        if valid == 'right':
            index_sum += i+1
    print('Number of correctly ordered pairs:', index_sum)

def bubble_sort(packets):
    for i in range(len(packets)):
        for j in range(len(packets)-i-1):
            if check_order(packets[j], packets[j+1]) == 'wrong':
                packets[j], packets[j+1] = packets[j+1], packets[j]
    return packets



def part_two(input_file):
    with open(input_file) as f:
        data = f.read().splitlines()
    packets = [[[2]], [[6]]]
    for row in data:
        if row != '':
            packet = eval(row)
            packets.append(packet)
    packets = bubble_sort(packets)
    first_packet = packets.index([[2]]) +1
    second_packet = packets.index([[6]]) + 1
    print('Decoder key for distress signal:', first_packet * second_packet)
    submit(first_packet * second_packet)


part_one('input.txt')
part_two('input.txt')