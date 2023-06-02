import pygame


class Input_Handler:
    def __init__(self) -> None:
        pass
    
    def set_turn(self) -> None:
        ...


class Player(Input_Handler):
    ...


class AI(Input_Handler):
    def __init__(self) -> None:
        super().__init__()
