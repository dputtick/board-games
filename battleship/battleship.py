class Game():
    def __init__(self):
        self.players = [Player(player_id) for player_id in [1]]

    def run(self):
        self.setup_phase()
        self.game_loop()

    def setup_phase(self):
        for player in self.players:
            player.initial_placements()

    def game_loop(self):
        while True:
            break
        pass


class Player():
    def __init__(self, player_id):
        self.human = True
        self.player_id = player_id
        self.board = Board(player_id)

    def initial_placements(self):
        ship_lengths = [2]
        ship_id = 1
        while ship_lengths:
            ship_data = self.get_locations(ship_lengths)
            if self.valid_ship_placement(ship_data):
                self.board.place_ship(ship_id, ship_data)
                ship_lengths.remove(ship_data['length'])
                ship_id += 1
            else:
                print("Invalid move. Try again.")

    def valid_ship_placement(self, ship_data):
        # TODO add ship placement validation
        return True

    def get_move(self):
        move = input("Player {}, enter your next move".format(self.player_id))
        return move

    def get_locations(self, ship_lengths):
        print("Remaining ships: ", *ship_lengths)
        loc_strings = input("Player {} location:\n".format(self.player_id))
        x, y = (int(n) for n in loc_strings.split())  # TODO sanitize input here
        direction = input("Direction:\n")
        length = int(input("Length:\n"))
        return {'location': (y, x),
                'direction': direction,
                'length': length}


class Board():
    def __init__(self, size, player_id):
        self.player_id = player_id
        row = [0 for _ in range(size)]
        self.matrix = [list(row) for _ in range(size)]
        self.ships = {}

    def render(self):
        for row in self.matrix:
            print(row)

    def place_ship(self, ship_id, ship_data):
        '''Ship data format: {'location': (<y>, <x>), 'direction': <'v' or 'h'>,
        'length': <int>'''
        self.ships[ship_id] = ship_data
        y, x = ship_data['location']
        for _ in range(ship_data['length']):
            self.matrix[y][x] = ship_id
            if ship_data['direction'] == 'v':
                y += 1
            else:
                x += 1


def main():
    game = Game()
    game.run()


if __name__ == '__main__':
    main()
