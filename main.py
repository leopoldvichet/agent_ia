from game.board import Board

def main():
    board = Board()
    game_over = False
    turn = 0

    while not game_over:
        board.display()
        piece = 1 if turn % 2 == 0 else 2
        try:
            col = int(input(f"Joueur {piece}, choisis une colonne (0-{board.cols-1}): "))
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
                    print("Colonne pleine, choisis une autre.")
            else:
                print("Colonne invalide, choisis entre 0 et 6.")
        except ValueError:
            print("Entrée invalide, mets un nombre.")



if __name__ == "__main__":
    main()