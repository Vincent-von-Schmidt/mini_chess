import pygame

import const


class Button:
    def __init__(self, text: str, clicked: function) -> None:

        self.text: str = text
        self.clicked: function = clicked
        
        self.surface: pygame.surface.Surface = pygame.surface.Surface(
            (const.BOARD_RESOLUTION, const.BOARD_RESOLUTION / 8)
        )

    def render(self) -> None:
        ...
