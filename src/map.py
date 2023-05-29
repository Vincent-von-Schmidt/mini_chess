import pygame

import const


class Tile:
    def __init__(self, texture: tuple[int, ...] | str) -> None:
        """
        texture: tuple[int, ...] -> RBGA color code

        OR

        texture: str -> path to image file
        """

        self.surface: pygame.surface.Surface = pygame.surface.Surface(
            (const.TILE_SIZE, const.TILE_SIZE) 
        )

        # texture type check and coloring of surface

        # get type of texture var
        texture_type: object = type( texture )

        # path given -> draw image on tile
        if texture_type == str:
            self.surface.blit(
                pygame.image.load( texture ), # load texture image
                (0, 0) # default position to draw
            )

        # color code given -> fill tile with given color
        elif texture_type == tuple:
            self.surface.fill( texture )


class Map:
    def __init__(self) -> None:

        width: int = const.RATIO[0] * const.TILE_SIZE
        height: int = const.RATIO[1] * const.TILE_SIZE

        self.surface: pygame.surface.Surface = pygame.surface.Surface( (width, height) )

        # tiles will be loaded in this list
        self.construct_matrix: list = []

        self.load()
        self.render()

    def load(self) -> None:
        """
        build the construct_matrix
        """

        chess_board_pattern_switch: bool = True

        for _ in range( const.RATIO[0] ): # row
            
            # one list per row
            self.construct_matrix.append( row := [] )

            for _ in range( const.RATIO[1] ): # column

                # black tile
                if chess_board_pattern_switch:
                    color: tuple = (0, 0, 0)
                    chess_board_pattern_switch: bool = False

                # white tile
                else:
                    color: tuple = (255, 255, 255)
                    chess_board_pattern_switch: bool = True

                # append white tile
                row.append( Tile(color) )

    def render(self) -> None:
        """
        draws the surface
        """

        heights: list = []

        for row in self.construct_matrix: # row

            widths: list = []
            tmp_tile: Tile | None = None

            for tile in row: # column

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
