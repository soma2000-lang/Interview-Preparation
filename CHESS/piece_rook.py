from piece import Piece

class Rook(Piece):
    def __init__(self, is_white):
        super().__init__(is_white)
        self.has_moved = False  # For castling purposes

    def can_move(self, board, start, end):
        # Rook can move horizontally or vertically
        if start.x != end.x and start.y != end.y:
            return False

        # Determine direction of movement
        x_direction = 0 if start.x == end.x else (1 if end.x > start.x else -1)
        y_direction = 0 if start.y == end.y else (1 if end.y > start.y else -1)

        # Check if path is clear
        current_x, current_y = start.x + x_direction, start.y + y_direction
        while (current_x, current_y) != (end.x, end.y):
            if board.get_spot(current_x, current_y).piece is not None:
                return False
            current_x += x_direction
            current_y += y_direction

        # Check if end spot is empty or has an enemy piece
        if end.piece is not None and end.piece.is_white == self.is_white:
            return False

        return True

    def move(self, board, start, end):
        if self.can_move(board, start, end):
            # Capture piece if present
            if end.piece is not None:
                end.piece.set_captured(True)

            # Move the rook
            end.piece = self
            start.piece = None
            self.has_moved = True

            # Update the last move on the board
            board.last_move = board.Move(self, start, end)
        else:
            raise ValueError("Invalid move for Rook")

    def get_symbol(self):
        return "ROOK"