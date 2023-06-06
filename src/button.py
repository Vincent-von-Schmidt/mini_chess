import pygame

import const


class Button:
    def __init__(self, text: str, clicked: function) -> None:

        self.text: str = text
        self.clicked: function = clicked

        self.font: pygame.font.Font = pygame.font.SysFont( const.FONT, 10 )
        
        self.surface: pygame.surface.Surface = pygame.surface.Surface(
            (const.BOARD_RESOLUTION, const.BOARD_RESOLUTION / 8)
        )

    def render(self) -> None:

        self.surface.fill( (111, 196, 213) )
