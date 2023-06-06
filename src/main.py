import pygame

import game

if __name__ == "__main__":

    pygame.init()
    pygame.font.init()

    a: game.Game = game.Game(144)
    a.run()

    pygame.font.quit()
    pygame.quit()
