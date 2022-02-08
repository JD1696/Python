from multiprocessing.connection import wait
from operator import truediv
import pygame, sys

clock = pygame.time.Clock()

from pygame.locals import *

pygame.init()
pygame.display.set_caption("Game")
WINDOW_SIZE = (1024, 768)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
G = 0
fram1 = "anim/Sprite-0001.png"
fram2 = "anim/Sprite-0002.png"
fram3 = "anim/Sprite-0003.png"
sprite_frams = [fram1, fram2, fram3]
player_image = pygame.image.load(sprite_frams[G])


jumped = False
moving_right = False
moving_left = False
xval = 0
yval = 0
player_location = [50, 50]
gravity = True

anim = True
frames = 0


def moveFunction():
    player_location[0] += xval
    player_location[1] += yval


while True:
    screen.fill((146, 244, 255))
    screen.blit(player_image, player_location)

    # Bouncy walls

    if (
        player_location[1] > WINDOW_SIZE[1] - player_image.get_height()
        and gravity == True
    ):
        yval -= yval
        xval = 0
    if player_location[1] < 0:
        print(yval)
        yval = (yval) * -1
    if player_location[0] > WINDOW_SIZE[0] - player_image.get_width():
        xval = (xval) * -1
    if player_location[0] < 0:
        xval = (xval) * -1

    ############################################################

    moveFunction()

    if xval > 0:
        xval -= 0.05

    if xval < 0:
        xval += 0.05

    if moving_right == True:
        xval += 0.2

    if moving_left == True:
        xval -= 0.2

    if jumped == True:
        yval -= 0.2
        gravity = False

    if jumped == False:
        gravity = True

    if gravity == True:
        yval += 0.2

    if fcount == 1:
        player_image = pygame.image.load(sprite_frams[1])
    if fcount == 2:
        player_image = pygame.image.load(sprite_frams[2])

    if anim == True:
        player_image = pygame.image.load(sprite_frams[G])

    ####### inputs ###########

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_UP:
                jumped = True

            if event.key == K_LEFT:
                moving_left = True
        if event.type == KEYUP:
            if event.key == K_UP:
                jumped = False
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False
        if event.type == MOUSEBUTTONDOWN:
            if G < 2:
                G += 1
            else:
                G = 0

            print("woo")

    pygame.display.update()
    clock.tick(60)
