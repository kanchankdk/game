# creation of the board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

current_player = "X"
game_is_on = True
winner = None


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def handle_turn():
    print(current_player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")
    board[position] = current_player


def swap_players():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


def check_game_is_win_or_tie():
    game_winner()
    game_tie()


def game_winner():
    global winner
    rowwin = row_win()
    colwin = column_win()
    diawin = diagonal_win()

    if rowwin:
        winner = rowwin
    elif colwin:
        winner = colwin
    else:
        winner = diawin


def row_win():
    global game_is_on

    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3:
        game_is_on = False

    if row1:
        return board[0]

    elif row2:
        return board[5]

    elif row3:
        return board[6]


def column_win():
    global game_is_on

    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"

    if col1 or col2 or col3:
        game_is_on = False

    if col1:
        return board[0]

    elif col2:
        return board[1]

    elif col3:
        return board[5]


def diagonal_win():
    global game_is_on

    dia1 = board[0] == board[4] == board[8] != "-"
    dia2 = board[2] == board[4] == board[6] != "-"

    if dia1 or dia2:
        game_is_on = False

    if dia1:
        return board[0]

    elif dia2:
        return board[4]


def game_tie():
    global game_is_on
    if "-" not in board:
        game_is_on = False
        return "Match is Tied true"
    else:
        return "Match is Tied false"


def display_game_details():
    while game_is_on:
        display_board()

        handle_turn()

        swap_players()

        check_game_is_win_or_tie()

    if winner == "X":
        print("X is the winner")
    elif winner == "O":
        print("O is the winner")


display_game_details()
