import pygame

import const
import input_handler

class Position:
    def __init__(self, player1, player2, next, field = const.FIELD_EMPTY, turn = 0) -> None:
        
        self.field = field
        self.player = [player1, player2]
        self.next = next
        self.turn = turn
    
    def set_turn(self, start, target) -> None:
        self.field[target] = self.field[start]
        self.field[start] = 0
        self.turn += 1
        self.next = self.player[self.turn%2]

    def get_position(self) -> list:
        return self.field
    
    def get_possible_turns() -> list:
        turns = []
        return turns
    
    def check_end() -> bool:
        pass
