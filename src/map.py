import pygame


class Tile:
    def __init__(self, texture: tuple[int, ...] | str) -> None:
        """
        texture: tuple[int, ...] -> RBGA color code

        OR

        texture: str -> path to image file
        """

        self.surface: pygame.surface.Surface = pygame.surface.Surface( (128, 128) )

        # texture type check and coloring of surface

        if texture_type := type( texture ) == str:
            self.surface.blit(
                pygame.image.load( texture ), # load texture image
                (0, 0) # default position to draw
            )

        elif texture_type == tuple[int, ...]:
            self.surface.fill( texture )


class Map:
    def __init__(self, ratio: tuple[int, int]) -> None:

        self.ratio: tuple[int, int] = ratio

        # 128*128 -> tile size
        width: int = self.ratio[0] * 128
        height: int = self.ratio[1] * 128

        self.surface: pygame.surface.Surface = pygame.surface.Surface( (width, height) )

        # tiles will be loaded in this list
        self.construct_matrix: list = []

        self.load()
        self.render()

    def load(self) -> None:
        """
        build the construct_matrix
        """

        for _ in range( self.ratio[0] ): # per row
            
            # one list per row
            self.construct_matrix.append( row := [] )

            for _ in range( self.ratio[1] ): # per column

                # append white tile
                row.append( Tile((255, 255, 255)) )

    def render(self) -> None:
        """
        draws the surface
        """

        heights: list = []

        for row in self.construct_matrix:

            widths: list = []
            tmp_tile: Tile | None = None

            for tile in row:

                # drawing coordinates
                x: int = sum( widths )
                y: int = sum( heights )

                self.surface.blit(
                    source = tile.surface,
                    dest = ( x, y )
                )

                widths.append( tile.surface.get_width() )

                tmp_tile: Tile | None = tile

            heights.append( tmp_tile.surface.get_height() )

    def get_map(self) -> list:
        return [(self.surface), (0, 0)]
