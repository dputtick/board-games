import pytest
import battleship as b


@pytest.fixture
def board():
    return b.Board(4)


class TestBoard:
    def test_init(self, board):
        assert len(board._matrix) == 4

    def test_matrix_updates_on_place_ship(self, board):
        add_ship_origin_vertical(board)
        assert board._matrix[0][0] == 'x'

    def test_ships_update_on_place_ship(self, board):
        add_ship_origin_vertical(board)
        test_ship = board._ships[-1]
        assert test_ship['location'] == (0,0)
        assert test_ship['length'] == 2
        assert test_ship['direction'] == 'v'


def add_ship_origin_vertical(board):
    board.place_ship((0,0), 2, 'v')