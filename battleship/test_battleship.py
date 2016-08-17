import pytest
import battleship as b

class TestBoard:
    def test_init(self):
        board = b.Board(4)
        assert len(board._matrix) == 4