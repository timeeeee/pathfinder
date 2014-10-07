import pygame
from pygame.locals import *
from character import Character
from obstacle import Obstacle

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    screen.fill((255, 255, 255))
    clock = pygame.time.Clock()

    character = Character((100, 100))
    obstacles = [Obstacle(200, 200, 100, 100),
                 Obstacle(500, 300, 50, 50),
                 Obstacle(50, 275, 50, 50),
                 Obstacle(400, 50, 100, 100)]
    
    while True:
        dTime = clock.tick()
        for event in pygame.event.get():
            if event.type == QUIT: return
            elif event.type == KEYDOWN and event.key == K_ESCAPE: return
            elif event.type == MOUSEBUTTONUP and event.button == 1:
                character.goTo(event.pos, obstacles)
            elif event.type == KEYDOWN and event.key == K_UP: character.accelerateUp()
            elif event.type == KEYDOWN and event.key == K_DOWN: character.accelerateDown()
            elif event.type == KEYDOWN and event.key == K_LEFT: character.accelerateLeft()
            elif event.type == KEYDOWN and event.key == K_RIGHT: character.accelerateRight()
            elif event.type == KEYUP and event.key == K_UP: character.accelerateDown()
            elif event.type == KEYUP and event.key == K_DOWN: character.accelerateUp()
            elif event.type == KEYUP and event.key == K_RIGHT: character.accelerateLeft()
            elif event.type == KEYUP and event.key == K_LEFT: character.accelerateRight()
        character.update(dTime, obstacles)
        screen.fill((255, 255, 255))
        for obstacle in obstacles: obstacle.draw(screen)
        character.draw(screen)
        pygame.display.flip()

if __name__ == "__main__": main()
