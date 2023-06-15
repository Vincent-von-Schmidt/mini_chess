import pygame
from typing import Callable

import const
from map import Tile


class Clickable_object:
    def __init__(
        self,
        position: tuple[int, int],
        on_click: Callable | None = None,
    ) -> None:

        self.position: tuple[int, int] = position
        self.on_click: Callable | None = on_click
        self.surface: pygame.surface.Surface | None = None

    def set_clicked(self, on_click: Callable) -> None:
        self.on_click = on_click

    def set_geometry(self, surface: pygame.surface.Surface) -> None:
        self.surface = surface
        self.non_highlighted_surface = self.surface

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

            # hover color change
            self.surface.set_alpha(150)

            if event.type == pygame.MOUSEBUTTONUP:

                if self.on_click != None:
                    self.on_click()

        # reset hover color to none
        else: self.surface.set_alpha(255)


class Button( Clickable_object ):
    def __init__(
        self,
        text: str,
        position: tuple[int, int],
        on_click: Callable | None = None,
    ) -> None:

        super().__init__(position, on_click)

        self.text: pygame.surface.Surface | None = None

        self.surface: pygame.surface.Surface = pygame.surface.Surface(
            (const.BOARD_RESOLUTION[0], const.BOARD_RESOLUTION[1] // 4)
        )
        
        self.font: pygame.font.Font = pygame.font.SysFont( const.FONT[0], const.FONT[1] )
        self.set_text( text )

        self.render()

    def render(self) -> None:

        self.surface.fill( (81, 145, 158) )

        self.surface.blit(
                source = self.text,
                dest = (
                    self.surface.get_width() // 2 - self.text.get_width() // 2,
                    self.surface.get_height() // 2 - self.text.get_height() // 2
                    )
                )

        self.set_geometry( self.surface )

    def set_text(self, text: str) -> None:
        self.text = self.font.render(
            text, False, (0, 0, 0)
        )


class Figure( Clickable_object ):
    
    def __init__(
        self,
        color: tuple[int, int, int],
        tile # tile: map.Tile
    ) -> None:

        self.color: tuple[int, int, int] = color
        self.pre_tile = tile
        self.tile = tile
        self.tile.set_figure( self )

        self.highlight: bool = False

        self.render()

    def set_tile(self, tile) -> None:
        self.pre_tile = self.tile
        self.tile = tile
        self.pre_tile.set_figure( None )
        self.tile.set_figure( self )
        self.render()

    def get_tile(self):
        return self.tile

    def set_highlight(self, switch: bool) -> None:
        self.highlight = switch
        self.render()

    def render(self) -> None:

        super().__init__(
            position = (self.tile.get_position())
        )

        surface: pygame.surface.Surface = self.tile.get_initial_surface()

        center: tuple[int, int] = (const.TILE_SIZE // 2, const.TILE_SIZE // 2)
        radius = const.TILE_SIZE // 2 - 15 # slidly smaller than the self.tile

        # draws a slidly biger circle around the figure
        print(f"{self.highlight = }")
        if self.highlight:
            pygame.draw.circle(
                surface = surface,
                color = (255, 255, 0),
                center = center,
                radius = radius + 2
            )

        pygame.draw.circle(
            surface = surface,
            color = self.color,
            center = center,
            radius = radius
        )

        self.tile.set_surface( surface )
        self.set_geometry( surface )
