from piece import Piece

class Bishop(Piece):
    def __init__(self, is_white):
        super().__init__(is_white)

    def can_move(self, board, start, end):
        # Check if the end position is occupied by a piece of the same color
        if end.piece is not None and end.piece.is_white == self.is_white:
            return False

        # Check if the move is diagonal
        dx = abs(end.x - start.x)
        dy = abs(end.y - start.y)
        if dx != dy:
            return False

        # Determine the direction of movement
        x_direction = 1 if end.x > start.x else -1
        y_direction = 1 if end.y > start.y else -1

        # Check for obstacles along the path
        x, y = start.x + x_direction, start.y + y_direction
        while x != end.x and y != end.y:
            if board.get_spot(x, y).piece is not None:
                return False
            x += x_direction
            y += y_direction

        return True

    def move(self, board, start, end):
        if self.can_move(board, start, end):
            # Remove the piece from the start position
            start.piece = None
            
            # Capture the piece at the end position if there is one
            if end.piece is not None:
                end.piece.is_captured = True
            
            # Move the bishop to the end position
            end.piece = self
        else:
            raise ValueError("Invalid move for Bishop")

    def get_symbol(self):
        return "BISHOP"