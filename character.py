import pygame
from node import Node
from math import sqrt
from itertools import combinations

class Character:
    def __init__(self, location):
        self.location = location
        # speed in pixels / second
        self.speed = 400
        self.destination = location
        self.path = []

    # Create map creates a map based on character and obstacle locations,
    # and destination. Format is:
    # [((vertex1x, vertex1y), [neighbor1index, ...]),
    #  ((vertex2x, vertex2y), [neighbor1index, ...]) ...]
    # or: [(locationTuple, neighborList), ...]
    # first vertex is start location, last vertex is destination
    def generateMap(self, destination, obstacleList):
        # placeholder, return a graph with a single edge from start to destination
        vertices = [self.location] + sum([obstacle.getVertices() for obstacle in obstacleList], []) + [self.destination]
        nodes = []
        for index in range(len(vertices)):
            neighbors = range(len(vertices))
            neighbors.remove(index)
            nodes.append(Node(vertices[index], neighbors))
        return nodes

    # findPath returns list of destinations on the shortest path from
    # first to last vertex of a map.
    def findPath(self, graph):
        # placeholder, currently just returns list of last vertex
        # so the character will just travel in a straight line
        return [(100,100)]

    def goTo(self, destination, obstacles):
        self.path = self.findPath(self.generateMap(destination, obstacles))
        self.destination = self.path.pop(0)

    def update(self, dTime):
        # Move towards closest destination. If already there, continue following self.path
        x, y = self.location
        destinationX, destinationY = self.destination
        # We could say "self.location == self.destination" except self.location is probably floats
        if (x - destinationX)**2 + (y - destinationY)**2 < 2:
            if self.path: self.destination = self.path.pop(0)
        else:
            # move towards destination at self.speed pixels per second
            vectorX = destinationX - x
            vectorY = destinationY - y
            length = sqrt(vectorX**2 + vectorY**2)
            displacementX = vectorX * self.speed * dTime / length / 1000
            displacementY = vectorY * self.speed * dTime / length / 1000
            if abs(displacementX) > abs(vectorX):
                self.location = self.destination
            else:
                self.location = (x + displacementX, y + displacementY)

    def draw(self, screen):
        # x and y are probably floats
        x, y = self.location
        pygame.draw.circle(screen, (255, 0, 0), (int(x), int(y)), 4)
