#!/usr/bin/env python3
# -*- coding: iso-8859-15 -*-

import numpy as np
from libspring import *
import sys
import pygame
from pygame.locals import *


width, height = 700, 700
pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))

# Objects
obj1 = Object(pos=np.array([300, 300]), mass=50, color=[255,0,0])
obj2 = Object(pos=np.array([400, 300]), mass=50, color=[0,255,0])
obj3 = Object(pos=np.array([300, 400]), mass=50, color=[0,0,255])
obj4 = Object(pos=np.array([400, 400]), mass=50, color=[255,0,255])
objects = [obj1, obj2, obj3, obj4]

# Springs
spring1 = Spring(obj1=obj1, obj2=obj2, L0=50, k=5000)
spring2 = Spring(obj1=obj1, obj2=obj3, L0=50, k=5000)
spring3 = Spring(obj1=obj4, obj2=obj2, L0=50, k=5000)
spring4 = Spring(obj1=obj4, obj2=obj3, L0=50, k=5000)
spring5 = Spring(obj1=obj1, obj2=obj4, L0=50, k=5000)
spring6 = Spring(obj1=obj2, obj2=obj3, L0=50, k=5000)
springs = [spring1, spring2, spring3, spring4, spring5, spring6]

# Game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
            break

    # Mechanism
    for spring in springs:
        F1, F2 = spring.forces()
        spring.obj1.add_force(F2)
        spring.obj2.add_force(F1)

    mouse = np.array(pygame.mouse.get_pos())
    d1 = scale(look_at(obj1.pos, mouse), 5000)
    obj1.add_force(d1)
    d4 = scale(look_at(obj4.pos, mouse), -5000)
    obj4.add_force(d4)

    for obj in objects:
        obj.move(dt=0.01)

    # Reset screen
    screen.fill([0,0,0])

    # Draw
    for obj in objects:
        obj.draw(screen)
    for spring in springs:
        spring.draw(screen)

    # Update
    pygame.display.flip()
    fpsClock.tick(fps)

pygame.quit()
