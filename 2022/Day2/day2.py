with open('Day2/input') as f:
    data = f.read().splitlines()

# scores = {
#     'AY': 6,
#     'BZ': 6,
#     'CX': 6,
#     'AX': 3,
#     'BY': 3,
#     'CZ': 3
# }

scores_index = {
    'X': 0,
    'Y': 1,
    'Z': 2
    }

game_score = {
    'X': 0,
    'Y': 3,
    'Z': 6
    }
rock_paper = {
    # lose, draw, win
    'A': [3, 1, 2],
    'B': [1, 2, 3],
    'C': [2, 3, 1]
}

# rock_paper_scissors = {
#     'X': 1,
#     'Y': 2,
#     'Z': 3
#     }

score = 0
for line in data:
    combo = line.replace(' ', '')
    score_index = scores_index[combo[1]]
    score += rock_paper[combo[0]][score_index]
    score += game_score[combo[1]]

print(score)

    





