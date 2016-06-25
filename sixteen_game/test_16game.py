import sixteen_game
import pytest
import curses

@pytest.fixture
def curses_setup():
    curses.wrapper(setup_fixture)

def setup_fixture(stdscr):
    board_size = 3
    solved_board_list = list(range(1, (board_size ** 2))) + [' ']
    return sixteen_game.list_to_matrix(solved_board_list, board_size)


# 3 board types: solved, valid but not solved, or invalid
# possible sizes = 3 or 4


def test_printing(curses_setup):
    sixteen_game.board_printer()