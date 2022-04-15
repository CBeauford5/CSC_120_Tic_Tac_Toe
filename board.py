board = [["-" for i in range(3)] for j in range(3)]


def print_board():
    for x in board:
        print(x)


def check_mark(row, col):
    if board[row][col] == '-':
        return True
    else:
        return False


def place_mark(row, col, player_id):
    if player_id == 1:
        board[row][col] = 'X'
    if player_id == 2:
        board[row][col] = 'O'


def check_win(player_id):
    if player_id == 1:
        if (board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X')\
                or (board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X')\
                or (board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X'):
            return True

        elif (board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X')\
                or (board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X')\
                or (board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X'):
            return True

        elif (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X')\
                or (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X'):
            return True

        else:
            return False

    if player_id == 2:
        if (board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O')\
                or (board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O')\
                or (board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O'):
            return True

        elif (board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O')\
                or (board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O')\
                or (board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O'):
            return True

        elif (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O')\
                or (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'):
            return True

        else:
            return False


def main():
    print_board()
    print(check_mark(0, 1))
    print('')

    place_mark(0, 0, 2)
    place_mark(0, 1, 2)
    place_mark(0, 2, 2)
    print_board()
    print(check_win(2))
    print('')

    place_mark(0, 2, 1)
    place_mark(1, 2, 1)
    place_mark(2, 2, 1)
    print_board()
    print(check_win(1))
    print('')

    place_mark(0, 2, 2)
    place_mark(1, 1, 2)
    place_mark(2, 0, 2)
    print_board()
    print(check_win(2))


main()
