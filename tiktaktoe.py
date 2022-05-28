"""this project is a game
project"""

import pygame
from pygame import time
from pygame.locals import *

import sys

pygame.init()
screen = pygame.display.set_mode([600,600])

pygame.display.set_caption("TIK-TAC-TOE")
#Startmenu

# Design Menu
# create font, texts for start menu
screen.fill((188, 238, 104))

fontStartmenu = pygame.font.SysFont("chalkduster.ttf", 75)
img_Play = fontStartmenu.render('PLAY', True, (0, 0, 0))
rect = img_Play.get_rect()
pygame.draw.rect(img_Play, (0, 0, 0), rect, 3)
screen.blit(img_Play, (200, 100))

img_Option = fontStartmenu.render('OPTION', True, (0, 0, 0))
rect = img_Option.get_rect()
pygame.draw.rect(img_Option, (0, 0, 0), rect, 3)
screen.blit(img_Option, (200, 200))

img_Credits = fontStartmenu.render('CREDITS', True, (0, 0, 0))
rect = img_Credits.get_rect()
pygame.draw.rect(img_Credits, (0, 0, 0), rect, 3)
screen.blit(img_Credits, (200, 300))

img_PlayRules = fontStartmenu.render('PLAY RULES', True, (0, 0, 0))
rect = img_PlayRules.get_rect()
pygame.draw.rect(img_PlayRules, (0, 0, 0), rect, 3)
screen.blit(img_PlayRules, (200, 400))

pygame.display.update()

# running menu until player quit
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False


