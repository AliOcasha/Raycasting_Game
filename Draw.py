import pygame as pg
import Constants as CONST

def draw_map(win,player):
    for row in range(8):
        for col in range(8):
            square = row * CONST.MAP_SIZE + col
            
            pg.draw.rect(
                win,
                CONST.WALL_UNLIT if CONST.MAP[square] == '#' else CONST.FLOOR,
                (col * CONST.TILE_SIZE, row * CONST.TILE_SIZE, CONST.TILE_SIZE - 2, CONST.TILE_SIZE - 2)
            )

    pg.draw.circle(win, CONST.RED, (int(player.player_x), int(player.player_y)), 8)
    
def draw(win,player):
    #Update Draw
    pg.draw.rect(win, CONST.BLACK, (0, 0, CONST.SCREEN_HEIGHT, CONST.SCREEN_HEIGHT))
    pg.draw.rect(win, CONST.FLOOR, (480, CONST.SCREEN_HEIGHT / 2, CONST.SCREEN_HEIGHT, CONST.SCREEN_HEIGHT))
    pg.draw.rect(win, CONST.SKY, (480, -CONST.SCREEN_HEIGHT / 2, CONST.SCREEN_HEIGHT, CONST.SCREEN_HEIGHT))
    draw_map(win,player)

def fpsDisplay(clock,win):
    fps = str(int(clock.get_fps()))
    font = pg.font.SysFont('Monospace Regular', 30)
    fps_surface = font.render(fps, False, (255, 255, 255))
    win.blit(fps_surface, (480, 0))  