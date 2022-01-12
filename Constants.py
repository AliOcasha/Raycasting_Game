import math

SCREEN_HEIGHT = 480
SCREEN_WIDTH = SCREEN_HEIGHT * 2
MAP_SIZE = 8
TILE_SIZE = int((SCREEN_WIDTH / 2) / MAP_SIZE)
MAX_DEPTH = int(MAP_SIZE * TILE_SIZE)
FOV = math.pi / 3
HALF_FOV = FOV / 2
CASTED_RAYS = 120
STEP_ANGLE = FOV / CASTED_RAYS
SCALE = (SCREEN_WIDTH / 2) / CASTED_RAYS

FLOOR = (50, 50, 50)
WALL_UNLIT = (230,230,230)
WALL_LIT = (100,100,100)
RAYS = (255, 255, 255)

RED = (255, 0, 0)
BLACK = (0, 0, 0)

FLOOR_3D = (100, 100, 100)
SKY = (200,200,200)

MAP = (
    '########'
    '# #    #'
    '# # ####'
    '# #    #'
    '#      #'
    '#  ### #'
    '#      #'
    '########'
)