def empty_board(x, y):
    '''Returns a board data structure based on the two dimensions passed in'''
    column = [' ' for y in range(y)]
    board = [list(column) for x in range(x)]
    return board


def print_board(board):
    '''Takes the current board structure and prints it to the terminal'''
    board_width = len(board)
    board_height = len(board[0])
    print('\n')
    for num in range(board_height):
        i = num + 1
        row = [column[-i] for column in board]
        print(row)
    print('\n')
    print([str(i + 1) for i in range(board_width)])
            

def new_move(player, board):
    player_token = {'P1': 'X', 'P2': 'O'}
    move = input('{}, type the number of desired column:\n'.format(player))
    move_index = int(move) - 1
    while True:
        if move_index in [i for i in range(len(board))]: #len(board) == # cols
            if board[move_index][-1] == ' ': #check if space in chosen column
                insert_spot = board[move_index].index(' ')
                board[move_index][insert_spot] = player_token[player]
                return move, board
            else:
                move = input('That column is full! Pick another:\n')
                move_index = int(move) - 1
        else:
            move = input('Please enter a valid number of a column:\n')
            move_index = int(move) - 1
    

def check_draw(board):
    '''Returns True if every board space has been filled'''

    counter = 0
    for column in board:
        counter += column.count(' ')
    if counter == 0:
        return True


def check_verticals(board, token):
    '''Checks columns for 4 in a row of token, returns True if exists'''

    for column in board:
        column_string = ''.join(column)
        if column_string.find(token * 4) != -1:
            return True


def check_horizontals(board, token):
    '''Checks rows for 4 in a row of token, returns True if exists'''

    board_height = len(board[0])
    for i in range(board_height): # try using zip here instead of list comp
        row = [column[i] for column in board]
        row_string = ''.join(row)
        if row_string.find(token * 4) != -1:
            return True


def check_diagonals(board, token):
    '''Checks diagonals for 4 in a row of token, returns True if exists'''

    board_width = len(board)
    board_height = len(board[0])
    diagonal_direction_options = ((4, 1), (-4, -1))
    for row in range(board_height):
        for col in range(board_width):
            for end, step in diagonal_direction_options:
                try:
                    column_shift = [j for j in range(0, end, step)]
                    diagonal = [board[row + i][col + column_shift[i]] 
                                for i in range(4)]
                    diagonal_string = ''.join(diagonal)
                    if diagonal_string.find(token * 4) != -1:
                        return True, step
                except IndexError:
                    pass


def victory_checker(board):
    '''Returns True if victory, False if continue, and 'draw' if a tie'''

    player_tokens = {'P1': 'X', 'P2': 'O'}
    if check_draw(board) == True:
        return 'Draw', None
    for player, token in player_tokens.items():
        if check_verticals(board, token) == True:
            return True, player
        elif check_horizontals(board, token) == True:
            return True, player
        elif check_diagonals(board, token) == True:
            return True, player
    else:
        return False, None


def move_recorder(move, board, move_history):
    move_history.append((move, board))
    return move_history


def play_again():
    again = input('Play again? (y/n)\n')
    if again.lower() == 'y':
        return True
    else:
        return False


def main():
    move_history = []
    player = 'P1'
    switch_player = {'P1': 'P2', 'P2': 'P1'}
    x, y = 5, 5
    board = empty_board(x, y)
    while True:
        print_board(board)
        move, board = new_move(player, board)
        move_history = move_recorder(move, board, move_history)
        victory, winner = victory_checker(board)
        if victory == 'Draw':
            print_board(board)
            print('The game is a draw.')
            if play_again() == True:
                main()
            else:
                break
        elif victory == True:
            print_board(board)
            print('{} wins!'.format(winner))
            if play_again() == True:
                main()
            else:
                break
        elif victory == False:
            player = switch_player[player]
    print('Thanks for playing!')
    return

def test():
    board = empty_board(5, 5)
    print_board(board)
    print(board)
    move, board = new_move('P1', board)
    print_board(board)
    print(board)

if __name__ == '__main__':
    main()


# Function that returns the desired board size
# Function that draws the board for the user
# Function that gets a move and returns it
# Function that adds the move to the board
# Function that checks for victory conditions
# Function that checks for draw conditions
# Function that records the sequence of moves that were made