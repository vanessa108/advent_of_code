import numpy as np

def part_one(input_file):
    with open(input_file) as f:
        data = f.read().splitlines()
    trees  = []
    for row in data:
        trees.append([int(n) for n in row])
    trees = np.array(trees)
    num_rows = len(trees)
    num_cols = len(trees[0])
    visible = num_rows * 2 + (num_cols-2) * 2
    for i in range(1, num_rows-1):
        for j in range(1, num_cols-1):
            tree_height = trees[i, j]
            left_max = trees[:i, j].max()
            right_max = trees[i+1:, j].max()
            top_max = trees[i, :j].max()
            bottom_max = trees[i, j+1:].max()
            max_heights = [left_max, right_max, top_max, bottom_max]
            for height in max_heights:
                if tree_height > height:
                    visible += 1
                    break
    print(f'number of visible trees: {visible}')
    


def part_two(input_file):
    with open(input_file) as f:
        data = f.read().splitlines()
    trees  = []
    for row in data:
        trees.append([int(n) for n in row])
    trees = np.array(trees)
    num_rows = len(trees)
    num_cols = len(trees[0])
    viewing_scores = []
    for i in range(1, num_rows-1):
        for j in range(1, num_cols-1):
            tree_height = trees[i, j]
            top_view = trees[:i, j][::-1]
            bottom_view = trees[i+1:, j]
            left_view = trees[i, :j][::-1]
            right_view = trees[i, j+1:]
            views = [left_view, right_view, top_view, bottom_view]
            view_score = 1
            for view in views:
                if tree_height > view.max():
                    this_score = len(view)
                else:
                    this_score = np.argmax(view >= tree_height) + 1 
                view_score = view_score * this_score
            viewing_scores.append(view_score)

    print(f'maximum viewing score:{max(viewing_scores)}')
part_one('input.txt')
part_two('input.txt')