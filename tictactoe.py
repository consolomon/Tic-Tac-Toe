# write your code here
def winner_is(state, player):
    main_diag_num = 0
    off_diag_num = 0

    for i in range(3):
        column_num = 0
        for column in range(0 + i, 9 + i, 3):
            column_num += 1 if state[column] == player else 0
        if column_num == 3:
            return True
        row_num = 0
        for row in range(0 + 3 * i, 3 + i * 3, 1):
            row_num += 1 if state[row] == player else 0
        if row_num == 3:
            return True
        main_diag_num += 1 if state[4 * i] == player else 0
        off_diag_num += 1 if state[2 + 2 * i] == player else 0
    if main_diag_num == 3 or off_diag_num == 3:
        return True
    else:
        return False


def state_check(state_line):
    x_num = 0
    y_num = 0
    for c in state_line:
        if c == "X":
            x_num += 1
        elif c == "O":
            y_num += 1
    if abs(x_num - y_num) > 1:
        game_state = "Impossible"
    elif x_num + y_num == len(state_line):
        game_state = "Finished"
    else:
        game_state = "Game not finished"

    if winner_is(state_line, "X") and winner_is(state_line, "O"):
        game_state = "Impossible"
    elif winner_is(state_line, "X"):
        game_state = "X wins"
    elif winner_is(state_line, "O"):
        game_state = "O wins"
    elif game_state == "Finished":
        game_state = "Draw"
    return game_state


def turn_is_correct(turn_line, grid):
    try:
        coord = [int(x) for x in turn_line.split()]
    except TypeError:
        print("You should enter numbers!")
        return False
    if coord[0] > 3 or coord[0] < 1 or coord[1] > 3 or coord[1] < 1:
        print("Coordinates should be from 1 to 3!")
        return False
    elif grid[coord[0] - 1][coord[1] - 1] != " ":
        print("This cell is occupied! Choose another one!")
        return False
    else:
        return True


def print_the_grid():
    print("---------")
    for row in grid:
        line = " ".join(row)
        print("|", line, "|")
    print("---------")


state_line = [" " for _ in range(9)]
grid = []
for i in range(3):
    grid.append([])
    for j in range(3):
        grid[i].append(state_line[i * 3 + j])
game_state = state_check(state_line)
player = "O"
while game_state == "Game not finished":
    if player == "X":
        player = "O"
    else:
        player = "X"
    print_the_grid()
    global turn_line
    turn_check = False
    while not turn_check:
        turn_line = input()
        turn_check = turn_is_correct(turn_line, grid)
    coord = [int(x) - 1 for x in turn_line.split()]
    grid[coord[0]][coord[1]] = player
    state_line[coord[0] * 3 + coord[1]] = player
    game_state = state_check(state_line)

print_the_grid()
print(game_state)
