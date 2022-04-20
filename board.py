board = [["-" for i in range(3)] for j in range(3)]


def print_board():
    print(' ')
    for x in board:
        print(x)
    print(' ')


def check_mark(row, col):
    if board[int(row)][int(col)] == '-':
        return True
    else:
        return False


def place_mark(row, col, player_id):
    if player_id == 1:
        board[int(row)][int(col)] = 'X'
    if player_id == 2:
        board[int(row)][int(col)] = 'O'


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
    turn_num = 0
    while not check_win(1) or not check_win(2):

        print_board()
        row1 = input('Player 1: Please enter a row to place your X (0-2): ')
        while row1 not in ['0', '1', '2']:
            print('Please enter a valid row number.')
            row1 = input('Player 1: Please enter a row to place your X (0-2): ')

        col1 = input('Player 1: Please enter a column to place your X (0-2): ')
        while col1 not in ['0', '1', '2']:
            print('Please enter a valid column number.')
            col1 = input('Player 1: Please enter a column to place your X (0-2): ')

        while not check_mark(row1, col1):
            print('This space is occupied. Choose another space.')
            row1 = input('Player 1: Please enter a row to place your X (0-2): ')
            while row1 not in ['0', '1', '2']:
                print('Please enter a valid row number.')
                row1 = input('Player 1: Please enter a row to place your X (0-2): ')

            col1 = input('Player 1: Please enter a column to place your X (0-2): ')
            while col1 not in ['0', '1', '2']:
                print('Please enter a valid column number.')
                col1 = input('Player 1: Please enter a column to place your X (0-2): ')

        place_mark(row1, col1, 1)
        if check_win(1):
            print_board()
            print('Player 1 has won the game!')
            break
        turn_num += 1
        if turn_num == 9:
            print_board()
            print('This game was a tie!')
            break

        print_board()
        row2 = input('Player 2: Please enter a row to place your O (0-2): ')
        while row2 not in ['0', '1', '2']:
            print('Please enter a valid row number.')
            row2 = input('Player 2: Please enter a row to place your O (0-2): ')

        col2 = input('Player 2: Please enter a column to place your O (0-2): ')
        while col2 not in ['0', '1', '2']:
            print('Please enter a valid column number.')
            col2 = input('Player 2: Please enter a column to place your O (0-2): ')

        while not check_mark(row2, col2):
            print('This space is occupied. Choose another space.')
            row2 = input('Player 2: Please enter a row to place your O (0-2): ')
            while row2 not in ['0', '1', '2']:
                print('Please enter a valid row number.')
                row2 = input('Player 2: Please enter a row to place your O (0-2): ')

            col2 = input('Player 2: Please enter a column to place your O (0-2): ')
            while col2 not in ['0', '1', '2']:
                print('Please enter a valid column number.')
                col2 = input('Player 2: Please enter a column to place your O (0-2): ')

        place_mark(row2, col2, 2)
        if check_win(2):
            print_board()
            print('Player 2 has won the game!')
            break
        turn_num += 1


main()
