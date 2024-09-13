from piece import Piece

class King(Piece):
    def __init__(self, is_white):
        super().__init__(is_white)
        self.castling_done = False

    def is_castling_done(self):
        return self.castling_done

    def set_castling_done(self, castling_done):
        self.castling_done = castling_done

    def can_move(self, board, start, end):
        if end.piece and end.piece.is_white == self.is_white:
            return False

        x = abs(start.x - end.x)
        y = abs(start.y - end.y)
        if x + y == 1:
            return True

        return self.is_valid_castling(board, start, end)

    def move(self, board, start, end):
        # Implement the logic to move the piece
        pass

    def is_valid_castling(self, board, start, end):
        if self.is_castling_done():
            return False
        return True
        # Add logic for castling validity

    def is_castling_move(self, start, end):
        return True
        # Check if it's a castling move

    def get_symbol(self):
        return "KING"