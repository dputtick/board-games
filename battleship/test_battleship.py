import pytest
import battleship as b


@pytest.fixture
def board():
    return b.Board(4, 1)


class TestBoard:
    def test_board_init_size(self, board):
        assert len(board.matrix) == 4

    def test_board_init_empty(self, board):
        for row in board.matrix:
            assert row == [0] * 4

    def test_matrix_updates_on_place_ship(self, board):
        add_ship_origin_vertical(board)
        assert board.matrix[0][0] == 1

    def test_ships_update_on_place_ship(self, board):
        add_ship_origin_vertical(board)
        test_ship = board.ships[1]
        assert test_ship['location'] == (0,0)
        assert test_ship['length'] == 2
        assert test_ship['direction'] == 'v'

def test_board_creation(board):
    assert len(board.matrix) == 4




def add_ship_origin_vertical(board):
    board.place_ship(1, {'location': (0,0), 'length': 2, 'direction': 'v'})

def make_board(size=4):
    return b.Board(size)