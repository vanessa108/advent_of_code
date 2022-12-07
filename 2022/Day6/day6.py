with open('input.txt') as f:
    data = f.read()

def part_one():
    
    for start in range(len(data)):
        current_arr = []
        for i in range(start, start+4):
            if data[i] in current_arr:
                break
            else:
                current_arr.append(data[i])
                if len(current_arr) == 4:
                    return start + 4
            


def part_two():
    for start in range(len(data)):
        current_arr = []
        for i in range(start, start+14):
            if data[i] in current_arr:
                break
            else:
                current_arr.append(data[i])
                if len(current_arr) == 14:
                    return start + 14

print(part_one())