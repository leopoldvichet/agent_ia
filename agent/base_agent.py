import random
import math

def get_valid_moves(board):
    valid_moves = []
    for col in range(board.cols):
        if board.is_valid_move(col):
            valid_moves.append(col)
    return valid_moves

def is_terminal(board):
    return(board.check_winner(1) or board.check_winner(2) or len(get_valid_moves(board)) == 0)

def evaluate(board):
    if board.check_winner(2):
        return 100
    elif board.check_winner(1):
        return -100
    else:
        score = 0
        for row in board.grid:
            score += row.count(2)
            score -= row.count(1)
        return score


def minimax(board, depth, maximizing_player):
    valid_moves = get_valid_moves(board)

    # Cas terminal
    if depth == 0 or is_terminal(board):
        return None, evaluate(board)

    if maximizing_player:
        value = -math.inf
        best_col = random.choice(valid_moves)

        for col in valid_moves:
            temp_board = board.copy()
            temp_board.drop_piece(col, 2)

            new_score = minimax(temp_board, depth - 1, False)[1]

            if new_score > value:
                value = new_score
                best_col = col

        return best_col, value

    else:
        value = math.inf
        best_col = random.choice(valid_moves)

        for col in valid_moves:
            temp_board = board.copy()
            temp_board.drop_piece(col, 1)

            new_score = minimax(temp_board, depth - 1, True)[1]

            if new_score < value:
                value = new_score
                best_col = col

        return best_col, value