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
        if self.can_move(board, start, end):
            if self.is_castling_move(start, end):
                self.perform_castling(board, start, end)
            else:
                # Regular move
                if end.piece:
                    end.piece.set_captured(True)
                end.piece = self
                start.piece = None
            self.set_castling_done(True)
        else:
            raise ValueError("Invalid move for King")

    def is_valid_castling(self, board, start, end):
        if self.is_castling_done():
            return False
        
        # Check if it's a castling move
        if abs(start.x - end.x) != 2 or start.y != end.y:
            return False

        # Check if the path is clear
        direction = 1 if end.x > start.x else -1
        for i in range(1, 3):
            if board.get_spot(start.x + i * direction, start.y).piece:
                return False

        # Check if the king or the rook has moved
        if self.has_moved or board.get_spot(end.x + (1 if direction == -1 else -1), end.y).piece.has_moved:
            return False

        # Check if the king is in check or passes through check
        for i in range(3):
            if board.is_spot_under_attack(self.is_white, start.x + i * direction, start.y):
                return False

        return True

    def is_castling_move(self, start, end):
        return abs(start.x - end.x) == 2 and start.y == end.y

    def perform_castling(self, board, start, end):
        direction = 1 if end.x > start.x else -1
        rook_start = board.get_spot(end.x + (1 if direction == -1 else -1), end.y)
        rook_end = board.get_spot(start.x + direction, start.y)

        # Move the king
        end.piece = self
        start.piece = None

        # Move the rook
        rook_end.piece = rook_start.piece
        rook_start.piece = None

    def get_symbol(self):
        return "KING"