import pygame as pg
import sys
import math

import Draw
import Constants as CONST
import Physics

class Player:
    def __init__(self,player_x,player_y,player_angle):
        self.player_x = player_x
        self.player_y = player_y
        self.player_angle = player_angle
        
# global variables
x = (CONST.SCREEN_WIDTH / 2) / 2
y = (CONST.SCREEN_WIDTH / 2) / 2
angle = math.pi
player = Player(x,y,angle)

# init pygame
pg.init()
win = pg.display.set_mode((CONST.SCREEN_WIDTH, CONST.SCREEN_HEIGHT))
pg.display.set_caption('Raycasting')
clock = pg.time.Clock()

# moving direction
forward = True

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit(0)
    
    #Collision Check
    Physics.checkCollision(forward,player)
    

    Draw.draw(win,player)
    Physics.cast_rays(win,player)
    Physics.Movement(forward,player)

    clock.tick(30)
    Draw.fpsDisplay(clock,win)

    pg.display.flip()