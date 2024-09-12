class Piece:


    def   __init__(self,white:bool):
        self._is_white_piece = white
        self._is_piece_killed = False
        
    def is_white(self) -> bool:
            return self._is_white_piece
    def set_white(self, p_is_white: bool):
            self._is_white_piece = p_is_white

    def is_killed(self) -> bool:
            return self._is_piece_killed
    def set_killed(self, killed: bool):
            self._is_piece_killed = killed
    def get_symbol(self) -> str:
            # This method should be overridden by subclasses
            pass

    def can_move(self, board, start, end) -> bool:
            # This method should be overridden by subclasses
            pass
