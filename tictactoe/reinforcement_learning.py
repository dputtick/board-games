import numpy as np
import tictactoe as t
from random import random
from bisect import bisect_left


def board_converter(board_input):
    '''converts a board with 'X' and 'O' to a ndarray
    with 1 and -1'''
    board_output = np.array([1 if location == 'X'
                    else -1 if location == 'O'
                    else 0 for location in board_input[1:]])
    return np.reshape(board_output, (3, -1)) #convert 1x9 array to 3x3


def ai_or_network_move(player, board, piece, prob_table):
    '''Returns a move from the rule-based AI or the
    reinforcement learning algorithm.'''
    if player == 'AI':
        return t.computer_move(board, piece)
    elif player == 'RL':
        return move_generator(board, piece, prob_table)


def move_generator(board, piece, prob_table):
    '''Looks up probability matrix and returns a move choice based on
    the weightings from the matrix'''
    board = board_converter(board)
    probability_matrix = probability_lookup(board, prob_table)
    return weighted_random_choice(probability_matrix)


def weighted_random_choice(probability_matrix):
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
    random_index = bisect_left(cumweights, random_point)
    return values[random_index]


def probability_lookup(board, prob_table):
    '''Takes a board and the global probability table, checks
    whether the board is in the table, and returns the appropriate
    probability matrix'''
    if str(board) not in prob_table:
        prob_table[str(board)] = base_probability_matrix_generator(board)
    return prob_table[str(board)]


def base_probability_matrix_generator(converted_binary_board):
    '''replaces all 0 (empty) spaces with an evenly weighted probability,
    replaces all other spaces with a 0 probability'''
    non_zero_count = np.count_nonzero(converted_binary_board)
    empty_space_count = converted_binary_board.size - non_zero_count
    base_probability = 1 / empty_space_count
    probability_matrix = np.zeros_like(converted_binary_board, dtype=float)
    np.place(probability_matrix, converted_binary_board == 0, base_probability)
    return probability_matrix


def update_probabilities(move_history, prob_table, player=None):
    '''Returns an updated probability table from a given probability
    table and a move history for a game. If player == None, the game
    was a draw.'''
    if player == None:
        update_function = 'Mild'
    elif player == 'RL':
        update_function = 'Strong'
    elif player == 'AI':
        update_function = 'Negative'
    return update_table(move_history, prob_table, update_function)


def update_table(move_history, prob_table, update_function):
    '''Updates a probability table using the passed-in update function.'''
    update_function_dict = {'Mild': 1.1, 'Strong': 5.0, 'Negative': .75}
    multiplication_factor = update_function_dict[update_function]
    for board, move in reversed(move_history):
        move_index = move - 1
        old_prob_matrix = prob_table[str(board)]
        flattened_prob_matrix = np.reshape(old_prob_matrix, (1, -1))
        old_move_probability = flattened_prob_matrix[0][move_index]
        new_move_prob = old_move_probability * multiplication_factor
        flattened_prob_matrix[0][move_index] = new_move_prob
        prob_table[str(board)] = np.reshape(flattened_prob_matrix, (3, 3))
    return prob_table


def game_loop(player, prob_table, win_counter):
    piece_dict = {'AI': 'X', 'RL': 'O'}
    invert_dict = {'AI': 'RL', 'RL': 'AI'}
    move_history = []
    board = t.empty_board()
    winner = False
    while True:
            piece = piece_dict[player]
            move = ai_or_network_move(player, board, piece, prob_table)
            if player == 'RL':
                move_history.append((board_converter(board), move))
            board = t.update_board(board, move, piece)
            if t.check_victory(board, piece):
                prob_table = update_probabilities(move_history, 
                                                prob_table, player)
                winner = player
                break
            elif 0 not in board_converter(board):
                prob_table = update_probabilities(move_history, 
                                                        prob_table)
                break
            else:
                player = invert_dict[player]
    if winner:
        win_counter[winner] += 1
    return prob_table, win_counter


def run_game(prob_table, runs):
    win_counter = {'AI': 0, 'RL': 0}
    run_results = []
    for run in range(runs):
        if run % 2 == 0:
            player = 'AI'
        else:
            player = 'RL'
        prob_table, win_counter = game_loop(player, prob_table, win_counter)
        if run > 0 and run % 1000 == 0:
            run_results.append((run, win_counter.copy()))
    return prob_table, win_counter, run_results


def main():
    prob_table = {}
    prob_table, win_counter, run_results = run_game(prob_table, 1001)
    for item in run_results:
        print(item)
    return prob_table


if __name__ == '__main__':
    main()
