import pygame

import const


class Clickable_object:
    def __init__(self, position: tuple[int, int]) -> None:

        self.position: tuple[int, int] = position
        self.clicked: function | None = None
        self.surface: pygame.surface.Surface | None = None
        self.highlight: tuple[int, int, int] | None = None

    def set_clicked(self, function: function) -> None:
        self.clicked = function

    def set_geometry(self, surface: pygame.surface.Surface) -> None:
        self.surface = surface

    def set_highlight(self, color: tuple[int, int, int]) -> None:
        self.highlight = color

    def get_map(self) -> list:
        return [self.surface, self.position]


class Button( Clickable_object ):
    def __init__(self, text: str, position: tuple[int, int]) -> None:
        super().__init__(position)

        self.text: pygame.surface.Surface = const.FONT.render(
            text = text,
            antialias = False,
            color = (111, 196, 213)
        )

        self.surface: pygame.surface.Surface = pygame.surface.Surface(
            (const.BOARD_RESOLUTION, const.BOARD_RESOLUTION / 8)
        )
        self.surface.fill( (111, 196, 213) )

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
        pygame.draw.circle(
            surface = self.surface,
            color = color,
            center = (const.TILE_SIZE // 2, const.TILE_SIZE // 2),
            radius = const.TILE_SIZE // 2 - 2 # slidly smaller than the tile
        )

        self.set_geometry( self.surface )
