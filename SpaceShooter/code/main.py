import pygame
from os.path import join
from random import randint

# general setup
pygame.init()
pygame.display.set_caption("Space Shooter")
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CENTER_OF_THE_WINDOW = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

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
PLAYER_DIRECTION = 1
PLAYER_SPEED = 0.4

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
    # Event loop
    for event in pygame.event.get():
        # inside this loop we can check for keyboard input mouse input and more.
        if event.type == pygame.QUIT:
            running = False

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
    player_rect.x += PLAYER_DIRECTION * PLAYER_SPEED

    # if the right side of the rectangle is greater than the window's width
    # or if the left side of the rectangle is smaller than zero or the beginning of the windows width
    # reverse the direction by multiplying it by negative one
    if player_rect.right > WINDOW_WIDTH or player_rect.left < 0:
        PLAYER_DIRECTION *= -1

    # display the ship or player
    display_surface.blit(player_surf, player_rect)

    pygame.display.update()  # update the whole window
    # pygame.display.flip()()# update part of the window


pygame.quit()
