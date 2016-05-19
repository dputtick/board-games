import unittest
import reinforcement_learning as rl
import tictactoe as t
import numpy as np


class tlTests(unittest.TestCase):

    def setUp(self):
        self.empty_binary_board = np.zeros((3,3))
        self.probability_matrix = rl.base_probability_matrix_generator(
            self.empty_binary_board)


    def test_weighted_random_choice(self):
        choice = rl.weighted_random_choice(self.probability_matrix)
        self.assertTrue(choice)

    def test_probability_matrix_generator(self):
        self.matrix = rl.base_probability_matrix_generator(
            self.empty_binary_board)
        print(self.matrix)


if __name__ == '__main__':
    unittest.main()



    # empty_board = [None, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # partial_board = [None, 1, 2, 'X', 4, 'O', 6, 7, 8, 9]
    # board_output_prototype = np.array([[0, 0, 1],
    #                               [0, -1, 0],
    #                               [0, 0, 0]])