import pygame


class Input_Handler:
    def __init__(self) -> None:
        pass
    
    def set_turn(self) -> None:
        ...


class Player(Input_Handler):
    def __init__(self, color) -> None:
        super().__init__()
        self.color = color
    
    def handle_input(self, position, turn):
        # hier Schnittstelle zwischen clickable und game loop
        if len(turn) == 2:
            position.set_turn(turn[0], turn[1])


class AI(Input_Handler):
    def __init__(self, color) -> None:
        super().__init__()
        self.color = color
        self.root = None
    
    def play_best_turn(self, position):
        pass

    def rate_turn(self, position):
        pass

    def build_tree(self, position):
        pass
