import pygame
from typing import Callable, Any

import main
import const
# from map import Tile


class Clickable_object:
    def __init__(
        self,
        position: tuple[int, int],
        on_click: Callable | None = None,
    ) -> None:
        """
        parent class to create button objects
        """

        self.position: tuple[int, int] = position
        self.on_click: Callable | None = on_click
        self.on_click_return: Any | None = None
        self.surface: pygame.surface.Surface | None = None

    def set_clicked(self, on_click: Callable) -> None:
        """
        set function to execute on click
        """
        self.on_click = on_click

    def get_function_return(self) -> Any:
        return self.on_click_return

    def set_geometry(self, surface: pygame.surface.Surface) -> None:
        """
        updates the surface to draw on screen
        """
        self.surface = surface

    def get_map(self) -> list:
        """
        returns the surface and the coordinates to draw it on the screen
        """
        return [self.surface, self.position]

    def is_hover(self) -> bool:
        """
        if mouse is hovering over object, return true
        """

        mouse_position: tuple[int, int] = pygame.mouse.get_pos()

        if ( mouse_position[0] >= self.position[0] and mouse_position[0] <= self.position[0] + self.surface.get_width() # x
            and mouse_position[1] >= self.position[1] and mouse_position[1] <= self.position[1] + self.surface.get_height()): # y

            return True

        return False

    def update(self, event) -> None:
        """
        processe the user inputs
        """

        if self.is_hover():

            # hover color change
            self.surface.set_alpha(150)

            if event.type == pygame.MOUSEBUTTONUP:

                if self.on_click != None:
                    self.on_click_return = self.on_click()

        # reset hover color to none
        else: self.surface.set_alpha(255)


class Button( Clickable_object ):
    def __init__(
        self,
        text: str,
        position: tuple[int, int],
        on_click: Callable | None = None,
    ) -> None:
        """
        button with clickable area
        """

        super().__init__(position, on_click)

        self.text: pygame.surface.Surface | None = None

        self.surface: pygame.surface.Surface = pygame.surface.Surface(
            (const.BOARD_RESOLUTION[0], const.BOARD_RESOLUTION[1] // 4)
        )
        
        self.font: pygame.font.Font = pygame.font.SysFont( const.FONT[0], const.FONT[1] )
        self.set_text( text )

        self.render()

    def render(self) -> None:
        """
        draws the texture + text on surface and initialize it in parent class
        """

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
        """
        set and render text on button
        """
        self.text = self.font.render(
            text, False, (0, 0, 0)
        )


class Figure( Clickable_object ):
    
    def __init__(
        self,
        color: tuple[int, int, int],
        tile # tile: map.Tile
    ) -> None:
        """
        playable character
        """

        self.color: tuple[int, int, int] = color
        self.pre_tile = tile
        self.tile = tile
        self.tile.set_figure( self )

        self.highlight: bool = False

        self.render()

    def __del__(self) -> None:
        """
        destructor
        """
        self.tile.set_surface( self.tile.get_initial_surface() )

    def set_tile(self, tile) -> None:
        """
        updates tile to draw on -> moves the figure to another tile
        """
        self.pre_tile = self.tile
        self.tile = tile
        self.pre_tile.set_figure( None )
        self.tile.set_figure( self )
        self.render()

    def get_tile(self):
        """
        return tile, where the figure is drawn on
        """
        return self.tile

    def set_highlight(self, switch: bool) -> None:
        """
        set highlight and rerenders the surface to add visible yellow circle around figure
        """
        self.highlight = switch
        self.render()

    def render(self) -> None:
        """
        draws the circles on the surface and update it in parent class
        """

        super().__init__(
            position = (self.tile.get_position())
        )

        surface: pygame.surface.Surface = self.tile.get_initial_surface()

        center: tuple[int, int] = (const.TILE_SIZE // 2, const.TILE_SIZE // 2)
        radius = const.TILE_SIZE // 2 - 15 # slidly smaller than the self.tile

        # draws a slidly biger circle around the figure
        if self.highlight:
            pygame.draw.circle(
                surface = surface,
                color = (255, 255, 0),
                center = center,
                radius = radius + 2
            )

        # draws the figure -> circle
        pygame.draw.circle(
            surface = surface,
            color = self.color,
            center = center,
            radius = radius
        )

        # updates the surface to draw on map
        self.tile.set_surface( surface )
        self.set_geometry( surface )

def button_push():
    return True
