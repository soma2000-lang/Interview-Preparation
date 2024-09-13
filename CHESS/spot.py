class Spot:
    def __init__(self, x: int, y: int, piece=None):
        self.x = x
        self.y = y
        self.piece = piece

    def get_piece(self):
        return self.piece

    def set_piece(self, piece):
        self.piece = piece

    def get_x(self):
        return self.x

    def set_x(self, x: int):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y: int):
        self.y = y
