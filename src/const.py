# TILE_SIZE: int = 128
TILE_SIZE: int = 96
# RATIO: tuple[int, int] = (3, 3)
RATIO: tuple[int, int] = (4, 4)
BOARD_RESOLUTION: tuple[int, int] = (400, 400)
BOARD_COLOR_A: tuple[int, int, int] = (0, 0, 0)
BOARD_COLOR_B: tuple[int, int, int] = (255, 255, 255)
# PLAYER_COLOR_A: tuple[int, int, int] = (91, 92, 91)
# PLAYER_COLOR_B: tuple[int, int, int] = (179, 181, 180)
PLAYER_COLOR_A: tuple[int, int, int] = (247, 106, 231)
PLAYER_COLOR_B: tuple[int, int, int] = (52, 229, 235)
FONT: tuple[str, int] = ("Arial", 50)
WINDOW_RESOLUTION: tuple[int, int] = (BOARD_RESOLUTION[0], BOARD_RESOLUTION[1] + BOARD_RESOLUTION[1] // 4)
WHITE: str = 'Blue'
BLACK: str = 'Pink'
# FIELD_EMPTY: list = [0, -1, -1, 0, 0, 0, 1, 1, 0]
FIELD_EMPTY: list = [-1, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1]
MATRIX_POS: int = RATIO[1]-1
MATRIX_RAT: int = (RATIO[1]-1)*2 + 1
ATTACK:str = 'attack'
MOVE: str = 'move'
EMPTY: int = 0
PAWN: int = 1
KNIGHT: int = 2

PAWN_MOV: list = []
for y in range(MATRIX_RAT):
    for x in range(MATRIX_RAT):
        if (y-MATRIX_POS == -1) and x == MATRIX_POS:
            PAWN_MOV.append(0)
        else:
            PAWN_MOV.append(1)

PAWN_ATK: list = []
for y in range(MATRIX_RAT):
    for x in range(MATRIX_RAT):
        if (y-MATRIX_POS == -1) and ((x-MATRIX_POS == -1) or (x-MATRIX_POS == 1)):
            PAWN_ATK.append(1)
        else:
            PAWN_ATK.append(0)

KNIGHT_MOV: list = []
KNIGHT_ATK: list = []
for y in range(MATRIX_RAT):
    for x in range(MATRIX_RAT):
        if (abs(y-MATRIX_POS) == 2 and abs(x-MATRIX_POS) == 1) or (abs(y-MATRIX_POS) == 1 and abs(x-MATRIX_POS) == 2):
            KNIGHT_MOV.append(0)
            KNIGHT_ATK.append(1)
        else:
            KNIGHT_MOV.append(1)
            KNIGHT_ATK.append(0)
