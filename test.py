#!/usr/bin/env python3
# -*- coding: iso-8859-15 -*-

import numpy as np
from libspring import *
import sys
import pygame
from pygame.locals import *
#from pygame.color import THECOLORS as COLORS
#from os import system
#clear = lambda: system('clear')


width, height = 700, 700
pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))

# Objects
mouse_obj = Object()
mass_obj = Object(pos=np.array([width/2, height/2]), mass=1)
spring = Spring(obj1=mouse_obj, obj2=mass_obj, L0=50, k=100)

# Mouse pos
pygame.mouse.set_pos([width//2, height//2-50])

# Game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
            break

    # Mechanism
    x, y = pygame.mouse.get_pos()
    mouse_obj.pos = np.array([x,y])
    F1, F2 = spring.forces()
    mass_obj.add_force(F1)
    mass_obj.add_force(np.array([0,10000]))
    mass_obj.move(dt=0.01)

    # Reset screen
    screen.fill([0,0,0])

    # Draw
    pygame.draw.circle(screen, [0,100,255], mouse_obj.pos.astype(int), 10)
    pygame.draw.circle(screen, [255,0,0], mass_obj.pos.astype(int), 10)
    pygame.draw.line(
        screen, [255,255,255],
        spring.obj1.pos.astype(int),
        spring.obj2.pos.astype(int),
        width=3
    )

    # Update
    pygame.display.flip()
    fpsClock.tick(fps)

pygame.quit()
