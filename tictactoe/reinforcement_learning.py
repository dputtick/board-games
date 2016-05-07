#boards for testing
empty_board = [None, 1, 2, 3, 4, 5, 6, 7, 8, 9]
partial_board = [None, 1, 2, 'X', 4, 'O', 6, 7, 8, 9]



def board_converter(board_input):
    board_output = list()
    for location in board_input[1:]:
        if location == 'X':
            board_output.append((True, False))
        if location == 'O':
            board_output.append((False, True))
        else:
            board_output.append((False, False))
    return board_output

                #  X      Y
board_output = [(False, False),
                (False, False),
                (True, False),
                (False, False),
                (False, True),
                (False, False),
                (False, False),
                (False, False),
                (False, False),]


def neuron(board_output):
    count = 0
    probability_matrix = list()
    for pair in board_output:
        if pair == (False, False):
            count += 1
            probability_matrix.append(True)
        else:
            probability_matrix.append(False)
    base_probability = 1 / count
    output_matrix = list()
    for item in probability_matrix:
        if item == True:
            output_matrix.append(base_probability)
        if item == False:
            output_matrix.append(0)
    return output_matrix

print(neuron(board_output))