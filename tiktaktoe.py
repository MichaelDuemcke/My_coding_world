"""this project is a game
project"""
import pygame
import pygame_menu
from pygame.locals import *

import sys

# define functions for menu switching
def start_the_game():
    print("Here will come the text for the game tetris!")




pygame.init()


screen = pygame.display.set_mode([600, 600])
pygame.display.set_caption("TIK-TAC-TOE")

# Design Menu
# create font, texts for start menu
# interactive menu buttons

menu = pygame_menu.Menu('TIC-TAC-TOE (Python-Edition)', 600, 600,
                        theme=pygame_menu.themes.THEME_BLUE)

menu.add.button('Play', start_the_game)
menu.add.button('OPTION', start_the_game)
menu.add.button('CREDITS', start_the_game)
menu.add.button('RULES', start_the_game)
menu.add.button('QUIT', pygame_menu.events.EXIT)
menu.mainloop(screen)
pygame.display.update()
# running menu until player quit
running = True
while menu == True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
