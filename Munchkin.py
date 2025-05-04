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

font = pygame.font.Font('freesansbold.ttf', 32)

text = font.render('There is a door in front of you \n Press enter to kick it down',True, GREEN, BLUE)

textRect = text.get_rect()

textRect.center =  (WIDTH // 2, HEIGHT // 2)

#game loop
running = True


def draw():
    screen.fill(BLACK)
    screen.blit(text, textRect)
    # all_sprites.draw(screen)
    # after drawing everything
    pygame.display.flip()


def update():
    global running
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

    # Draw / render
    draw()

pygame.quit()