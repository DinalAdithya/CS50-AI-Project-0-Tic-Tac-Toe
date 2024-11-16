"""
Tic Tac Toe Player
"""
import math
from copy import deepcopy

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
    x_count = 0
    o_count = 0

    for row in board:
        x_count += row.count(X)
        o_count += row.count(O)
    print(f"Debug: X count = {x_count}, O count = {o_count}")
    if x_count == o_count:
        print("Debug: It's X's turn.")
        return X
    else:
        print("Debug: It's O's turn.")
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available_actions = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is EMPTY:
                available_actions.add((i, j))

    return available_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    i, j = action
    if board[i][j] is not EMPTY:
        raise ValueError("Invalid action")

    copy_board = deepcopy(board)
    copy_board[i][j] = player(board)

    return copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # for rows
    for row in board:
        if row[0] is not EMPTY and row[0] == row[1] == row[2]:
            return row[0]

    # for columns
    for columns in range(3):
        if board[0][columns] is not EMPTY and board[0][columns] == board[1][columns] == board[2][columns]:
            return board[0][columns]

    # diagonals
    if board[0][0] is not EMPTY and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] is not EMPTY and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not EMPTY or not actions(board)

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None, utility(board)
        #print(f"Terminal board reached with utility: {result[1]}")

    best_move = None

    if player(board) == X:

        v = -float('inf')

        for action in actions(board):
            _, value = minimax(result(board, action))
            if value is EMPTY:
                #print(f"Debug: value is None for action {action} on board {board}")
                value = -float('inf')
            if value > v:
                v = value
                best_move = action
        #return best_move, v
    else:

        v = float('inf')

        for action in actions(board):
            _, value = minimax(result(board, action))
            if value is EMPTY:
                #print(f"Debug: value is None for action {action} on board {board}")
                value = float('inf')
            if value < v:
                v = value
                best_move = action

    return best_move, v
