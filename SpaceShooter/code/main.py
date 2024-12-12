import pygame

# general setup
pygame.init()
pygame.display.set_caption('Space Shooter')
WINDOW_WIDTH,WINDOW_HEIGHT = 1280,720
display_surface= pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

running= True

#surface 
surface = pygame.Surface((100,200))

while running:
    # Event loop 
    for event in pygame.event.get():
        #inside this loop we can check for keyboard input mouse input and more.
        if event.type == pygame.QUIT:
            running =False
        
    # Draw the game
    
    
    display_surface.fill('darkgray')
    display_surface.blit(surface,(100,150))
    pygame.display.update()# update the whole window
    # pygame.display.flip()()# update part of the window
    
    
pygame.quit()