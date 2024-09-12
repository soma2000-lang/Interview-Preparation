class Player:
    def __init__(self, p_name: str, p_is_white: bool):
        self.human_player = True
        self.name = p_name
        self.is_white = p_is_white
        self.is_curr_player = False

    def get_name(self) -> str:
        return self.name

    def is_white_side(self) -> bool:
        return self.is_white

    def is_human_player(self) -> bool:
        return self.human_player

class HumanPlayer(Player):
    def __init__(self, white_side: bool):
        super().__init__("Human Player", white_side)

class ComputerPlayer(Player):
    def __init__(self, white_side: bool):
        super().__init__("Computer Player", white_side)
        self.human_player = False
