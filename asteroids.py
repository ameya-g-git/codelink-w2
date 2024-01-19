import pygame as py
import math

# Pygame setup
py.init()
py.display.set_caption("Asteroids")
clock = py.time.Clock()

# Screen Setup
w, h = 1200, 800
screen = py.display.set_mode((w, h))

# Colours
white = (255,255,255)
black = (17,17,17)

# Movement & Speed
x, y = 400, 400
x_speed, y_speed = 0, 0
vel = 0
acceleration = 0.005  # Rate of acceleration increase
angle = 0 # Rotation of the sprite
deceleration = 0.98  # Adjust the deceleration rate as needed

run_program = True

# Game Loop
while run_program:
    screen.fill(black)

    # Event Listener
    for event in py.event.get(): 
        if event.type == py.QUIT:
            run_program = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                run_program = False

    # Sprite
    square = py.Surface((50, 50))
    square.fill(white)

    # Rotation Code (we'll worry about this in a bit!)
    rotated_surface = py.transform.rotate(square, angle)
    rotated_rect = rotated_surface.get_rect(center = (x, y))
    screen.blit(rotated_surface, rotated_rect)

    # Update Surface
    py.display.update()
    clock.tick(100)

py.quit()