class Board:
    def __init__(self):
        self.rows = 6
        self.cols = 7
        self.grid = [[0 for k in range(self.cols)] for k in range(self.rows)]

    def display(self):
        print("\nPlateau :")
        for row in self.grid:
            print(" | ".join(str(cell) for cell in row))
        indication = [0,1,2,3,4,5,6]
        print("-" * 25)
        print(" | ".join(str(elem) for elem in indication))
        print("-" * 25)

    def is_valid_move(self, col):
        return self.grid[0][col] == 0

    def get_next_open_row(self, col):
        for row in reversed(range(self.rows)):
            if self.grid[row][col] == 0:
                return row
        return None

    def copy(self):
        new_board = Board()
        new_board.grid = [row[:] for row in self.grid]
        return new_board

    def drop_piece(self, col, piece):
        row = self.get_next_open_row(col)
        if row is not None:
            self.grid[row][col] = piece
            
    def check_winner(self, piece):
        # Vérifier horizontale
        for r in range(self.rows):
            for c in range(self.cols - 3):
                if all(self.grid[r][c+i] == piece for i in range(4)):
                    return True

        # Vérifier verticale
        for r in range(self.rows - 3):
            for c in range(self.cols):
                if all(self.grid[r+i][c] == piece for i in range(4)):
                    return True

        # Vérifier diagonale \
        for r in range(self.rows - 3):
            for c in range(self.cols - 3):
                if all(self.grid[r+i][c+i] == piece for i in range(4)):
                    return True

        # Vérifier diagonale /
        for r in range(3, self.rows):
            for c in range(self.cols - 3):
                if all(self.grid[r-i][c+i] == piece for i in range(4)):
                    return True

        return False

    