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
    
    def find_turns(self, x,y,n,fld,mtr,tp) -> list:
        turns = []
        for i in range(const.RATIO[0]):
            for j in range(const.RATIO[1]):
                p = const.MATRIX_RAT*(const.MATRIX_POS+i-y) + const.MATRIX_POS+x+j
                n2 = const.RATIO[0]*i + j
                print(fld[n2])
                if tp == const.ATTACK:
                    if mtr[p] == 0: continue
                    if fld[n2] == 0: continue
                    if (fld[n2]/abs(fld[n2])) != fld[n]/abs(fld[n]):
                        turns += [n, n2]
                else:
                    if mtr[p] != 1: continue
                    if fld[n2] != 0: continue
                    # kann noch nicht mehrere in eine Richtung gehen
                    turns += [n, n2]
        print(turns)
        return turns
    
    def check_end() -> bool:
        pass
