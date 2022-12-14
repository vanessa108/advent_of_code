from aocd import submit
import string
import numpy as np

def shortest_path(graph, start):
    distances = [float('inf') for _ in range(len(graph))]
    visited = [False for _ in range(len(graph))]
    distances[start] = 0
    while True:
        shortest_distance = float('inf')
        shortest_index = -1
        for i in range(len(graph)):
            if distances[i] < shortest_distance and not visited[i]:
                shortest_distance = distances[i]
                shortest_index = i
        if shortest_index == -1:
            return distances
        for i in range(len(graph[shortest_index])):
            if graph[shortest_distance][i] != 0 and distances[i] > distances[shortest_index] + graph[shortest_index][i] and abs(graph[shortest_distance][i] - graph[shortest_index][i]) <= 1:
                distances[i] = distances[shortest_index] + graph[shortest_index][i]
        visited[shortest_index] = True

def part_one(input_file):
    with open(input_file) as f:
        data = f.read().splitlines()
    data = [list(row) for row in data]
    alphabet = string.ascii_letters
    graph = []
    for row in data:
        graph_row = []
        for letter in row:
            graph_row.append(alphabet.index(letter))
        graph.append(graph_row)
    # for row in data:
    graph = np.array(graph)
    start = np.where(graph==44)
    end = np.where(graph==30)
    print(start, end)



part_one('example.txt')


def find_shortest_paths(graph, start_point):
    # initialize graphs to track if a point is visited,
    # current calculated distance from start to point,
    # and previous point taken to get to current point
    visited = [[False for col in row] for row in graph]
    distance = [[float('inf') for col in row] for row in graph]
    distance[start_point[0]][start_point[1]] = 0
    prev_point = [[None for col in row] for row in graph]
    n, m = len(graph), len(graph[0])
    number_of_points, visited_count = n * m, 0
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    min_heap = []

    # min_heap item format:
    # (pt's dist from start on this path, pt's row, pt's col)
    heapq.heappush(min_heap, (distance[start_point[0]][start_point[1]], start_point[0], start_point[1]))

    while visited_count < number_of_points:
        current_point = heapq.heappop(min_heap)
        distance_from_start, row, col = current_point
        for direction in directions:
            new_row, new_col = row + direction[0], col + direction[1]
            if -1 < new_row < n and -1 < new_col < m and not visited[new_row][new_col]:
                dist_to_new_point = distance_from_start + graph[new_row][new_col]
                if dist_to_new_point < distance[new_row][new_col]:
                    distance[new_row][new_col] = dist_to_new_point
                    prev_point[new_row][new_col] = (row, col)
                    heapq.heappush(min_heap, (dist_to_new_point, new_row, new_col))
        visited[row][col] = True
        visited_count += 1

    return distance, prev_point