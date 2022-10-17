with open('tests/4_given.txt') as f:
    data = f.read().splitlines()

boards = []

numbers_drawn = data[0].split(',')
numbers_drawn = list(map(int, numbers_drawn))
# extract all boards
for i in range(2, len(data)- 4, 6):
    board = {'rows':[], 'marks':[], 'complete': False}
    this_board = [data[i], data[i+1], data[i+2], data[i+3], data[i+4]]
    this_board = [x.split() for x in this_board]
    board['rows'] = [list(map(int, x)) for x in this_board] # convert rows from string to int
    board['marks'] = [['O' for i in range(5)] for j in range(5)]
    # I initally created  board['marks'] = [['O']*5]*5 but found each row referred to the same int object
    boards.append(board)

def update_boards(boards, drawn_num):
    for board in boards:
        this_board = board['rows']
        for i in range(len(this_board)):
            for j in range(len(this_board)):
                if this_board[i][j] == drawn_num:
                    board['marks'][i][j] = 'X'
    return boards


def update_win(boards):
    for board in boards:
        if not board['complete']:
            win_state = ['X', 'X', 'X', 'X','X']
            if win_state in board['marks']:
                board['complete'] = True
            if win_state in get_columns(board):
                board['complete'] = True
    return boards

def check_win(boards):
    for board in boards:
        if board['complete'] == True:
            return board
    return False

def get_columns(board):
    marks = board['marks']
    columns = zip(marks[0], marks[1], marks[2], marks[3], marks[4])
    columns = list(map(list, list(columns)))
    return columns

def calculate_score(board):
    score = 0
    values = board['rows']
    marks = board['marks']
    for i in range(len(values)):
        for j in range(len(values)):
            if marks[i][j] == 'O':
                score += values[i][j]
    return score

def num_won(boards):
    count = 0
    for board in boards:
        if board['complete']:
            count += 1
    return num_won

def track_wins(boards):
    board_won = [False] * len(boards)
    for i in range(len(boards)):
        if boards[i]['complete']:
            board_won[i] = True
    return board_won

def part_1(boards):
    win_found = check_win(boards)
    i = 0
    while not win_found and i < len(numbers_drawn):
        boards = update_boards(boards, numbers_drawn[i])
        boards = update_win(boards)
        win_found = check_win(boards)
        i+=1
    final_score = calculate_score(win_found) * numbers_drawn[i-1]
    return final_score



def part_2(boards):
    i = 0
    prev_board_won = track_wins(boards)
    while i < len(numbers_drawn):
        boards = update_boards(boards, numbers_drawn[i])
        boards = update_win(boards)
        board_won = track_wins(boards)
        if board_won == [True] * len(boards):
            losing_board_idx = prev_board_won.index(False)
            losing_board = boards[losing_board_idx]
            final_score = calculate_score(losing_board) * numbers_drawn[i]
            return final_score
        prev_board_won = board_won
        i+=1

print("Part 1:", part_1(data))
print("Part 2:", part_2(data))