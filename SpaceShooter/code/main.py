import pygame
from os.path import join
from random import randint

# general setup
pygame.init()
pygame.display.set_caption("Space Shooter")
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

running = True

# plain surface
surface = pygame.Surface((100, 200))
surface.fill("blue")
x, y = 100, 150

# import an image as a surface
path = join("images", "player.png")
player_surf = pygame.image.load(path).convert_alpha()

# importing stars
star_path = join("images", "star.png")
star_surf = pygame.image.load(star_path).convert_alpha()
number_of_stars = 50
star_positions = {(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for star in range(number_of_stars)}


while running:
    # Event loop
    for event in pygame.event.get():
        # inside this loop we can check for keyboard input mouse input and more.
        if event.type == pygame.QUIT:
            running = False

    # Draw the game

    #display the background
    display_surface.fill("darkgray")
    x += 0.1
    #display the stars
    for position in star_positions:
        display_surface.blit(star_surf, position)
        
    #display the ship or player    
    # display_surface.blit(surface, (x, y))
    display_surface.blit(player_surf, (x, y))

        
    pygame.display.update()  # update the whole window
    # pygame.display.flip()()# update part of the window


pygame.quit()
