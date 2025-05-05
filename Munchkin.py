import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 30

# define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My game')
clock = pygame.time.Clock()

# creating the monster class
class Door(pygame.sprite.Sprite):
    def __init__(self):
        print('Door class created')

class Monster(pygame.sprite.Sprite):
    def __init__(self, name, pwr_lvl, image_path, pos=(WIDTH // 2, HEIGHT // 2)):
        super().__init__()
        self.name = name
        self.level = pwr_lvl

        try:
            self.image = pygame.image.load(image_path).convert_alpha()
        except pygame.error():
            print(f'image failed to load: {image_path}')
            self.image = pygame.Surface((50,50))
            self.image.fill((225, 0, 0))
        self.rect = self.image.get_rect(topleft=pos)





font = pygame.font.Font('freesansbold.ttf', 20)

message = 'There is a door in front of you, Press enter to kick it down'

#game loop
running = True


def draw():
    screen.fill(BLACK)

    text = font.render(message, True, GREEN, BLACK)

    textRect = text.get_rect()

    textRect.center = (WIDTH // 2, HEIGHT // 2)

    screen.blit(text, textRect)

    # all_sprites.draw(screen)
    # after drawing everything
    pygame.display.flip()

# how a game works.
# [Door] kick down the door
# [Encounter] get a door card
    # a monster
        # run away
        # fight
            # ask for help
            # win - get loot
            # lose - something bad
    # not a monster
        # curse
        # something else
        # loot the room -free loot
# [Trade] trade
# [Sell] sell stuff?
# [Charity] give stuff away

# loot cards
    #gear treasure etc
# door cards
    # monsters curses race etc


# homework
    # make it go through all the phases of a turn for a 1 player game
    # show monster
    # give options
    # auto win fight
    # get loot
    # level up

def update():
    global running
    global message
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_RETURN]:
        message = 'boop'
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
    # Update
    # all_sprites.update()


while running:

    update()

    draw()

pygame.quit()