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

        self.root = Node(
            turn = [0, 0],
            rating = 0,
            alpha = -999,
            beta = 999,
            pointer = []
        )

        # self.build_tree( self.position )

    def set_position(self, position) -> None:
        self.position = position
    
    def play_best_turn(self, position):

        children: list[Node] = self.root.pointer

        for child in children:
            if child.rating == max( [child.rating for child in children] ):
                self.root = child
                position.set_turn( child.turn[0], child.turn[1] )
                break


    def build_tree(self, position):
        return self.build( self.root, position, 1 )

    def build(self, tree: Node, position, min_max_switch: int):
        
        turns: list[list[int]] = position.get_possible_turns()

        if turns == []: # draw
            return Node(
                turn = [],
                rating = 0,
                alpha = -999,
                beta = 999,
                pointer = []
            )

        elif position.check_end():

            if position.cur == self: # win
                return Node(
                    turn = [],
                    rating = 1,
                    alpha = -999,
                    beta = 999,
                    pointer = []
                )

            else: # lose
                return Node(
                    turn = [],
                    rating = -1,
                    alpha = -999,
                    beta = 999,
                    pointer = []
                )

        else:

            for turn in turns:

                position_neo = copy.deepcopy( position )
                position_neo.set_turn( turn[0], turn[1] )
                
                node: Node = self.build(
                    tree = Node(
                        turn = turn,
                        rating = 0,
                        alpha = -999,
                        beta = 999,
                        pointer = []
                    ),
                    position = position_neo,
                    min_max_switch = -min_max_switch
                )

                tree.pointer.append( node )

            # children
            children: list[Node] = tree.pointer 

            # negamax of the rating of the children equals the new rating
            tree.rating = -max( [child.rating for child in children] )

            return tree
