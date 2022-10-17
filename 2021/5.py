with open('tests/5_given.txt') as f:
    data = f.read().splitlines()

lines = []
max_x = 0
max_y = 0
for line in data:
    coord_pair = line.split('->')
    coord_pair = [xy.split(',') for xy in coord_pair]
    coord_pair = [list(map(int, x)) for x in coord_pair]
    lines.append(coord_pair)

def draw_lines(lines):
    line_count = {}
    for line in lines:
        pair1 = line[0]
        pair2 = line[1]
        if pair1[1] == pair2[1] or pair1[0] == pair2[0]: # check diagonal
            if pair1[0] > pair2[0]:
                x_start = pair2[0]
                x_end = pair1[0]
            else:
                x_start = pair1[0]
                x_end = pair2[0]
            if pair1[1] > pair2[1]:
                y_start = pair2[1]
                y_end = pair1[1]
            else:
                y_start = pair1[1]
                y_end = pair2[1]
            for i in range(x_start, x_end+1):
                for j in range(y_start, y_end+1):
                    if (i, j) in line_count:
                        line_count[(i,j)] += 1
                    else:
                        line_count[(i,j)] = 1
    return line_count   

def draw_diagonals(lines, line_count):
    for line in lines:
        pair1 = line[0]
        pair2 = line[1]
        if pair1[1] != pair2[1] and pair1[0] != pair2[0]:
            if pair1[0] > pair2[0]:
                x_val = list(range(pair1[0], pair2[0]-1, -1))
            else:
                x_val = list(range(pair1[0], pair2[0]+1))
            if pair1[1] > pair2[1]:
                y_val = list(range(pair1[1], pair2[1]-1, -1))
            else:
                y_val = list(range(pair1[1], pair2[1]+1))    
            
            for i in range(len(x_val)):
                x = x_val[i]
                y = y_val[i]
                if (x, y) in line_count:
                    line_count[(x,y)] += 1
                else:
                    line_count[(x,y)] = 1     
    return line_count          

def part_1(lines):
    line_count = draw_lines(lines)
    get_overlap = list(line_count.values())
    num_overlap = len(get_overlap) - get_overlap.count(1)
    return num_overlap

def part_2(lines):
    line_count = draw_lines(lines)
    line_count = draw_diagonals(lines, line_count)
    get_overlap = list(line_count.values())
    num_overlap = len(get_overlap) - get_overlap.count(1)
    return num_overlap


print("Part 1:", part_1(lines))
print("Part 2:", part_2(lines))