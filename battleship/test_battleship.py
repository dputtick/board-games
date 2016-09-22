import pytest
import battleship as b


@pytest.fixture
def board():
    return b.Board(4)


class TestBoard:
    def test_init(self, board):
        assert len(board._matrix) == 4

    def test_place(self, board):
        board.place_ship((0,0), 2, 'v')
        assert board._matrix[0][0] == 'x'
        assert board._ships[-1]['location'] == (0,0)
