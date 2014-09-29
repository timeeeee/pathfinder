import pygame
from pygame.locals import *
from character import Character

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    screen.fill((255, 255, 255))
    character = Character((100, 100))
    clock = pygame.time.Clock()
    
    while True:
        dTime = clock.tick()
        for event in pygame.event.get():
            if event.type == QUIT: return
            elif event.type == KEYDOWN and event.key == K_ESCAPE: return
            elif event.type == MOUSEBUTTONUP and event.button == 1:
                character.goTo(event.pos, [])
        character.update(dTime)
        screen.fill((255, 255, 255))
        character.draw(screen)
        pygame.display.flip()

if __name__ == "__main__": main()
