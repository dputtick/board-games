import unittest
import reinforcement_learning as rl
import tictactoe as t
import numpy as np


class RlTests(unittest.TestCase):

    def setUp(self):
        self.empty_binary_board = np.zeros((3,3))
        self.probability_matrix = rl.base_probability_matrix_generator(
            self.empty_binary_board)


    def test_weighted_random_choice(self):
        choice = rl.weighted_random_choice(self.probability_matrix)
        self.assertTrue(choice)


if __name__ == '__main__':
    unittest.main()