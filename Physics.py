import Constants as CONST
import pygame as pg
import math

#Here the Physics of Player and Ray are implemented

def Movement(player):
    forward = True
    # User Input
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]: player.player_angle -= 0.1
    if keys[pg.K_RIGHT]: player.player_angle += 0.1
    if keys[pg.K_UP]:
        forward = True
        player.player_x += -math.sin(player.player_angle) * 5
        player.player_y += math.cos(player.player_angle) * 5
    if keys[pg.K_DOWN]:
        forward = False
        player.player_x -= -math.sin(player.player_angle) * 5
        player.player_y -= math.cos(player.player_angle) * 5

    return forward

def checkCollision(forward,player):
    col = int(player.player_x / CONST.TILE_SIZE)
    row = int(player.player_y / CONST.TILE_SIZE)
    square = row * CONST.MAP_SIZE + col
    if CONST.MAP[square] == '#':
        if forward:
            player.player_x -= -math.sin(player.player_angle) * 10
            player.player_y -= math.cos(player.player_angle) * 10
        else:
            player.player_x += -math.sin(player.player_angle) * 10
            player.player_y += math.cos(player.player_angle) * 10

def cast_rays(win,player):
    start_angle = player.player_angle - CONST.HALF_FOV
    counter = 0
    for ray in range(CONST.CASTED_RAYS):
        for depth in range(CONST.MAX_DEPTH):
            target_x = player.player_x - math.sin(start_angle) * depth
            target_y = player.player_y + math.cos(start_angle) * depth
            
            col = int(target_x / CONST.TILE_SIZE)
            row = int(target_y / CONST.TILE_SIZE)
            square = row * CONST.MAP_SIZE + col

            if CONST.MAP[square] == '#':
                pg.draw.rect(win, CONST.WALL_LIT, (col * CONST.TILE_SIZE,
                                                    row * CONST.TILE_SIZE,
                                                    CONST.TILE_SIZE - 2,
                                                    CONST.TILE_SIZE - 2))
                if counter == 0:
                    pg.draw.line(win, CONST.RAYS, (player.player_x, player.player_y), (target_x, target_y),3)
                counter += 1
                redFactor = 200 / (1 + depth * depth * 0.0001)
                blueFactor = 70 / (1 + depth * depth * 0.0001)
                greenFactor = 72 / (1 + depth * depth * 0.0001)

                depth *= math.cos(player.player_angle - start_angle)
                                
                wall_height = 21000 / (depth + 0.0001)
                
                if wall_height > CONST.SCREEN_HEIGHT: wall_height = CONST.SCREEN_HEIGHT 
                
                pg.draw.rect(win, (redFactor, greenFactor, blueFactor), (
                    CONST.SCREEN_HEIGHT + ray * CONST.SCALE,
                    (CONST.SCREEN_HEIGHT / 2) - wall_height / 2,
                     CONST.SCALE,
                      wall_height))
                break

        start_angle += CONST.STEP_ANGLE
#EOF
