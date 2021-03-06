import random


def display_board(board):
    '''Returns a visual representation of the current board.'''
    empty_row = '   |   |   '
    token_row = ' {0} | {1} | {2} '
    full_row = '___|___|___'
    print()
    print(empty_row)
    print(token_row.format(board[1], board[2], board[3]))
    print(full_row)
    print(empty_row)
    print(token_row.format(board[4], board[5], board[6]))
    print(full_row)
    print(empty_row)
    print(token_row.format(board[7], board[8], board[9]))
    print(empty_row)
    print()


def get_move(player, board, piece):
    '''Returns a new move from either player, 
    or the computer if a 1 player game.'''
    if player in ('Player 1', 'Player 2'):
        move = input("{}, it's your turn. Enter 1-9:\n".format(player))
        while True:
            while True:
                try:
                    move = int(move)
                    break
                except ValueError:
                    move = input("Please enter a number 1-9.\n")
            if move in board:
                return move
            move = int(input("That square is already taken. Try again.\n"))
    elif player == 'Computer':
        return computer_move(board, piece)


def update_board(board, move, piece):
    '''Updates the board with a new move and returns it.'''
    board[move] = piece
    return board


def check_victory(board, piece):
    '''Checks whether the victory conditions are met for a given player.'''
    return ((board[1] == board[2] == board[3] == piece) or
    (board[4] == board[5] == board[6] == piece) or
    (board[7] == board[8] == board[9] == piece) or
    (board[1] == board[4] == board[7] == piece) or
    (board[2] == board[5] == board[8] == piece) or
    (board[3] == board[6] == board[9] == piece) or
    (board[1] == board[5] == board[9] == piece) or
    (board[3] == board[5] == board[7] == piece))


def play_again():
    '''Returns input from the player whether or not to start a new game.'''
    return input('Play again? y/n\n').lower() == 'y'


def one_or_two_players():
    '''Returns input from the player 
    whether to start in 1 or 2 player mode.'''
    return 2 if input('One or two players? 1/2\n') == '2' else 1


def empty_board():
    '''Makes a new blank board as a list'''
    return [None] + list(range(1, 10))

def main(first_mover):
    '''Function that actually handles playing the game.'''
    board = empty_board()
    player = first_mover
    while True:
        piece = player_dict[player]
        if player in ('Player 1', 'Player 2'):
            display_board(board)
        move = get_move(player, board, piece)
        update_board(board, move, piece)
        if check_victory(board, piece) == True:
            break
        if [loc for loc in board if str(loc).isdigit()] == []:
            display_board(board)
            print('The game ends in a draw.\n')
            if play_again() == True:
                player = invert_dict[player]
                main(player)
                return None
            else:
                print('Thanks for playing!')
                return None
        player = invert_dict[player]
    display_board(board)
    print('Congratulations {}, you won!\n'.format(player.lower()))
    if play_again() == True:
        player = invert_dict[player]
        main(player)
        return None
    else:
        print('Thanks for playing!')
        return None


def computer_move(board, piece):
    '''Returns a move for the computer in 1 player mode.'''
    invert_piece = {'X': 'O', 'O': 'X'}
    opp_piece = invert_piece[piece]
    transform_sides = {1:9, 9:1, 2:8, 8:2, 3:7, 7:3, 4:6, 6:4}
    corners = (1, 3, 7, 9)
    sides = (2, 4, 6, 8)
    board_tuple = tuple(board)
    open_spaces = tuple([loc for loc in board_tuple if str(loc).isdigit()])
    for loc in board_tuple:
        if loc in open_spaces:
            test_board = list(board_tuple)
            test_board[loc] = piece
            if check_victory(test_board, piece) == True:
                return loc
    for loc in board_tuple:
        if loc in open_spaces:
            test_board = list(board_tuple)
            test_board[loc] = opp_piece
            if check_victory(test_board, opp_piece) == True:
                return loc
    if len(open_spaces) == 9:
        return 1
    open_corners = [l for l in open_spaces if l in corners]
    open_sides = [l for l in open_spaces if l in sides]
    corners_list = [l for i, l in enumerate(board_tuple) if i in corners]
    sides_list = [l for i, l in enumerate(board_tuple) if i in sides]
    if len(open_spaces) == 8:
        if board_tuple[5] == opp_piece:
            return 1
        else:
            return 5
    if len(open_spaces) == 7:
        if opp_piece in sides_list:
            return 5
        if board_tuple[5] == opp_piece:
            return 9
        if opp_piece in [board_tuple[7], board_tuple[9]]:
            return 3
        if board_tuple[3] == opp_piece:
            return 7
    if len(open_spaces) == 6:
        if board_tuple[1] == opp_piece and board_tuple[9] == opp_piece:
            return 8
        if board_tuple[3] == opp_piece and board_tuple[7] == opp_piece:
            return 8
        if len(open_corners) == 3:
            if opp_piece in corners_list:
                if board_tuple[1] == opp_piece:
                    return 9
                if board_tuple[3] == opp_piece:
                    return 7
                if board_tuple[7] == opp_piece:
                    return 3
                if board_tuple[9] == opp_piece:
                    return 1
    if len(open_spaces) == 5:
        if len(open_corners) == 1:
            return open_corners[0]
        if 5 in open_spaces:
            return 5
    if open_corners:
        good_corners = [l for l in open_corners if transform_sides[l] 
                        in open_corners]
        if good_corners:
            return random.choice(good_corners)
    if 5 in open_spaces:
        return 5            
    good_sides = [l for l in open_sides if transform_sides[l] in open_sides]
    if good_sides:
        return random.choice(good_sides)
    if open_spaces:
        return random.choice(open_spaces)
    else:
        return None


if __name__ == '__main__':
    players = one_or_two_players()
    if players == 2:
        invert_dict = {'Player 1': 'Player 2', 'Player 2': 'Player 1'}
        player_dict = {'Player 1': 'X', 'Player 2': 'O'}
    if players == 1:
        invert_dict = {'Player 1': 'Computer', 'Computer': 'Player 1'}
        player_dict = {'Player 1': 'X', 'Computer': 'O'}
    main('Player 1')
    print('Goodbye :)')
    

