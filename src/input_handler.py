import pygame
from typing import Any
from dataclasses import dataclass
import copy


class Player:
    def __init__(self, color) -> None:
        self.color = color
    
    def handle_input(self, position, turn):
        # hier Schnittstelle zwischen clickable und game loop
        if len(turn) == 2:
            position.set_turn(turn[0], turn[1])


@dataclass
class Node:
    turn: list[int]
    rating: int
    alpha: int
    beta: int
    pointer: list


class AI:
    def __init__(self, color, position = None) -> None:

        self.color = color
        self.position = position
        self.last_turn: list[int] = [0, 0]

        self.root: Node | None = None

        # self.build_tree( self.position )

    def set_position(self, position) -> None:
        self.position = position
    
    def play_best_turn(self, position):

        # get child with max rating
        self.build_tree(position)
        print("Root: ", self.root)
        child_max: tuple[Node | None, int] = (None, -999)
        for child in self.root.pointer:
            if child.rating > child_max[1]: child_max = (child, child.rating)
            else: del child

        self.root = child_max[0]
        print("Root: ", self.root)
        position.set_turn( self.root.turn[0], self.root.turn[1] )

    def rate_turn(self, position) -> int:
        rate = 0
        turns = position.get_possible_turns()
        print(position.cur, self)
        if position.check_end() and type(position.cur) == type(self): 
            rate = -1*(10-position.turn) # lose
        elif position.check_end() and type(position.cur) != type(self): 
            rate = 1*(5-position.turn) # win
        elif len(turns) == 0: 
            rate = 0 # draw
        for i in position.field:
            pass
        return rate

    def build_tree(self, position):
        self.root = self.build( 
            turn = [0, 0],
            alpha = -999,
            beta = 999,
            position = position,
            min_max_switch = 1
        )

    def build(self,
        turn: list[int],
        alpha: int,
        beta: int,
        position,
        min_max_switch: int
    ) -> Node:
        
        turns: list[list[int]] = position.get_possible_turns()
        alpha = alpha
        beta = beta

        # last turn
        if turns == [] or position.check_end():
            
            rating = self.rate_turn(position)

            match min_max_switch:

                case 1: # max
                    if rating > alpha: alpha = copy.deepcopy(rating)

                case -1: # min
                    if rating < beta: beta = copy.deepcopy(rating)

            return Node(
                turn = turn,
                rating = rating,
                alpha = alpha,
                beta = beta,
                pointer = []
            )

        else:

            pointer: list[Node] = []

            rating = None

            for turn_neo in turns:


                position_neo = copy.deepcopy( position )
                position_neo.set_turn( turn_neo[0], turn_neo[1] )

                node: Node = self.build(
                    turn = turn_neo,
                    alpha = -999,
                    beta = beta,
                    position = position_neo,
                    min_max_switch = -min_max_switch
                )

                pointer.append( node )

                match min_max_switch:

                    case 1: # max

                        if node.beta > alpha:
                            alpha = copy.deepcopy(node.beta)
                            rating = copy.deepcopy(node.beta)

                    case -1: # min
                        if node.alpha < beta: 
                            beta = copy.deepcopy(node.alpha)
                            rating = copy.deepcopy(node.alpha)

                    case _:
                        raise TypeError( "min_max_switch has to be 1 or -1" )

                if alpha > beta: break

            return Node(
                turn = turn,
                rating = rating,
                alpha = alpha,
                beta = beta,
                pointer = pointer
            )
