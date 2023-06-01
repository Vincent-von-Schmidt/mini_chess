import pygame

import map
import const


class Game:
    def __init__(self, maxfps: int) -> None:

        self.maxfps: int = maxfps

        # screen config
        self.screen = pygame.display.set_mode(
            (const.BOARD_RESOLUTION, const.BOARD_RESOLUTION) 
        )
        pygame.display.set_caption("Mini Chess")

        self.clock: pygame.time.Clock = pygame.time.Clock()
        pygame.key.set_repeat(30, 30)

        # stops game loop if necesary
        self.running: bool = True

        # init map
        self.map: map.Map = map.Map()

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

        # close window on key e -> faster keyboard control
        if keys[pygame.K_e]:
            self.running: bool = False

    def update(self) -> None:
        """
        game logic
        """

        pass

    def render(self) -> None:
        """
        renders the screen
        """

        # objects -----------------------------------------------

        # queue with all objects to draw
        objects: list = []

        # objects to draw on screen

        objects.append(self.map.get_map())

        # display -----------------------------------------------

        # create unscaled surface to draw all objects on
        original_surface: pygame.surface.Surface =  pygame.surface.Surface(
            # calc initial surface resolution befor upscaling
            (const.RATIO[0] * const.TILE_SIZE, const.RATIO[1] * const.TILE_SIZE)
        )
        original_surface.fill((0, 0, 0)) # fill black
        original_surface.blits(objects) # draw objects on surface

        # upscale drawn surface
        scaled_surface: pygame.surface.Surface = pygame.transform.scale(
            original_surface, # source -> unscaled surface
            (const.BOARD_RESOLUTION, const.BOARD_RESOLUTION) # resolution
        )

        # draw upscaled surface on main screen
        self.screen.blit(scaled_surface, (0, 0))
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

        pygame.init()

        while self.running:

            self.input()
            self.update()
            self.render()
            self.wait()

        pygame.quit()