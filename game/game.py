from game.board import Board

class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.current_player_index = 0
        self.game_over = False

    def switch_player(self):
        if self.current_player_index == 0 :
            self.current_player_index = 1
        else : 
            self.current_player_index = 0

    def play(self):
        # while not self.game_over:
            self.board.display()
            current_player = self.players[self.current_player_index]
            
            col = current_player.get_action(self.board)

            if self.board.is_valid_move(col):
                self.board.drop_piece(col, self.current_player_index + 1)

                if self.board.check_victory(self.current_player_index + 1):
                    self.board.display()
                    print(f"Player {self.current_player_index + 1} wins!")
                    self.game_over = True
                else:
                    self.switch_player()