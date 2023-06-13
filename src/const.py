TILE_SIZE: int = 128
RATIO: tuple[int, int] = (3, 3) # for chess board pattern -> only uneven numbers possible
BOARD_RESOLUTION: tuple[int, int] = (400, 400)
BOARD_COLOR_A: tuple[int, int, int] = (0, 0, 0)
BOARD_COLOR_B: tuple[int, int, int] = (255, 255, 255)
FONT: tuple[str, int] = ("Arial", 50)
WINDOW_RESOLUTION: tuple[int, int] = (BOARD_RESOLUTION[0], BOARD_RESOLUTION[1] + BOARD_RESOLUTION[1] // 4)
FIELD_EMPTY: list[int, ...] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
MATRIX_POS = RATIO[1]-1
MATRIX_RAT = (RATIO[1]-1)*2 + 1
ATTACK = 'attack'
MOVE = 'move'
EMPTY: int = 0
PAWN: int = 1

# bitte noch kommentieren (also vielleicht ... oder lieber nicht um VIncent leiden zu sehen)
PAWN_MOV = []
for y in range(MATRIX_RAT):
    for x in range(MATRIX_RAT):
        # Wenn der Bauer 2 vorgehen kann: if (y-MATRIX_POS == -2 or y-MATRIX_POS == -1) and x == MATRIX_POS:
        if (y-MATRIX_POS == -1) and x == MATRIX_POS:
            PAWN_MOV.append(0)
        else:
            PAWN_MOV.append(1)
print(PAWN_MOV)

PAWN_ATK = []
for y in range(MATRIX_RAT):
    for x in range(MATRIX_RAT):
        if (y-MATRIX_POS == -1) and ((x-MATRIX_POS == -1) or (x-MATRIX_POS == 1)):
            PAWN_ATK.append(1)
        else:
            PAWN_ATK.append(0)
print(PAWN_ATK)

