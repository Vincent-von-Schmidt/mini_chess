import pygame

import map
import clickable
import const
import position


class Game:
    def __init__(self, maxfps: int) -> None:

        self.maxfps: int = maxfps

        # screen config
        self.screen = pygame.display.set_mode(
            # (const.BOARD_RESOLUTION, const.BOARD_RESOLUTION + const.BOARD_RESOLUTION // 4) 
            const.WINDOW_RESOLUTION
        )
        pygame.display.set_caption("Mini Chess")

        self.clock: pygame.time.Clock = pygame.time.Clock()
        pygame.key.set_repeat(30, 30)

        # stops game loop if necesary
        self.running: bool = True

        # init map
        self.map: map.Map = map.Map()
        self.button_start: clickable.Button = clickable.Button(
            text = "start",
            position = (0, const.BOARD_RESOLUTION[1]),
            on_click = lambda: print("clicked"),
            highlight = (89, 170, 186)
        )
        self.test_figure: clickable.Figure = clickable.Figure(
            # position = (100, 100),
            color = (155, 155, 155),
            tile = self.map.get_construct_matrix()[0][0]
        )

    def input(self) -> None:
        """
        key input + reaction
        """

        # get all events
        events: list = pygame.event.get()
        keys: pygame.key.ScanccodeWrapper = pygame.key.get_pressed()

        for event in events:

            # if clicked on the close button -> break game loop
            if event.type == pygame.QUIT:
                self.running: bool = False

            self.button_start.update(event)

        # close window on key e -> faster keyboard control
        if keys[pygame.K_e]:
            self.running: bool = False

    def update(self) -> None:
        """
        game logic
        """

        # if type(position.next) == Player: position.next.handle_input(position)
        # else: position.next.play_best_turn(position)
        pass

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
        objects_board.append(self.test_figure.get_map())

        objects_window.append(self.button_start.get_map())

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

        while self.running:

            self.input()
            self.update()
            self.render()
            self.wait()
