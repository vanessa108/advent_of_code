directions = {
    'R':[1, 0],
    'L':[-1, 0],
    'U':[0, 1],
    'D':[0, -1]
}

def follow_head(head, tail):
    x_distance = abs(head[0] - tail[0])
    y_distance = abs(head[1] - tail[1])
    #int(abs(xd)/xd)
    if not (x_distance <= 1 and y_distance <= 1):
        if x_distance != 0:
            tail[0] += int(x_distance/(head[0] - tail[0]))
        if y_distance != 0:
             tail[1] += int(y_distance/(head[1] - tail[1]))
    return tail

def part_one(input_file):
    with open(input_file) as f:
        data = f.read().splitlines()
    head = [0, 0]
    tail = [0, 0]
    tail_visted = set()
    for line in data:
        # line = list(line)
        n = int(line[2:])
        heading = line[0]
        direction = directions[heading]
        for _ in range(n):
            head[0] += direction[0]
            head[1] += direction[1]
            #print('head:', head, 'tail:', tail, 'before follow')
            tail = follow_head(head, tail)
            tail_visted.add(tuple(tail))
            #print('head:', head, 'tail:', tail, 'after follow')
    print('Number of tail visit positions:', len(tail_visted))

def part_two(input_file):
    with open(input_file) as f:
        data = f.read().splitlines()
    head = [0, 0]
    knots = [[0, 0] for _ in range(9)]
    tail_visited = set()
    for line in data:
        n = int(line[2:])
        heading = line[0]
        direction = directions[heading]
        for _ in range(n):
            head[0] += direction[0]
            head[1] += direction[1]
            knots[0] = follow_head(head, knots[0])
            for i in range(1, 9):
                knots[i] = follow_head(knots[i-1], knots[i])
            tail_visited.add(tuple(knots[-1]))
    print('Number of tail visit positions:', len(tail_visited))

part_one('input.txt')
part_two('input.txt')




