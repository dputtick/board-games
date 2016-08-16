class Game():
    def __init__(self):
        # objects we need: board object
        # methods we need: moves, checking for 
        pass


    def game_loop(self):
        # should I use async here? or threading? that could be cool
        pass


    class Board():
        def __init__(self):
            row = ['*' for _ in range(10)]
            self.matrix = [list(row) for _ in range(10)]
            # is there a better solution here than list(row)?
            self.matrix[0][0] = 1
            print(self.matrix)
            # is this the best way to make a matrix efficiently?
            # should I use an @property here for the board?



def main():
    board = Game.Board()


if __name__ == '__main__':
    main()


# if I try to run this at module level, I get "can't find '__main__' module in 'battleship/'"
# how do I make this work?