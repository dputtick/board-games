import sixteen_game
import pytest
import curses

# 3 board types: solved, valid but not solved, or invalid
# possible sizes = 3 or 4


def setup_board(board_size=3):
    solved_board_list = list(range(1, (board_size ** 2))) + [' ']
    return sixteen_game.list_to_matrix(solved_board_list, board_size)


def test_printing(stdscr, board_matrix):
    curses.use_default_colors()
    curses.curs_set(0)
    stdscr.erase()
    sixteen_game.board_printer(stdscr, board_matrix)
    curses.napms(2000)
    y_coord = 0
    for row in board_matrix:
        row_str = ''.join([str(num).rjust(2) for num in row])
        stdscr.addstr(y_coord, 0, row_str)
        y_coord += 1
    stdscr.refresh()
    curses.napms(2000)


if __name__ == '__main__':
    board_matrix = setup_board()
    curses.wrapper(test_printing, board_matrix)