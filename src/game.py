import pygame

import map
import clickable
import const
import position
import input_handler


class Game:
    def __init__(self, maxfps: int) -> None:

        self.maxfps: int = maxfps

        # screen config
        self.screen = pygame.display.set_mode(
            const.WINDOW_RESOLUTION
        )
        pygame.display.set_caption("Mini Chess")

        self.clock: pygame.time.Clock = pygame.time.Clock()
        pygame.key.set_repeat(30, 30)

        # stops game loop if necesary
        self.running: bool = True

        # init map
        self.map: map.Map = map.Map()

        # clickable objects
        self.clickable_objects: list = []

        self.clickable_objects.append( clickable.Button(
            text = "resign",
            position = (0, const.BOARD_RESOLUTION[1]),
            on_click = lambda: print("clicked"),
        ))

        # init figures
        for index, element in enumerate( const.FIELD_EMPTY ):
            match element:

                case 1:
                    self.clickable_objects.append( clickable.Figure(
                        color = const.PLAYER_COLOR_B,
                        tile = self.map.get_tile_by_id( index )
                    )) 

                case -1:
                    self.clickable_objects.append( clickable.Figure(
                        color = const.PLAYER_COLOR_A,
                        tile = self.map.get_tile_by_id( index )
                    )) 

        self.highlighted_figure: clickable.Figure | None = None

        self.tmp: bool = True
        self.player1: input_handler.Player = input_handler.Player( const.WHITE )
        self.player2: input_handler.Player = input_handler.Player( const.BLACK )
        self.position: position.Position = position.Position(
            self.player1,
            self.player2,
            cur = self.player1
        )
        self.turns = self.position.get_possible_turns()

        self.last_turn: tuple[int, int] | None = None

    def input(self) -> None:
        """
        key input + reaction
        """

        # get all events
        events: list = pygame.event.get()
        keys: pygame.key.ScanccodeWrapper = pygame.key.get_pressed()

        for event in events:

            match event.type:

                case pygame.QUIT:
                    self.running: bool = False

                case pygame.MOUSEBUTTONUP:
                    if event.button == 1: # left click

                        tile: map.Tile | None = self.map.get_tile_by_hover()
                        
                        # if highlighted
                        if self.highlighted_figure != None:

                            print(f"{self.turns = }")

                            turn: list[int, int] = [self.highlighted_figure.get_tile().get_id(), tile.get_id()]
                            print(f"{turn = }")

                            # evaluation
                            if turn in self.turns:
                                
                                # if figure on tile, kill it
                                if tile.get_figure() != None:
                                    tile.set_figure( None )
                                    figure = tile.get_figure()
                                    del figure

                                # move figure
                                self.highlighted_figure.set_tile( tile )
                                print("moved")

                            # remove highlight from figure
                            self.highlighted_figure.set_highlight( False )
                            self.highlighted_figure = None

                            # save turn for evalution
                            self.last_turn = turn
                            print(f"{self.last_turn = }")
                            break # otherwise highlighted_figure will be set in next loop entry

                        if tile != None and tile.get_figure() != None:
                            print("got tile")
                            self.highlighted_figure = tile.get_figure()
                            self.highlighted_figure.set_highlight( True )
                            break

            for object in self.clickable_objects:
                object.update(event)

        # close window on key e -> faster keyboard control
        if keys[pygame.K_e]:
            self.running: bool = False


    def update(self) -> None:
        """
        game logic
        """

        if self.last_turn in self.turns:
            if type(self.position.cur) == input_handler.Player: self.position.cur.handle_input(self.position, self.last_turn)
            else: self.position.cur.play_best_turn(self.position)
            self.last_turn = []
            self.turns = self.position.get_possible_turns()
            print(self.position.field)
        if self.position.check_end():
            self.running = False
            print(self.position.field)
            print(self.position.player[self.position.player.index(self.position.cur)-1].color, "wins")
        if len(self.turns) == 0 and self.position.turn != 0:
            self.running = False
            print("Remis")


    def render(self) -> None:
        """
        renders the screen
        """

        # objects_board -----------------------------------------------

        # queue with all objects_board to draw
        objects_board: list = []
        objects_window: list = []

        # objects_board to draw on screen

        objects_board.append(self.map.get_map())
        for object in self.clickable_objects:

            if isinstance( object, clickable.Button ):
                objects_window.append( object.get_map() )
            elif isinstance( object, clickable.Figure ):
                objects_board.append( object.get_map() )

        # objects_window.append(self.button_start.get_map())

        # display -----------------------------------------------

        # create unscaled surface to draw all objects_board on
        original_surface_board: pygame.surface.Surface =  pygame.surface.Surface(
            # calc initial surface resolution befor upscaling
            (const.RATIO[0] * const.TILE_SIZE, const.RATIO[1] * const.TILE_SIZE)
        )
        original_surface_board.fill((0, 0, 0)) # fill black
        original_surface_board.blits(objects_board) # draw objects_board on surface

        # upscale drawn surface
        scaled_surface_board: pygame.surface.Surface = pygame.transform.scale(
            original_surface_board, # source -> unscaled surface
            const.BOARD_RESOLUTION
        )

        main_window_surface: pygame.surface.Surface = pygame.surface.Surface(
            const.WINDOW_RESOLUTION
        )

        main_window_surface.blit(scaled_surface_board, (0, 0))
        main_window_surface.blits(objects_window)

        # draw upscaled surface on main screen
        self.screen.blit(main_window_surface, (0, 0))
        pygame.display.flip() # update screen

    def wait(self) -> None:
        """
        Wait to perserve frame rate.
        """

        self.clock.tick(self.maxfps)

    def run(self) -> None:
        """
        game loop
        """

        PvP = clickable.Button(
            text = "PvP",
            position = (0, const.BOARD_RESOLUTION[1]),
            on_click = 0,
        )
        PvE = clickable.Button(
            text = "PvE",
            position = (0, const.BOARD_RESOLUTION[1]),
            on_click = 1,
        )
        while True:
            events: list = pygame.event.get()
            for event in events:
                PvP.update(event)
                PvE.update(event)
            if PvP.

        while self.running:

            self.input()
            self.update()
            self.render()
            self.wait()
