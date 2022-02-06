from operator import truediv
import pygame, sys
clock = pygame.time.Clock()

from pygame.locals import *
pygame.init() 
pygame.display.set_caption('Game')
WINDOW_SIZE = (1024,768)
screen = pygame.display.set_mode(WINDOW_SIZE,0,32)
player_image = pygame.image.load('groy.png')


moving_right = False
moving_left = False

player_location = [50,50]
player_y = 0


while True:
    screen.fill((146,244,255))
    screen.blit(player_image,player_location)
   
   
    if player_location[1] > WINDOW_SIZE[1]-player_image.get_height():
        player_y = -player_y
    else: 
        player_y += 0.2
    player_location[1] += player_y
   
   
   
   
   
   
   
   
   
   
    if moving_right == True:
        player_location[0] += 4
    if moving_left == True:
        player_location[0] -= 4



    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False
            



    pygame.display.update()
    clock.tick(60)