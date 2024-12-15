import pygame
from os.path import join
from random import randint

# general setup
pygame.init()
pygame.display.set_caption("Space Shooter")
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
FRAME_RATE = 60
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CENTER_OF_THE_WINDOW = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
clock = pygame.time.Clock()
running = True

# plain surface
surface = pygame.Surface((100, 200))
surface.fill("blue")
x, y = 100, 150

# import an image as a surface
path = join("images", "player.png")
player_surf = pygame.image.load(path).convert_alpha()
# create a rectangle from the player that can be better manipulated in the game
player_rect = player_surf.get_frect(center=CENTER_OF_THE_WINDOW)
PLAYER_DIRECTION = pygame.math.Vector2(0, 0)
PLAYER_SPEED = 300

# importing stars
star_path = join("images", "star.png")
star_surf = pygame.image.load(star_path).convert_alpha()
number_of_stars = 50
star_positions = {
    (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT))
    for star in range(number_of_stars)
}

# import meteorite
meteor_path = join("images", "meteor.png")
meteor_surface = pygame.image.load(meteor_path).convert_alpha()
meteor_rect = meteor_surface.get_frect(center=CENTER_OF_THE_WINDOW)


# import laser
laser_path = join("images", "laser.png")
laser_surface = pygame.image.load(laser_path).convert_alpha()
laser_rect = laser_surface.get_frect(bottomleft=(20, WINDOW_HEIGHT - 20))

# creating custom rect
# plain_rect = pygame.FRect(left top width height )


while running:
    dt = clock.tick(FRAME_RATE) / 1000
    # Event loop
    for event in pygame.event.get():
        # inside this loop we can check for keyboard input mouse input and more.
        if event.type == pygame.QUIT:
            running = False

        # if event.type == pygame.K:
        #     pass

    # input game control
    keys = pygame.key.get_pressed()

    PLAYER_DIRECTION.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    PLAYER_DIRECTION.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
    PLAYER_DIRECTION = (
        PLAYER_DIRECTION.normalize() if PLAYER_DIRECTION else PLAYER_DIRECTION
    )

    recently_pressed = pygame.key.get_just_pressed()
    if recently_pressed[pygame.K_SPACE]:
        print('Fire Laser')
    # if keys[pygame.K_RIGHT]:
    #     print('right')
    #     PLAYER_DIRECTION.x = 1
    # else:
    #     PLAYER_DIRECTION.x = 0

    # Draw the game
    # display the background
    display_surface.fill("darkgray")
    # display the stars
    for position in star_positions:
        display_surface.blit(star_surf, position)

    # display_surface.blit(surface, (x, y))

    # display meteorite
    display_surface.blit(meteor_surface, meteor_rect)

    # display laser
    display_surface.blit(laser_surface, laser_rect)

    # player movement

    # if player_rect.right >= WINDOW_WIDTH or player_rect.left < 0:
    #     PLAYER_DIRECTION.x *=-1
    # if player_rect.bottom >= WINDOW_HEIGHT or player_rect.top < 0:
    #     PLAYER_DIRECTION.y *=-1

    player_rect.center += PLAYER_DIRECTION * PLAYER_SPEED * dt
    # if the right side of the rectangle is greater than the window's width
    # or if the left side of the rectangle is smaller than zero or the beginning of the windows width
    # reverse the direction by multiplying it by negative one
    # if player_rect.right > WINDOW_WIDTH or player_rect.left < 0:
    #     PLAYER_DIRECTION *= -1

    # display the ship or player
    display_surface.blit(player_surf, player_rect)

    pygame.display.update()  # update the whole window
    # pygame.display.flip()()# update part of the window


pygame.quit()
