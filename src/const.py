import pygame

TILE_SIZE: int = 128
RATIO: tuple[int, int] = (3, 3) # for chess board pattern -> only uneven numbers possible
BOARD_RESOLUTION: tuple[int, int] = (400, 400)
BOARD_COLOR_A: tuple[int, int, int] = (0, 0, 0)
BOARD_COLOR_B: tuple[int, int, int] = (255, 255, 255)
# FONT: pygame.font.Font = pygame.font.SysFont( "Arial", 10, True )
FONT: tuple[str, int] = ("Arial", 50)
FIELD_EMPTY: list[int, int, int, int, int, int, int, int, int] = [int, int, int, int, int, int, int, int, int]
WINDOW_RESOLUTION: tuple[int, int] = (BOARD_RESOLUTION[0], BOARD_RESOLUTION[1] + BOARD_RESOLUTION[1] // 4)
