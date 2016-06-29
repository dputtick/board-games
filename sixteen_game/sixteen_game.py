import random
import time
import curses

'''Write a function that mimics the Python print function using curses since all
of my interaction with the user is via print and input statements.
This means I need some sort a screen displayer function, and then a 
Insert the appropriate .refreshes and .clears for desired functionality
Adjust move_getter to abstract out the appropriate key functionality
Write a function that takes the possible arrow keys, waits for them, 
and returns the chosen one'''


def board_printer(stdscr, board_matrix):
    '''Prints a visual representation of the board.'''
    stdscr.clear()
    y_coord = 0
    for row in board_matrix:
        row_str = ''.join([str(num).rjust(2) for num in row])
        stdscr.addstr(y_coord, 0, row_str)
        y_coord += 1


def get_input(stdscr, prompt):
    stdscr.clear()
    stdscr.addstr(prompt)
    return stdscr.getkey()


def print_text(stdscr, string):
    stdscr.clear()
    stdscr.addstr(string)


def move_getter(board_matrix):
    '''Inputs a move from the player and returns the new board.'''
    while True:
        move = input("Enter the piece number you want to move:\n")
        try:
            move = int(move)
        except ValueError:
            print("That's not a number. Try again!")
            continue
        empty_spot_row, empty_spot_index = location_finder(board_matrix, " ")
        move_row, move_index = location_finder(board_matrix, move)
        if (move_row, move_index) == (None, None):
            print("That's not a legal move. Try again!")
            continue
        legal_moves = [(empty_spot_row - 1, empty_spot_index),
                        (empty_spot_row + 1, empty_spot_index),
                        (empty_spot_row, empty_spot_index - 1),
                        (empty_spot_row, empty_spot_index + 1)]
        if (move_row, move_index) not in legal_moves:
            print("You can't move that piece. Try again!")
            continue
        board_matrix[empty_spot_row][empty_spot_index] = move
        board_matrix[move_row][move_index] = ' '
        return board_matrix


def choose_board_size(stdscr):
    '''Returns the player's choice of square board's side length.'''
    stdscr.clear
    stdscr.echo()
    while True:
        size_prompt = "How long do you want the board's sides to be?"
        board_size = get_input(stdscr, size_prompt)
        try:
            return int(board_size)
        except ValueError:
            print_text(stdscr, "Oops. Please enter an integer (3-9).")


def setup(stdscr):
    '''Called by main(), performs initial setup of the game state'''
    curses.use_default_colors()
    board_size = choose_board_size(stdscr)
    solution_board_list = list(range(1, (board_size ** 2))) + [' ']
    solution_board_matrix = list_to_matrix(solution_board_list, board_size)
    shuffled_board_list = list(solution_board_list)
    random.shuffle(shuffled_board_list)
    while not is_valid_board(shuffled_board_list, board_size):
        random.shuffle(shuffled_board_list)
    board_matrix = list_to_matrix(shuffled_board_list, board_size)
    return shuffled_board_list, board_matrix, solution_board_matrix


def location_finder(board_matrix, item):
    '''Finds the position (row, index) in board_matrix of item,
    returns (None, None) if item not in board_matrix.'''
    item_location = (None, None)
    for index, row in enumerate(board_matrix):
        if item in row:
            item_location = (index, row.index(item))
    return item_location


def list_to_matrix(board_list, board_size):
    '''Converts a board represented as a list
    to a board represented by a matrix with a side length of board_size.'''
    return [board_list[i:i + board_size]
            for i in range(0, len(board_list), board_size)]


def game_finished_checker(board_matrix, solution_board_matrix):
    '''Checks whether the puzzle has been completed.'''
    return board_matrix == solution_board_matrix


def count_inversions(board_list):
    '''Counts the number of inversions (number out of numerical sequence)
    in board_list.'''
    inversions = 0
    board_no_spaces = [num for num in board_list if num != ' ']
    for index, number in enumerate(board_no_spaces):
        for compare_number in board_no_spaces[index + 1:]:
            if compare_number < number:
                inversions += 1
    return inversions


def is_even_num(number):
    '''Returns true if number is even, else returns False.'''
    return number % 2 == 0


def is_valid_board(board_list, board_size):
    '''Checks if board_list represents a solvable board,
    returns True if it does.'''
    inversions = count_inversions(board_list)
    board_matrix = list_to_matrix(board_list, board_size)
    empty_space_row, index = location_finder(board_matrix, ' ')
    if is_even_num(board_size):
        if is_even_num(inversions):
            if not is_even_num(empty_space_row):
                return True
        elif not is_even_num(inversions):
            if is_even_num(empty_space_row):
                return True
    elif not is_even_num(board_size):
        if is_even_num(inversions):
            return True
    return False


def main(stdscr):
    board_list, board_matrix, solution_board_matrix = setup(stdscr)
    start_time = time.time()
    while True:
        board_printer(stdscr, board_matrix)
        board_matrix = move_getter(board_matrix)
        if game_finished_checker(board_matrix, solution_board_matrix):
            total_time = round(time.time() - start_time)
            print("Congrats - you finished the puzzle!")
            print("You took {} seconds".format(str(total_time)))
            board_printer(board_matrix)
            break


if __name__ == '__main__':
    curses.wrapper(main)
