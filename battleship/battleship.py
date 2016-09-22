class Game():
    def __init__(self):
        # create board (maybe prompt for size)
        self.board = Board(4)
        players = []
        for playerid in (1, 2):
            players.append(Player(playerid))

    def run(self):
        self.setup_phase()

    def setup_phase(self):
        for player in self.players:
            ship_lengths = [2, 2]
            while ship_lengths:
                ship = player.get_locations(ship_lengths)
                if valid_ship(ship):
                    self.board.place_ship(ship_id, data)
    
    def valid_ship(self, ship):
        pass

    def game_loop(self):
        pass


class Player():
    def __init__(self, id_name):
        self.human = True
        self.id_name = id_name

    def get_move(self):
        move = input("Player {}, enter your next move".format(self.id_name))
        return move

    def get_locations(self):
        ship_lengths = [2, 2]
            while ship_lengths:
                print("Remaining ships: ", *ship_lengths)
                y, x = input("Player {} move:\n".format(self.id_name))
                

class Board():
    def __init__(self, size):
        row = [0 for _ in range(size)]
        self.matrix = [list(row) for _ in range(size)]
        self.ships = {}

    def render(self):
        for row in self._matrix:
            print(row)


    def place_ship(self, ship_id, data):
        '''Ship data format: {'location': (<y>, <x>), 'direction': <'v' or 'h'>,
        'length': <int>'''
        self.ships[ship_id] = data
        y, x = data['location']
        for _ in range(data['length']):
            self.matrix[y][x] = ship_id
            if data['direction'] == 'v':
                y -= 1
            else:
                x -= 1


def main():
    board_size = 4
    game = Game(board_size)
    game.run()


if __name__ == '__main__':
    main()
