import random

def get_random_move(board):
    valid_moves = []
    for col in range(board.cols):
        if board.is_valid_move(col):
            valid_moves.append(col)
    return random.choice(valid_moves)
