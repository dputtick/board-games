import numpy as np
import tictactoe as t
from random import random


def board_converter(board_input):
    '''converts a board with 'X' and 'O' to a ndarray
    with 1 and -1'''
    board_output = np.array([1 if location == 'X'
                    else -1 if location == 'O'
                    else 0 for location in board_input[1:]])
    return np.reshape(board_output, (3, -1)) #convert 1x9 array to 3x3


def base_probability_matrix_generator(converted_binary_board):
    '''replaces all 0 (empty) spaces with an evenly weighted probability,
    replaces all other spaces with a 0 probability'''
    non_zero_count = np.count_nonzero(converted_binary_board)
    empty_space_count = converted_binary_board.size - non_zero_count
    base_probability = 1 / empty_space_count
    probability_matrix = np.zeros_like(converted_binary_board, dtype=float)
    np.place(probability_matrix, converted_binary_board == 0, base_probability)
    return probability_matrix


def move_generator(board, piece, probability_table):
    '''Looks up probability matrix and returns a move choice based on
    the weightings from the matrix'''
    board = board_converter(board)
    probability_matrix = probability_lookup(board, probability_table)
    return random_choice(probability_matrix)


def random_choice(probability_matrix):
    '''Takes given probability matrix and returns a weighted
    random choice of board spaces [1 - 9]'''
    weights = np.reshape(probability_matrix, (1, -1))
    values = np.arange(1, 10)
    cumweights = []
    weight_sum = 0
    for weight in weights[0]:
        weight_sum += weight
        cumweights.append(weight_sum)
    random_point = random() * weight_sum
    random_index = np.searchsorted(weights, random_point)
    return values[random_index]


def probability_lookup(board, probability_table):
    '''Takes a board and the global probability table, checks
    whether the board is in the table, and returns the appropriate
    probability matrix'''
    if board not in probability_table:
        probability_table[board] = base_probability_matrix_generator(board)
    return probability_table[board]


def update_probabilities(move_history, probability_table, player=None):
    '''Returns an updated probability table from a given probability
    table and a move history for a game. If player == None, the game
    was a draw.'''
    if player == 'None':
        update_function = 'Mild'
    elif player == 'RL':
        update_function = 'Strong'
    elif player == 'AI':
        update_function = 'Negative'
    return update_table(move_history, probability_table, update_function)

def update_table(move_history, probability_table, update_function):
    '''Updates a probability table using the passed-in update function.'''
    update_function_dict = {'Mild': 1.1, 'Strong': 1.25, 'Negative': .75}
    multiplication_factor = update_function_dict[update_function]
    for board in reversed(move_history):
        probability_table[board] = probability_table[board]*multiplication_factor
    return probability_table


def ai_or_network_move(player, board, piece, probability_table):
    '''Returns a move from the rule-based AI or the
    reinforcement learning algorithm.'''
    if player == 'AI':
        return t.computer_move(board, piece)
    elif player == 'RL':
        return move_generator(board, piece, probability_table)


def run_game(first_mover, probability_table, runs):
    board = t.empty_board()
    move_history = [board_converter(board)]
    player_dict = {'AI': 'X', 'RL': 'O'}
    invert_dict = {'AI': 'RL', 'RL': 'AI'}
    win_counter = {'AI': 0, 'RL': 0}
    for run in range(runs):
        if run % 2 == 0:
            player = 'AI'
        else:
            player = 'RL'
        while True:
            piece = player_dict[player]
            move = ai_or_network_move(player, board, piece, probability_table)
            board = t.update_board(board, move, piece)
            if player == 'RL':
                move_history.append(board_converter(board))
            if t.check_victory(board, piece):
                probability_table = update_probabilities(move_history, 
                                                probability_table, player)
                win_counter[player] = win_counter[player] + 1
                break
            elif 0 not in board_converter(board):
                probability_table = update_probabilities(move_history, 
                                                        probability_table)
                break
            else:
                player = invert_dict[player]
    return probability_table


def main():
    probability_table = {}
    probability_table, win_counter = run_game('AI', probability_table, 10000)
    print(win_counter)
    #boards for tests
    empty_board = [None, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    partial_board = [None, 1, 2, 'X', 4, 'O', 6, 7, 8, 9]
    board_output_prototype = np.array([[0, 0, 1],
                                  [0, -1, 0],
                                  [0, 0, 0]])



if __name__ == '__main__':
    main()
