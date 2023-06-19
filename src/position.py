import pygame

import const
import input_handler

class Position:
    def __init__(self, player1, player2, cur, field = const.FIELD_EMPTY, turn = 0) -> None:
        
        self.field = field
        self.player = [player1, player2]
        self.cur = cur
        self.turn = turn
        self.history = []
    
    def set_turn(self, start, target) -> None:
        self.field[target] = self.field[start]
        self.field[start] = 0
        self.turn += 1
        self.cur = self.player[self.turn%2]
        self.history.append([start, target])
        print("Gespielt: ", start, "nach", target)

    def get_position(self) -> list:
        return self.field
    
    def get_possible_turns(self) -> list:
        if self.cur == self.player[0]: pl = 1
        else: pl = -1
        turns = []
        for i in range(len(self.field)):
            if self.field[i] == 1*pl:
                turns += self.find_turns(i%const.RATIO[0],i//const.RATIO[1],i,self.field,const.PAWN_MOV,const.MOVE,pl)
                turns += self.find_turns(i%const.RATIO[0],i//const.RATIO[1],i,self.field,const.PAWN_ATK,const.ATTACK,pl)
        return turns
    
    def find_turns(self, x,y,n,fld,mtr,tp,pl) -> list:
        turns = []
        if pl == -1:
            fld = fld[::-1]
            x = (const.RATIO[0]-1)-x
            y = (const.RATIO[0]-1)-y
            n = (const.RATIO[0]*y)+x
            # print("N", n)
        for i in range(const.RATIO[0]):
            for j in range(const.RATIO[1]):
                p = const.MATRIX_RAT*(const.MATRIX_POS+i-y) + const.MATRIX_POS-x+j
                n2 = const.RATIO[0]*i + j
                # if pl == -1: n2 = (const.RATIO[0]*const.RATIO[1])-n2
                # print("X", x, "Y", y)
                # print("Position", p)
                # print("Ziel", n2)
                # print("Target", fld[n2])
                if tp == const.ATTACK:
                    if mtr[p] == 0: continue
                    if fld[n2] == 0: continue
                    if (fld[n2]/abs(fld[n2])) != fld[n]/abs(fld[n]):
                        # print(n, "kann", n2, "schlagen")
                        turns.append([n, n2])
                else:
                    if mtr[p] == 1: continue
                    if fld[n2] != 0: continue
                    # kann noch nicht mehrere in eine Richtung gehen
                    # print(n, "kann nach", n2, "moven")
                    turns.append([n, n2])
        if pl == -1:
            for i in range(len(turns)):
                for j in range(2):
                    turns[i][j] = (const.RATIO[0]*const.RATIO[1]-1)-turns[i][j]
        # print(turns)
        return turns
    
    def check_end(self) -> bool:
        if self.cur == self.player[1]: pl = 1
        else: pl = -1
        n = 0
        for i in range(len(self.field)):
            if self.field[i] == 0: continue
            if (self.field[i]//abs(self.field[i])) == pl:
                if pl == 1 and i//const.RATIO[0] == 0:
                    return True
                if pl == -1 and i//const.RATIO[0] == 2:
                    return True
            else:
                n += 1
        if n == 0:
            return True
        return False
