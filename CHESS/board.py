import sys

class Piece:
    def __init__(self, is_white):
        self.is_white = is_white

    def is_white(self):
        return self.is_white

    def get_symbol(self):
        pass

class Rook(Piece):
    def get_symbol(self):
        return "R"

class Knight(Piece):
    def get_symbol(self):
        return "N"

class Bishop(Piece):
    def get_symbol(self):
        return "B"

class Queen(Piece):
    def get_symbol(self):
        return "Q"

class King(Piece):
    def get_symbol(self):
        return "K"

class Pawn(Piece):
    def get_symbol(self):
        return "P"

class Spot:
    def __init__(self, row, col, piece):
        self.row = row
        self.col = col
        self.piece = piece

    def get_piece(self):
        return self.piece

class Board:
    def __init__(self):
        self.boxes = [[None for _ in range(8)] for _ in range(8)]
        self.reset_board()

    def get_spot(self, row, col):
        if row < 0 or row >= 8 or col < 0 or col >= 8:
            print("Error: Index out of bounds", file=sys.stderr)
            return None
        return self.boxes[row][col]

    def reset_board(self):
        # Initialize white pieces
        self.boxes[0][0] = Spot(0, 0, Rook(True))
        self.boxes[0][1] = Spot(0, 1, Knight(True))
        self.boxes[0][2] = Spot(0, 2, Bishop(True))
        self.boxes[0][3] = Spot(0, 3, Queen(True))
        self.boxes[0][4] = Spot(0, 4, King(True))
        self.boxes[0][5] = Spot(0, 5, Bishop(True))
        self.boxes[0][6] = Spot(0, 6, Knight(True))
        self.boxes[0][7] = Spot(0, 7, Rook(True))
        for i in range(8):
            self.boxes[1][i] = Spot(1, i, Pawn(True))

        # Initialize black pieces
        self.boxes[7][0] = Spot(7, 0, Rook(False))
        self.boxes[7][1] = Spot(7, 1, Knight(False))
        self.boxes[7][2] = Spot(7, 2, Bishop(False))
        self.boxes[7][3] = Spot(7, 3, Queen(False))
        self.boxes[7][4] = Spot(7, 4, King(False))
        self.boxes[7][5] = Spot(7, 5, Bishop(False))
        self.boxes[7][6] = Spot(7, 6, Knight(False))
        self.boxes[7][7] = Spot(7, 7, Rook(False))
        for i in range(8):
            self.boxes[6][i] = Spot(6, i, Pawn(False))

        # Initialize remaining boxes without any piece
        for i in range(2, 6):
            for j in range(8):
                self.boxes[i][j] = Spot(i, j, None)

    def display_board(self):
        print(" " * 12, end="")
        for ch in range(ord('a'), ord('i')):
            print(f"{chr(ch):^12}", end="")
        print()

        for i in range(8):
            print(f"{8-i:^12}", end="")
            for j in range(8):
                spot = self.get_spot(i, j)
                if spot.get_piece():
                    symbol = ""
                    if spot.get_piece().is_white:
                        symbol = "WHITE" + spot.get_piece().get_symbol()
                    else:
                        symbol = "BLACK" + spot.get_piece().get_symbol()
                    print(f"{symbol:^12}", end="")
                else:
                    print(f"{'.:^12'}", end="")
            print(f"{8-i:^12}")

        print(" " * 12, end="")
        for ch in range(ord('a'), ord('i')):
            print(f"{chr(ch):^12}", end="")
        print("\n")