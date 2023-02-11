"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    empty_count = 0

    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                empty_count +=1

    if empty_count % 2 == 0:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions_set.add((i,j))

    return actions_set



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    board_copy = deepcopy(board)

    if board[i][j] == EMPTY:
        board_copy[i][j] = player(board)
        return board_copy

    raise ValueError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    count_X = 0
    count_O = 0
    # horizontal
    for i in range(3):
        count_X = 0
        count_O = 0
        for j in range(3):
            if board[i][j] == X:
                count_X += 1
            elif board[i][j] == O:
                count_O += 1
        if count_X == 3:
            return X
        elif count_O == 3:
            return O
    count_X = 0
    count_O = 0
    # Vertical
    for i in range(3):
        count_X = 0
        count_O = 0
        for j in range(3):
            if board[j][i] == X:
                count_X += 1
            elif board[j][i] == O:
                count_O += 1
        if count_X == 3:
            return X
        elif count_O == 3:
            return O
    count_X = 0
    count_O = 0
    #diagnal 1
    for i in range(3):
        if board[i][i] == X:
            count_X += 1
        elif board[i][i] == O:
            count_O += 1
        if count_X == 3:
            return X
        elif count_O == 3:
            return O
    count_X = 0
    count_O = 0
    #diagnal 2
    j = 0
    for i in range(2,-1,-1):
        if board[i][j] == X:
            count_X += 1
        elif board[i][j] == O:
            count_O += 1
        j += 1
        if count_X == 3:
            return X
        elif count_O == 3:
            return O

    raise None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    TODO: check if winner?
    """

    #check if there is a winner
    if winner(board) != None:
        return True

    #checks if board has an empty cell
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False

    

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    result = winner(board)

    if result == X:
        return 1
    elif result == O:
        return -1
    
    return 0
    #raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    
    should try to give it the best action

    """
    if terminal(board):
        return None

    for action in actions(board):
        result_min = minmax(result(board,action))
        if result_min == 1:
            return action


    raise NotImplementedError
