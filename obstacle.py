import pygame

class Obstacle(pygame.Rect):
    # Obstacle is subclass of Rect- keeps track of own location,
    # is able to draw itself, and return the vertices that will
    # need to be included in a graph

    # Space to keep clear of paths around the obstacle
    openBuffer = 3

    def draw(self, screen):
        pygame.draw.rect(screen, (0,0,0), self)

    def getVertices(self):
        inflated = self.inflate(Obstacle.openBuffer + 1, Obstacle.openBuffer + 1)
        return [inflated.topleft,
                inflated.topright,
                inflated.bottomleft,
                inflated.bottomright]

    def collideLine(self, start, end):
        # Checks to see if a line from start tuple to finish tuple
        # collides with this rect. Assume that the line to test isn't
        # entirely in the obstacle, so just check if it intersects
        # any boundaries.
        return False
