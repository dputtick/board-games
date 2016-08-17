class Game():
    def __init__(self):
        # objects we need: board object
        # methods we need: moves, checking for 
        pass


    def game_loop(self):
        # should I use async here? or threading? that could be cool
        pass

# game object is a dispatcher
    # gives and takes information from players and board

# player object
    # get user input
    # UI / client
    # input validation
    # sends input to game object

# board
    # stores the state of the game
    # gives information to the game object about events


# list of game events
    # let the player choose where their ships are
    # taking turns - logic for alternating
    # guessing a specific location
    # checking for hits
    # checking for sunken ships
    # checking for win conditions



class Board():
    def __init__(self, size):
        row = [0 for _ in range(size)]
        self._matrix = [list(row) for _ in range(size)]


    def render(self):
        for row in self.matrix:
            print(row)


def main():
    board_size = 4
    board = Board(board_size)
    board.render()


if __name__ == '__main__':
    main()


# if I try to run this at module level, I get "can't find '__main__' module in 'battleship/'"
# how do I make this work?

# how do I merge in only my changes to battleship and leave curses stuff as is? Can I merge only specific sections?