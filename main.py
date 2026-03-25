from game.board import Board
from agent.random_agent import get_random_move
from agent.base_agent import minimax

def main():
    board = Board()
    game_over = False
    turn = 0

    while not game_over:
        board.display()
        piece = 1 if turn % 2 == 0 else 2
        try:
            if piece == 1:
                col = int(input(f"Joueur {piece}, choisis une colonne (0-{board.cols-1}): "))
            else:
                #col = get_random_move(board)
                col, _ = minimax(board, 3, True)
                print(f"IA joue sur la colonne {col}")    
            if 0 <= col < board.cols:
                if board.is_valid_move(col):
                    board.drop_piece(col, piece)
                    if board.check_winner(piece):
                        board.display()
                        print(f"🎉 Joueur {piece} a gagné !")
                        game_over = True
                    else:
                        turn += 1
                else:
                    print("Colonne pleine, regarde avant de jouer pfffff.")
            else:
                print("Colonne invalide, t'as cru que le plateau était infini ???.")
        except ValueError:
            print("N'essaie plus jamais autre chose qu'un NOMBRE.")



if __name__ == "__main__":
    main()