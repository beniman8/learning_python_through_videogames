import pygame
from os.path import join
from random import randint, uniform

# general setup
pygame.init()
pygame.display.set_caption("Space Shooter")
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
FRAME_RATE = 60
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CENTER_OF_THE_WINDOW = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
clock = pygame.time.Clock()
running = True
NUMBER_OF_STARS = 100


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(join("images", "player.png")).convert_alpha()
        self.rect = self.image.get_frect(center=CENTER_OF_THE_WINDOW)
        self.direction = pygame.math.Vector2()
        self.speed = 300

        # cooldown timer
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 400

    def laser_timer(self) -> None:
        ''' A timer for when the laser can shoot'''
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True

    def update(self, dt):
        keys = pygame.key.get_pressed()

        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = (
            self.direction.normalize() if self.direction else self.direction
        )
        self.rect.center += self.direction * self.speed * dt

        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            Laser(laser_surface, self.rect.midtop, (all_sprites,laser_sprites))
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()

        self.laser_timer()


class Laser(pygame.sprite.Sprite):
    def __init__(self, surf: pygame.Surface, pos: tuple, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom=pos)
        self.speed = 400

    def update(self, dt):
        self.rect.centery -= self.speed * dt
        if self.rect.bottom < 0:
            self.kill()


class Star(pygame.sprite.Sprite):

    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(
            center=(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT))
        )


class Meteor(pygame.sprite.Sprite):

    def __init__(self, surf: pygame.Surface, pos: tuple, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center=pos)
        self.speed = randint(400, 500)
        self.life_duration = 3000
        self.start_time = pygame.time.get_ticks()
        self.direction = pygame.Vector2(uniform(-0.5, 0.5), 1)

    def update(self, *args):

        self.rect.center += self.direction * self.speed * args[0]
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time >= self.life_duration:
            self.kill()


def collision():
    
    global running
    #collision 
    player_meteor_collision =pygame.sprite.spritecollide(player,meteor_sprites,True)
    if player_meteor_collision:
        running=False
        print('collided')
    for laser in laser_sprites:
        collided_sprites=pygame.sprite.spritecollide(laser,meteor_sprites,True)
        if collided_sprites:
            laser.kill()
    

# game imports
star_surf = pygame.image.load(join("images", "star.png")).convert_alpha()
meteor_surface = pygame.image.load(join("images", "meteor.png")).convert_alpha()
laser_surface = pygame.image.load(join("images", "laser.png")).convert_alpha()

# creating sprite
all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()

for i in range(NUMBER_OF_STARS):
    Star(all_sprites, star_surf)
player = Player(all_sprites)

# custom event -> meteor event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)


while running:
    dt = clock.tick(FRAME_RATE) / 1000
    # Event loop
    for event in pygame.event.get():
        # inside this loop we can check for keyboard input mouse input and more.
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            x, y = randint(0, WINDOW_WIDTH), 0
            meteor = Meteor(meteor_surface, (x, y), (all_sprites, meteor_sprites))
    # update the game
    all_sprites.update(dt)
    
    collision()
    
    # Draw the game
    # display the background
    display_surface.fill("darkgray")
    # draw the sprite at a certain target for us its the display_surface
    all_sprites.draw(display_surface)


    pygame.display.update()


pygame.quit()
