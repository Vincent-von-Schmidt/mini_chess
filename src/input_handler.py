import pygame
from typing import Any
from dataclasses import dataclass


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
    def __init__(self, color) -> None:
        super().__init__()
        self.color = color
        self.root = Node(
            turn = [0, 0],
            rating = 0,
            alpha = -999,
            beta = 999,
            pointer = []
        )
    
    def play_best_turn(self, position):
        pass

    def rate_turn(self, position):
        pass

    def build_tree(self, position):
        return self.build( self.root, position )

    def build(self, tree: Node, position):
        
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
                
                node: Node = self.build(
                    tree = Node(
                        turn = turn,
                        rating = 0,
                        alpha = -999,
                        beta = 999,
                        pointer =[]
                    ),
                    position = position
                )

                tree.pointer.append( node )

            return tree
