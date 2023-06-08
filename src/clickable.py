import pygame
from typing import Callable

import const


class Clickable_object:
    def __init__(
        self,
        position: tuple[int, int],
        on_click: Callable | None = None,
        highlight: tuple[int, int, int] | None = None
    ) -> None:

        self.position: tuple[int, int] = position
        self.on_click: Callable | None = on_click
        self.highlight: tuple[int, int, int] | None = highlight
        self.surface: pygame.surface.Surface | None = None

    def set_clicked(self, on_click: Callable) -> None:
        self.on_click = on_click

    def set_geometry(self, surface: pygame.surface.Surface) -> None:
        self.surface = surface

    def set_highlight(self, color: tuple[int, int, int]) -> None:
        self.highlight = color

    def get_map(self) -> list:
        return [self.surface, self.position]

    def is_hover(self) -> bool:

        mouse_position: tuple[int, int] = pygame.mouse.get_pos()

        if ( mouse_position[0] >= self.position[0] and mouse_position[0] <= self.position[0] + self.surface.get_width() # x
            and mouse_position[1] >= self.position[1] and mouse_position[1] <= self.position[1] + self.surface.get_height()): # y

            return True

        return False

    def update(self, event) -> None:

        if self.is_hover():

            if self.highlight != None:
                self.surface.fill( self.highlight )

            if event.type == pygame.MOUSEBUTTONUP:
                self.on_click()


class Button( Clickable_object ):
    def __init__(
        self,
        text: str,
        position: tuple[int, int],
        on_click: Callable | None = None,
        highlight: tuple[int, int, int] | None = None
    ) -> None:

        super().__init__(position, on_click, highlight)

        self.surface: pygame.surface.Surface = pygame.surface.Surface(
            (const.BOARD_RESOLUTION[0], const.BOARD_RESOLUTION[1] // 4)
        )
        
        font: pygame.font.Font = pygame.font.SysFont( const.FONT[0], const.FONT[1] )
        self.text: pygame.surface.Surface = font.render(
            text, False, (0, 0, 0)
        )

        self.surface.fill( (81, 145, 158) )

        self.surface.blit(
            source = self.text,
            dest = (
                self.surface.get_width() // 2 - self.text.get_width() // 2,
                self.surface.get_height() // 2 - self.text.get_height() // 2
            )
        )

        self.set_geometry( self.surface )


class Figure( Clickable_object ):
    def __init__(self, position: tuple[int, int], color: tuple[int, int, int]) -> None:
        super().__init__(position)

        self.surface: pygame.surface.Surface = pygame.surface.Surface(
            (const.TILE_SIZE, const.TILE_SIZE)
        )

        self.surface.set_alpha(128)

        pygame.draw.circle(
            surface = self.surface,
            color = color,
            center = (const.TILE_SIZE // 2, const.TILE_SIZE // 2),
            radius = const.TILE_SIZE // 2 - 2 # slidly smaller than the tile
        )

        self.set_geometry( self.surface )
