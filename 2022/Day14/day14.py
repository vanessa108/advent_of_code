from aocd import submit
def part_one(input_file):
    with open(input_file) as f:
        data = f.read().splitlines()
    rocks = set()
    history = []
    abyss_height = 0
    for line in data:
        line = line.split(' -> ')
        line = [x.split(',') for x in line]
        line = [list(map(lambda a: int(a), x)) for x in line]
        for i in range(1, len(line)):
            coord1, coord2 = line[i-1], line[i]
            start_x = min([coord1[0], coord2[0]])
            end_x = max([coord1[0], coord2[0]])
            start_y = min([coord1[1], coord2[1]])
            end_y = max([coord1[1], coord2[1]])
            for x in range(start_x, end_x+1):
                for y in range(start_y, end_y+1):
                    rocks.add((x, y))
                    abyss_height = max(abyss_height, y)
    grains = 0
    abyss = False
    while abyss == False:
        sand = (500, 0)
        x, y = sand
        while True:
            if y > abyss_height+1:
                abyss = True
                break
            if (x, y+1) not in rocks:
                y += 1
            elif (x-1, y+1) not in rocks:
                x-=1
                y+=1
            elif (x+1, y+1) not in rocks:
                x+=1
                y+=1
            else:
                rocks.add((x, y))
                grains += 1
                break
    print('Number of grains:', grains)
    #submit(grains)    
        
def part_two(input_file):
    with open(input_file) as f:
        data = f.read().splitlines()
    rocks = set()
    history = []
    abyss_height = 0
    for line in data:
        line = line.split(' -> ')
        line = [x.split(',') for x in line]
        line = [list(map(lambda a: int(a), x)) for x in line]
        for i in range(1, len(line)):
            coord1, coord2 = line[i-1], line[i]
            start_x = min([coord1[0], coord2[0]])
            end_x = max([coord1[0], coord2[0]])
            start_y = min([coord1[1], coord2[1]])
            end_y = max([coord1[1], coord2[1]])
            for x in range(start_x, end_x+1):
                for y in range(start_y, end_y+1):
                    rocks.add((x, y))
                    abyss_height = max(abyss_height, y)
    grains = 0

    while (500, 0) not in rocks:
        sand = (500, 0)
        x, y = sand
        while True:
            if y  == abyss_height+1:
                rocks.add((x,y))
                grains +=1
                break
            if (x, y+1) not in rocks:
                y += 1
            elif (x-1, y+1) not in rocks:
                x-=1
                y+=1
            elif (x+1, y+1) not in rocks:
                x+=1
                y+=1
            else:
                rocks.add((x, y))
                grains += 1
                break
    print('Number of grains:', grains)
    submit(grains)

part_one('input.txt')
part_two('input.txt')