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
NUMBER_OF_STARS=100


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(join("images", "player.png")).convert_alpha()
        self.rect = self.image.get_frect(center=CENTER_OF_THE_WINDOW)
        self.direction = pygame.math.Vector2()
        self.speed = 300

    def update(self, dt):
        keys = pygame.key.get_pressed()

        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt
        
        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE]:
            print('Fire Laser')

class Star(pygame.sprite.Sprite):
    
    def __init__(self, groups,surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center=(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))
        


        


# plain surface
surface = pygame.Surface((100, 200))
surface.fill("blue")
x, y = 100, 150


all_sprites = pygame.sprite.Group()

star_surf = pygame.image.load(join("images", "star.png")).convert_alpha()
for i in range(NUMBER_OF_STARS):
    Star(all_sprites,star_surf)
player = Player(all_sprites)

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

    all_sprites.update(dt)
    # Draw the game
    # display the background
    display_surface.fill("darkgray")
    # draw the sprite at a certain target for us its the display_surface
    all_sprites.draw(display_surface)
    
    pygame.display.update() 



pygame.quit()
