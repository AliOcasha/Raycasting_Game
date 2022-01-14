import math

SCREEN_HEIGHT = 480
SCREEN_WIDTH = SCREEN_HEIGHT * 2
MAP_SIZE = 8
TILE_SIZE = int((SCREEN_WIDTH / 2) / MAP_SIZE)
MAX_DEPTH = int(MAP_SIZE * TILE_SIZE)
FOV = math.pi / 2.5
HALF_FOV = FOV / 2
CASTED_RAYS = 160
STEP_ANGLE = FOV / CASTED_RAYS
SCALE = (SCREEN_WIDTH / 2) / CASTED_RAYS

FLOOR = (129, 132, 121)
WALL_LIT = (200,70,72)
WALL_UNLIT = (170,40,42)
RAYS = (255, 255, 255)

RED = (255, 255, 0)
BLACK = (0, 0, 0)

SKY = (0,136,255)

MAP = (
    '########'
    '# #    #'
    '# # ####'
    '# #  # #'
    '#      #'
    '#  ### #'
    '#      #'
    '########'
)