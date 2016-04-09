import connect4 as c
import pdb


empty_board = [
            [' ', ' ', ' ', ' ', ' '], 
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ']
            ]

board = [
        [' ', ' ', ' ', ' ', ' '], 
        ['X', ' ', ' ', 'X', ' '],
        [' ', 'X', 'X', ' ', ' '],
        [' ', 'X', 'X', ' ', ' '],
        ['X', ' ', ' ', ' ', ' ']
        ]

full_board = [
            ['X', 'X', 'X', 'X', 'X'], 
            ['X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X']
            ]


def test_move_getter(board):
    move, new_board = c.new_move('P1', board)
    print(move)
    c.print_board(new_board)


def test_victory_checker(board):
    print(c.check_verticals(board, 'X'))
    print(c.check_horizontals(board, 'X'))
    print(c.check_diagonals(board, 'X'))

def main():
    test_move_getter(empty_board)


#if __name__ == '__main__':
#    main()
    # test_victory_checker(board)
    


# should print a properly displayed 5x5 board with 'X' on bottom row
# board2 = [['X', ' ', ' ', ' ', ' '], 
#           ['X', ' ', ' ', ' ', ' '],
#           ['X', 'X', ' ', ' ', ' '],
#           ['X', ' ', ' ', ' ', ' '],
#           ['X', ' ', ' ', ' ', ' ']]
# c.board_printer(board2)