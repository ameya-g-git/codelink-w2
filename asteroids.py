import pygame as py
import math

# Pygame setup
py.init()
py.display.set_caption("Asteroids")
clock = py.time.Clock()

# Screen Setup
w, h = 1200, 800
screen = py.display.set_mode((w, h))

# Movement & Speed
x, y = 400, 400
x_speed, y_speed = 0, 0
vel = 0
acceleration = 0.005  # Rate of acceleration increase
arrow_angle = 0
deceleration = 0.98  # Adjust the deceleration rate as needed

# Colours
white = (242,242,242)
black = (17,17,17)

run_program = True
while run_program:
    screen.fill(black)

    for event in py.event.get():
        if event.type == py.QUIT:
            run_program = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                run_program = False

    surface = py.Surface((50, 50))
    surface.fill((255,255,255))

    rotated_surface = py.transform.rotate(surface, arrow_angle)
    rotated_rect = rotated_surface.get_rect(center = (x, y))
    screen.blit(rotated_surface, (rotated_rect))

    py.display.update()
    clock.tick(100)

py.quit()