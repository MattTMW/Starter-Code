from utilities import generate_piece, print_board

DEV_MODE = False


def move_left(game_board):
    for row in game_board:
        # remove 0s and append to end
        no_zeros = [cell for cell in row if cell != 0]
        num_of_zeros = len(row) - len(no_zeros)
        row[:] = no_zeros + [0] * num_of_zeros

        # combine adjacent equal elements
        for i in range(1, len(row)):
            if row[i] == row[i - 1]:
                row[i - 1] *= 2
                row[i] = 0

        # remove zeros and combine to end
        no_zeros = [cell for cell in row if cell != 0]
        num_of_zeros = len(row) - len(no_zeros)
        row[:] = no_zeros + [0] * num_of_zeros


def move_right(game_board):
    for row in game_board:

        no_zeros = [cell for cell in row if cell != 0]
        num_of_zeros = len(row) - len(no_zeros)
        row[:] = [0] * num_of_zeros + no_zeros  # zeros appended to beginning

        for i in range(len(row) - 1, 0, -1):
            if row[i] == row[i - 1]:
                row[i] *= 2
                row[i - 1] = 0

        no_zeros = [cell for cell in row if cell != 0]
        num_of_zeros = len(row) - len(no_zeros)
        row[:] = [0] * num_of_zeros + no_zeros


def move_down(game_board):
    for col_idx in range(len(game_board[0])):
        column = [game_board[row_idx][col_idx] for row_idx in range(len(game_board))]

        no_zeros = [cell for cell in column if cell != 0]
        num_of_zeros = len(column) - len(no_zeros)
        column[:] = [0] * num_of_zeros + no_zeros  # zeros appended to beginning

        for i in range(len(column) - 1, 0, -1):
            if column[i] == column[i - 1]:
                column[i] *= 2
                column[i - 1] = 0

        num_of_zeros = [cell for cell in column if cell != 0]
        num_zeros = len(column) - len(num_of_zeros)
        column[:] = [0] * num_zeros + num_of_zeros

        for row_idx in range(len(game_board)):
            game_board[row_idx][col_idx] = column[row_idx]


def move_up(game_board):
    for col_idx in range(len(game_board[0])):
        column = [game_board[row_idx][col_idx] for row_idx in range(len(game_board))]

        no_zeros = [cell for cell in column if cell != 0]
        num_of_zeros = len(column) - len(no_zeros)
        column[:] = no_zeros + [0] * num_of_zeros  # zeros appended to end

        for i in range(1, len(column)):
            if column[i] == column[i - 1]:
                column[i - 1] *= 2
                column[i] = 0

        no_zeros = [cell for cell in column if cell != 0]
        num_of_zeros = len(column) - len(no_zeros)
        column[:] = no_zeros + [0] * num_of_zeros

        for row_idx in range(len(game_board)):
            game_board[row_idx][col_idx] = column[row_idx]


def user_movements(move, game_board):
    if move == 'w':
        move_up(game_board)
    if move == 'a':
        move_left(game_board)
    if move == 's':
        move_down(game_board)
    if move == 'd':
        move_right(game_board)
    if move == 'q':
        return


def validate_user_move(move):
    if move in ['w', 'a', 's', 'd', 'q']:
        return True
    else:
        return False


def is_board_full(game_board: [[int, ], ]) -> bool:
    """
    Check if the game board is full (no empty cells).

    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: True if the board is full, False otherwise
    """
    for row in game_board:
        for cell in row:
            if cell == 0:  # Found an empty cell
                return False
    return True  # No empty cells found, board is full


def main(game_board: [[int, ], ]) -> [[int, ], ]:
    """
    2048 main function, runs a game of 2048 in the console.

    Uses the following keys:
    w - shift up
    a - shift left
    s - shift down
    d - shift right
    q - ends the game and returns control of the console
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: returns the ending game board
    """
    # Initialize board's first cell
    initialize_piece = generate_piece(game_board)
    # TODO: generate a random piece and location using the generate_piece function
    new_piece = generate_piece(game_board)
    # TODO: place the piece at the specified location
    game_board[new_piece['row']][new_piece['column']] = new_piece['value']
    game_board[initialize_piece['row']][initialize_piece['column']] = initialize_piece['value']

    # Game Loop
    while not game_over(game_board):
        # otherwise... game continues
        print_board(game_board)
        # move the piece
        # user_input = whatever
        user_input = input()  # USER INPUTS MOVE
        if user_input == 'q':
            print('Goodbye')
            break
        # validate user input
        validate_user_move(user_input)
        # if not validate_user_input(user_input):
        if not validate_user_move(user_input):
            continue

        # uyser iunput is valid
        user_movements(user_input, game_board)
        # generate piece:  new_piece = generate_piece(game_board)
        new_piece = generate_piece(game_board)
        game_board[new_piece['row']][new_piece['column']] = new_piece['value']
        # move the piece

        # update the peices

        # check if win (2048)
        if win_con(game_board) == True:
            break

    # TODO: UPDATE/ADD PIECE TO BOARD

    # place a random piece on the board
    # game_board[new_piece['row']][new_piece['column']] = new_piece['value']

    # TODO: Show updated board using the print_board function
    # TODO: GET AND EXECUTE USER MOVE
    # if valid_user_move():

    # Take input until the user's move is a valid key
    # if the user quits the game, print Goodbye and stop the Game Loop
    # User's Move Loop:
    # Execute the user's move
    # Compare board before user's move & after user's move
    # get and execute another move if board has not changed

    # Check if the user wins
    return game_board


def win_con(game_board):
    for row in range(4):
        for col in range(4):
            current = game_board[row][col]
            if current == 2048:
                return True


def check(game_board):
    for row in range(3):
        for col in range(3):
            current = game_board[row][col]
            if current == game_board[row][col + 1]:
                return True
            if current == game_board[row + 1][col]:
                return True
    return False


def game_over(game_board: [[int, ], ]) -> bool:
    """
    Query the provided board's game state.

    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: Boolean indicating if the game is over (True) or not (False)
    """
    # TODO: Loop over the board and determine if the game is over

    if is_board_full(game_board) and not check(game_board):
        return True
    else:
        return False  # TODO: Don't always return false


if __name__ == "__main__":
    main([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]])


