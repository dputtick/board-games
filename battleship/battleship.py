class Game():
    def __init__(self):
        # objects we need: board object, player objects
        # methods we need: moves, checking for 
        pass

    def run(self):
        pass

    def setup_phase(self):
        pass

    def game_loop(self):
        pass


class Player():
    def __init__(self):
        self.human = True

    def get_move(self):
        pass


class Board():
    def __init__(self, size):
        row = [0 for _ in range(size)]
        self._matrix = [list(row) for _ in range(size)]
        self._ships = []


    def render(self):
        for row in self._matrix:
            print(row)


    def place_ship(self, location, length, direction):
        ship = {'location': location, 'length': length, 'direction': direction}
        self._ships.append(ship)
        self._matrix[location[0]][location[1]] = 'x'


def main():
    board_size = 4
    board = Board(board_size)
    board.render()


if __name__ == '__main__':
    main()
