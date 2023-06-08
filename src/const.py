TILE_SIZE: int = 128
RATIO: tuple[int, int] = (3, 3) # for chess board pattern -> only uneven numbers possible
BOARD_RESOLUTION: tuple[int, int] = (400, 400)
BOARD_COLOR_A: tuple[int, int, int] = (0, 0, 0)
BOARD_COLOR_B: tuple[int, int, int] = (255, 255, 255)
FONT: tuple[str, int] = ("Arial", 50)
WINDOW_RESOLUTION: tuple[int, int] = (BOARD_RESOLUTION[0], BOARD_RESOLUTION[1] + BOARD_RESOLUTION[1] // 4)
FIELD_EMPTY: list[int, ...] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
EMPTY: int = 0
PAWN: int = 1

# bitte noch kommentieren (also vielleicht ... oder lieber nicht um VIncent leiden zu sehen)
PAWN_MOV = []
p = [(RATIO[1]-1), (RATIO[1]-1)]
for y in range((RATIO[1]-1)*2 + 1):
    for x in range((RATIO[1]-1)*2 + 1):
        if (y-p[1] == -2 or y-p[1] == -1) and x == p[1]:
            PAWN_MOV.append(0)
        else:
            PAWN_MOV.append(1)

PAWN_ATK = []
p = [(RATIO[1]-1), (RATIO[1]-1)]
for y in range((RATIO[1]-1)*2 + 1):
    for x in range((RATIO[1]-1)*2 + 1):
        if (y-p[1] == -1) and ((x-p[1] == -1) or (x-p[1] == 1)):
            PAWN_ATK.append(1)
        else:
            PAWN_ATK.append(0)
print(PAWN_ATK)

# MOV
# 1, 1, 0, 1, 1, 
# 1, 1, 0, 1, 1, 
# 1, 1, 1, 1, 1, 
# 1, 1, 1, 1, 1, 
# 1, 1, 1, 1, 1

# Test
# 0, 0, 0, 
# 0, 0, 0, 
# 1, 0, 0

p = [2,2]
n = 12



# ATK
# 0, 0, 0, 0, 0, 
# 0, 1, 0, 1, 0, 
# 0, 0, 0, 0, 0, 
# 0, 0, 0, 0, 0, 
# 0, 0, 0, 0, 0
