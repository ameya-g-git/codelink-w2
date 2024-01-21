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
sprite_w, sprite_h = 50, 50
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

    keys = py.key.get_pressed()

    if keys[py.K_a]:
        angle += 3
    
    elif keys[py.K_d]:
        angle -= 3

    if keys[py.K_w]:
        if x_speed > -9 or y_speed > -9:
            x_speed += vel
            y_speed += vel
            vel += acceleration

    elif keys[py.K_s]:
        if x_speed < 9 or y_speed < 9:
            x_speed += vel
            y_speed += vel
            vel += acceleration
    else:
        vel = 0 
        x_speed *= deceleration
        y_speed *= deceleration
        if -0.3 < x_speed < 0.3 or -0.3 < y_speed < 0.3:
            x_speed = 0
            y_speed = 0

    if x < -sprite_w:
        x = w + sprite_w
    if x > w + sprite_w:
        x = -sprite_w
    if y < -sprite_h:
        y = h + sprite_h
    if y > h + sprite_h:
        y = -sprite_h

    angle_in_radians = math.radians(angle)
    x += x_speed * math.sin(angle_in_radians)
    y += y_speed * math.cos(angle_in_radians)

    # Sprite
    square = py.Surface((sprite_w, sprite_h))
    square.fill(white)

    # Rotation Code (we'll worry about this in a bit!)
    rotated_surface = py.transform.rotate(square, angle)
    rotated_rect = rotated_surface.get_rect(center = (x, y))
    screen.blit(rotated_surface, (rotated_rect))

    # Update Surface
    py.display.update()
    clock.tick(100)

py.quit()