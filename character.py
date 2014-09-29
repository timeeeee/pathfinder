from math import sqrt
import pygame

# this could potentially be a subclass of Sprite

class Character:
    def __init__(self, location):
        self.location = location
        # speed in pixels / second
        self.speed = 400
        self.currentDestination = location
        self.path = []
        print("character created")

    # Create map creates a map based on character and obstacle locations,
    # and destination. Format is:
    # [((vertex1x, vertex1y), [neighbor1index, ...]),
    #  ((vertex2x, vertex2y), [neighbor1index, ...]) ...]
    # or: [(locationTuple, neighborList), ...]
    # first vertex is start location, last vertex is destination
    def generateMap(self, destination, obstacleList):
        # placeholder, return a graph with a single edge from start to destination
        return [(self.location, [1]),
                (destination, [0])]

    # findPath returns list of destinations on the shortest path from
    # first to last vertex of a map.
    def findPath(self, graph):
        # placeholder, currently just returns last vertex
        # so the character will just travel in a straight line
        return graph[-1][0]

    def goTo(self, destination, obstacles):
        self.path = self.findPath(self.generateMap(destination, obstacles))
        self.destination = self.path.pop(0)

    # Move towards closest destination. If already there, continue following self.path
    def update(self, dTime):
        # coordinates are turned into tuples here before comparison, because if they
        # were passed as parameters earlier, they aren't guaranteed to be the same type
        if tuple(self.location) == tuple(self.destination):
            if self.path: self.destination = self.path.pop(0)
        else:
            # move towards destination at self.speed pixels per second
            x, y = self.location
            destinationX, destinationY = self.destination
            vectorX = destinationX - x
            vectorY = destinationY - y
            length = sqrt(vectorX**2 + vectorY**2)
            displacementX = int(vectoryX * dTime / length / 1000)
            displacementY = int(vectoryY * dTime / length / 1000)
            if displacementX > vectorX: 
                self.location = self.destination
            else:
                self.location = (x + displacementX, y + displacementY)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), self.location, width = 4)
