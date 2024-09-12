class Move:
    def __init__(self, player, start_spot, end_spot, piece):
        self.player = player
        self.start = start_spot
        self.end = end_spot
        self.piece_moved = piece
        self.piece_killed = None
        self.castling_move = False
        self.is_valid_move = True

    def is_castling_move(self):
        return self.castling_move

    def set_castling_move(self, castling_move):
        self.castling_move = castling_move

    def set_invalid_move(self):
        self.is_valid_move = False

    def get_player(self):
        return self.player

    def get_start_spot(self):
        return self.start

    def get_end_spot(self):
        return self.end

    def get_piece_moved(self):
        return self.piece_moved

    def get_piece_killed(self):
        return self.piece_killed