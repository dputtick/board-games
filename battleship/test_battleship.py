import pytest
import battleship


@pytest.fixture
def board():
    return battleship.Board(player_id=1)

@pytest.fixture
def new_game():
    return battleship.Game()

@pytest.fixture
def start_game():
    game = battleship.Game()
    # TODO: make arbitrary placements
    return game

# how do I make stubs to test input()

class TestBoardObject:
    def test_board_init_size(self, board):
        assert len(board.matrix) == 4

    def test_board_init_empty(self, board):
        for row in board.matrix:
            assert row == [0] * 4

    def test_matrix_updates_on_place_ship(self, board):
        add_ship_origin_vertical(board)
        assert board.matrix[0][0] == 1

    def test_ships_dict_updates_on_place_ship(self, board):
        add_ship_origin_vertical(board)
        test_ship = board.ships[1]
        assert test_ship['location'] == (0, 0)
        assert test_ship['length'] == 2
        assert test_ship['direction'] == 'v'


class TestSetup:
    def test_setup(self):
        pass



class TestGamePlay:
    def test_user_guess_hit(self, start_game):
        assert # guess should modify board, result in a hit

    def test_user_guess_miss(self):
        assert # guess should modify board, result in a miss

    def test_run(self):


class TestUI:
    def test_user_sees_rendered_board(self):
        pass


# Helper Functions ######

def add_ship_origin_vertical(board):
    board.place_ship(1, {'location': (0, 0), 'length': 2, 'direction': 'v'})
