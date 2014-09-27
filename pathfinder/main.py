import pygame
from pygame.locals import *
from character import Character

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    character = Character()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT: return
            elif event.type == KEYDOWN && event.key == K_ESCAPE: return
        screen.fill((0, 255, 0))
        pygame.display.flip()

if __name__ == "__main__": main()
