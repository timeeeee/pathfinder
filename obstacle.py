import pygame

class Obstacle(pygame.Rect):
    # Obstacle is subclass of Rect- keeps track of own location,
    # is able to draw itself, and return the vertices that will
    # need to be included in a graph
    def draw(self, screen):
        pygame.draw.rect(screen, (0,0,0), self)

    def getVertices(self):
        inflated = self.inflate(5)
        return [inflated.topleft,
                inflated.topright,
                inflated.bottomleft,
                inflated.bottomright]
