import pygame

import map


class Game:
    def __init__(self, maxfps: int) -> None:

        self.maxfps: int = maxfps

        # screen config
        self.screen = pygame.display.set_mode((384, 384))
        pygame.display.set_caption("Mini Chess")

        self.clock: pygame.time.Clock = pygame.time.Clock()

        pygame.key.set_repeat(30, 30)

        self.running: bool = True

        self.map: map.Map = map.Map((3, 3))

    def input(self) -> None:
        """
        key input + reaction
        """

        pass

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

        objects: list = []

        objects.append(self.map.get_map())

        # display -----------------------------------------------

        original_surface: pygame.surface.Surface =  pygame.surface.Surface((384, 384))
        original_surface.fill((0, 0, 0))
        original_surface.blits(objects)

        scaled_surface: pygame.surface.Surface = pygame.transform.scale(
            original_surface,
            (1000, 1000) # resolution
        )

        self.screen.blit(scaled_surface, (0, 0))
        pygame.display.flip()

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
