import pygame

import const


class Tile:

    __number_instances: int = 0 
    
    def __new__(cls, *args, **kwargs):
        """
        counts the created objects to use as id

        :param *args: *args passed to constructor
        :param *kwargs: *kwargs passed to constructor

        :return Tile object: the created object
        """

        cls.__number_instances += 1
        return super().__new__(cls)

    def __init__(self, texture: tuple[int, ...] | str) -> None:
        """
        field on map

        :param tuple[int, ...] texture: RGB colorcode - color of surface
        :param str texture: path to texture image - texture of surface
        """

        self.position: tuple[int, int] | None = None
        self.id: int = self.__number_instances - 1 # indexing starts at 0
        self.figure = None

        self.surface: pygame.surface.Surface = pygame.surface.Surface(
            (const.TILE_SIZE, const.TILE_SIZE) 
        )

        # texture type check and coloring of surface

        # get type of texture var
        texture_type: object = type( texture )

        # path given -> draw image on tile
        if texture_type == str:
            self.surface.blit(
                pygame.image.build( texture ), # build texture image
                (0, 0) # default position to draw
            )

        # color code given -> fill tile with given color
        elif texture_type == tuple:
            self.surface.fill( texture )

        self.inital_surface: pygame.surface.Surface = self.surface.copy()

        self.highlight_surface: pygame.surface.Surface = self.surface.copy()
        tmp = pygame.surface.Surface((const.TILE_SIZE, const.TILE_SIZE))
        tmp.fill((200, 10, 10))
        tmp.set_alpha(100)
        self.highlight_surface.blit(tmp, (0,0))

    def set_surface(self, surface: pygame.surface.Surface) -> None:
        """
        update the internal surface

        :param pygame.surface.Surface surface: new surface
        """

        self.surface = surface

    def get_surface(self) -> pygame.surface.Surface:
        """
        return the drawn image

        :return pygame.surface.Surface: internal surface
        """

        return self.surface

    def get_initial_surface(self) -> pygame.surface.Surface:
        """
        return the initial surface without any outside changes

        :return pygame.surface.Surface: surface with no changes made
        """

        return self.inital_surface.copy()

    def get_highlight_surface(self) -> pygame.surface.Surface:
        """
        return the highlight surface

        :return pygame.surface.Surface: modified surface with highlight layer
        """

        return self.highlight_surface.copy()

    def set_highlight(self, switch: bool) -> None:
        """
        replaces the surface with the modified highlight surface or reset
        the surface to the unmodified surface

        :param bool switch: decide if tile should be highlighted or not
        """

        if switch:
            self.set_surface(self.get_highlight_surface())
        else:
            self.set_surface(self.get_initial_surface())

    def is_hover(self) -> bool:
        """
        check if mouse if hovering over tile

        :return bool: returns True if mouse is hovering
        """

        mouse_position: tuple[int, int] = pygame.mouse.get_pos()

        if ( mouse_position[0] >= self.position[0] and mouse_position[0] <= self.position[0] + self.surface.get_width() # x
            and mouse_position[1] >= self.position[1] and mouse_position[1] <= self.position[1] + self.surface.get_height()): # y

            return True

        return False

    def set_position(self, coordinates: tuple[int, int]) -> None:
        """
        updates the coordinates of the tile

        :param tuple[int, int] coordinates: coordinates of the top left corner of the tile
        """

        self.position = coordinates

    def set_figure(self, figure) -> None:
        """
        saves the figure wich is currently drawn on surface

        :param clickable.Figure figure: game figure
        """

        self.figure = figure

    def get_figure(self):
        """
        :return clickable.Figure: game figure
        """

        return self.figure

    def get_position(self) -> tuple[int, int] | None:
        """
        :return tuple[int, int]: coordinates of the top left corner of the tile
        """

        return self.position

    def get_id(self) -> int:
        """
        :return int: tile id
        """

        return self.id


class Map:
    def __init__(self) -> None:
        """
        chess board
        """

        width: int = const.RATIO[0] * const.TILE_SIZE
        height: int = const.RATIO[1] * const.TILE_SIZE

        self.surface: pygame.surface.Surface = pygame.surface.Surface( (width, height) )

        # tiles will be loaded in this list
        self.construct_matrix: list = []

        self.build()
        self.render()

    def build(self) -> None:
        """
        build the construct_matrix
        """

        for y in range( const.RATIO[0] ): # row
            
            # one list per row
            self.construct_matrix.append( row := [] )

            for x in range( const.RATIO[1] ): # column

                # black tile
                if y%2 + x%2 == 1:
                    row.append( Tile(const.BOARD_COLOR_B) )

                # white tile
                else:
                    row.append( Tile(const.BOARD_COLOR_A) )

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
        """
        returns the surface and coordinates in the format used by the pygame 
        builtin blits function

        :return list: surface + coordinates
        """

        return [(self.surface), (0, 0)]

    def get_construct_matrix(self) -> list[list[Tile]]:
        """
        construct_matrix built by build function

        :return list[list[Tile]]: tile matrix
        """

        return self.construct_matrix

    def get_tile_by_id(self, id: int) -> Tile:
        """
        goes through the tiles used in map and returns the Tile with the given id

        :param int id: id of tile

        :return Tile: map field

        :raises NotImplementedError: if tile with given id was not found
        """

        for row in self.construct_matrix:
            for tile in row:

                if tile.get_id() == id:
                    return tile

        raise NotImplementedError( f"No tile with the id: {id} found." )

    def get_tile_by_hover( self ) -> Tile | None:
        """
        check wich tile is hoverd by the mouse and returns it

        :return Tile: map field
        :return None: if no tile is hoverd
        """

        for row in self.construct_matrix:
            for tile in row:

                if tile.is_hover():
                    return tile

        return None
