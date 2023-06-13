import pygame

import const


class Tile:

    __number_instances: int = 0 
    
    def __new__(cls, *args, **kwargs):
        """
        counts the created objects to use as id
        """

        cls.__number_instances += 1
        return super().__new__(cls)

    def __init__(self, texture: tuple[int, ...] | str) -> None:
        """
        texture: tuple[int, ...] -> RBGA color code

        OR

        texture: str -> path to image file
        """

        self.position: tuple[int, int] | None = None
        self.id: int = self.__number_instances - 1 # indexing starts at 0

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

    def get_surface(self) -> pygame.surface.Surface:
        return self.surface

    def set_position(self, coordinates: tuple[int, int]) -> None:
        self.position = coordinates

    def get_position(self) -> tuple[int, int]:
        return self.position

    def get_id(self) -> int:
        return self.id


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
                    chess_board_pattern_switch: bool = False
                    row.append( Tile(const.BOARD_COLOR_A) )

                # white tile
                else:
                    chess_board_pattern_switch: bool = True
                    row.append( Tile(const.BOARD_COLOR_B) )

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
                destination: tuple[int, int] = ( x, y )

                tile.set_position( destination )

                self.surface.blit(
                    source = tile.surface,
                    dest = destination
                )

                widths.append( tile.surface.get_width() )

                tmp_tile: Tile | None = tile

            heights.append( tmp_tile.surface.get_height() )

    def get_map(self) -> list:
        return [(self.surface), (0, 0)]

    def get_construct_matrix(self) -> list[list[Tile]]:
        return self.construct_matrix

    def get_tile_by_id(self, id: int) -> Tile:
        """
        returns the tile with the given id
        """

        for row in self.construct_matrix:
            for tile in row:

                if tile.get_id() == id:
                    return tile

        raise NotImplementedError( f"No tile with the id: {id} found." )

    def get_tile_by_hover( self ) -> Tile:
        """
        return hoverd tile
        """

        mouse_position: tuple[int, int] = pygame.mouse.get_pos()

        for row in self.construct_matrix:
            for tile in row:

                tile_coordinats: tuple[int, int] = tile.get_position()
                tile_surface: pygame.surface.Surface = tile.get_surface()
                
                if ( mouse_position[0] >= tile_coordinats[0] and mouse_position[0] <= tile_coordinats[0] + tile_surface.get_width() # x
                    and mouse_position[1] >= tile_coordinats[1] and mouse_position[1] <= tile_coordinats[1] + tile_surface.get_height()): # y

                    return tile
