import pygame

TILE_SIZE: int = 128
RATIO: tuple[int, int] = (3, 3) # for chess board pattern -> only uneven numbers possible
BOARD_RESOLUTION: int = 400
BOARD_COLOR_A: tuple[int, int, int] = (0, 0, 0)
BOARD_COLOR_B: tuple[int, int, int] = (255, 255, 255)
FONT: pygame.font.Font = pygame.font.SysFont( "Arial", 10 )
FIELD_EMPTY: list[int, int, int, int, int, int, int, int, int] = [int, int, int, int, int, int, int, int, int]
