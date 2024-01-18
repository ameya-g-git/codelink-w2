import pygame as py
import math

# Pygame setup
py.init()
py.display.set_caption("Asteroids")
clock = py.time.Clock()

w, h = 1200, 800
counter = 0
screen = py.display.set_mode((w, h))    

run_program = True
while run_program:
    screen.fill((17, 17, 17))

    for event in py.event.get():
        if event.type == py.QUIT:
            run_program = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                run_program = False

py.display.update()
clock.tick(100)

py.quit()