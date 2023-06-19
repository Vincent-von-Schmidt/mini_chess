import pygame
from typing import Any
from dataclasses import dataclass
import copy


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


@dataclass
class Node:
    turn: list[int]
    rating: int
    alpha: int
    beta: int
    pointer: list


class AI(Input_Handler):
    def __init__(self, color, position = None) -> None:
        super().__init__()

        self.color = color
        self.position = position
        self.last_turn: list[int] = [0, 0]

        self.root: Node | None = None

        # self.build_tree( self.position )

    def set_position(self, position) -> None:
        self.position = position
    
    def play_best_turn(self, position):

        # get child with max rating
        child_max: tuple[Node | None, int] = (None, 0)
        for child in self.root.pointer:
            if child.rating > child_max[1]: child_max = (child, child.rating)

        self.root = child_max[0]
        position.set_turn( self.root.turn[0], self.root.turn[1] )

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
            
            rating: int = 0 # draw

            if position.cur == self: rating = 1 # win
            else: rating = -1 # lose

            match min_max_switch:

                case 1: # max
                    if rating > alpha: alpha = rating

                case -1: # min
                    if rating < beta: beta = rating

            return Node(
                turn = [],
                rating = rating,
                alpha = alpha,
                beta = beta,
                pointer = []
            )

        else:

            pointer: list[Node] = []

            for turn_neo in turns:

                position_neo = copy.deepcopy( position )
                position_neo.set_turn( turn_neo[0], turn_neo[1] )

                node: Node = self.build(
                    turn = turn_neo,
                    alpha = alpha,
                    beta = beta,
                    position = position_neo,
                    min_max_switch = -min_max_switch
                )

                alpha = node.alpha
                beta = node.beta

                # does not generate the remaining branches -> cut the rest
                if alpha >= beta: break

                pointer.append( node )

            match min_max_switch:

                case 1: # max

                    rating_list: list[int] = []

                    for child in pointer:
                        rating: int = child.rating
                        if rating > 0: rating_list.append( rating )
                    
                    rating: int = sum( rating_list )

                    if rating > alpha: alpha = rating

                case -1: # min

                    rating_list: list[int] = []

                    for child in pointer:
                        rating: int = child.rating
                        if rating < 0: rating_list.append( rating )
                    
                    rating: int = sum( rating_list )

                    if rating < beta: beta = rating

                case _:
                    raise TypeError( "min_max_switch has to be 1 or -1" )

            return Node(
                turn = turn,
                rating = rating,
                alpha = alpha,
                beta = beta,
                pointer = pointer
            )
