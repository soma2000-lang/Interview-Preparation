from piece import Piece

class Pawn(Piece):
    def __init__(self, is_white):
        super().__init__(is_white)
        self.has_moved = False

    def can_move(self, board, start, end):
        # Determine direction based on color
        direction = -1 if self.is_white else 1

        # Check for forward move
        if start.x == end.x and end.y == start.y + direction and end.piece is None:
            return True

        # Check for initial double move
        if not self.has_moved and start.x == end.x and end.y == start.y + 2 * direction:
            middle_spot = board.get_spot(start.x, start.y + direction)
            if end.piece is None and middle_spot.piece is None:
                return True

        # Check for diagonal capture
        if abs(start.x - end.x) == 1 and end.y == start.y + direction:
            if end.piece is not None and end.piece.is_white != self.is_white:
                return True

        # Check for en passant (assuming the Board class tracks the last moved pawn)
        if abs(start.x - end.x) == 1 and end.y == start.y + direction:
            if board.last_moved_piece is not None:
                last_move = board.last_moved_piece
                if isinstance(last_move, Pawn) and last_move.is_white != self.is_white:
                    if last_move.has_moved_two_squares and last_move.position.y == start.y:
                        return True

        return False

    def move(self, board, start, end):
        if self.can_move(board, start, end):
            # Check for promotion
            if (self.is_white and end.y == 0) or (not self.is_white and end.y == 7):
                # Promote pawn (you might want to add logic to let the player choose the piece)
                new_piece = Queen(self.is_white)  # Default promotion to Queen
                end.piece = new_piece
            else:
                # Regular move
                end.piece = self
            
            # Handle en passant capture
            if abs(start.x - end.x) == 1 and start.y != end.y and end.piece is None:
                captured_pawn_y = start.y
                board.get_spot(end.x, captured_pawn_y).piece = None

            start.piece = None
            self.has_moved = True

            # Set flag for two-square move (for en passant)
            self.has_moved_two_squares = abs(start.y - end.y) == 2

            # Update last moved piece on the board
            board.last_moved_piece = self
        else:
            raise ValueError("Invalid move for Pawn")

    def get_symbol(self):
        return "PAWN"