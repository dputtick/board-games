class Game():
    def __init__(self):
        # create board (maybe prompt for size)
        self.players = []
        self.boards = {}
        for playerid in [1]:
            self.players.append(Player(playerid))
            self.boards[playerid] = Board(4, playerid)

    def run(self):
        self.setup_phase()
        self.board.render()

    def setup_phase(self):
        for player in self.players:
            board = boards[player.playerid]
            ship_lengths = [2]
            ship_id = 1
            while ship_lengths:
                ship_data = player.get_locations(ship_lengths)
                if self.valid_ship(ship_data):
                    self.board.place_ship(ship_id, ship_data)
                    ship_lengths.remove(ship_data['length'])
                else:
                    print("Invalid move. Try again.")

    def valid_ship(self, ship_data):
        return True

    def game_loop(self):
        pass


class Player():
    def __init__(self, playerid):
        self.human = True
        self.playerid = playerid

    def get_move(self):
        move = input("Player {}, enter your next move".format(self.playerid))
        return move

    def get_locations(self, ship_lengths):
        print("Remaining ships: ", *ship_lengths)
        loc_strings = input("Player {} location:\n".format(self.playerid))
        x, y = (int(n) for n in loc_strings.split()) # TODO sanitize input here
        direction = input("Direction:\n")
        length = int(input("Length:\n"))
        return {'location': (y, x),
                'direction': direction,
                'length': length}
                

class Board():
    def __init__(self, size, player):
        self.player = player
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
