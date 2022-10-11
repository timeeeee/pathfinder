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
        self.xVelocity = 0; self.yVelocity = 0
        self.graph = []
        self.stopped = True

    def accelerateUp(self):
        self.yVelocity -= 1
        self.stopped = True

    def accelerateDown(self):
        self.yVelocity += 1
        self.stopped = True

    def accelerateRight(self):
        self.xVelocity += 1
        self.stopped = True

    def accelerateLeft(self):
        self.xVelocity -= 1
        self.stopped = True

    def generateMap(self, destination, obstacleList):
        # Creates a list of nodes, with a node for self.location first, and
        # self.destination last. 
        vertices = [self.location] + sum([obstacle.getVertices() for obstacle in obstacleList], []) + [destination]
        nodes = list(map(Node, vertices))
        for index1, index2 in combinations(list(range(len(nodes))), 2):
            if not any(obstacle.collideLine(nodes[index1].vertex, nodes[index2].vertex) for obstacle in obstacleList):
#                print "{}->{} does not collide with any obstacles, connected nodes {}, {}".format(nodes[index1].vertex, nodes[index2].vertex, index1, index2)
                nodes[index1].neighbors.append(index2)
                nodes[index2].neighbors.append(index1)
#        print nodes
        self.graph = nodes
        return nodes

    # findPath returns list of destinations on the shortest path from
    # first to last vertex of a map.
    def findPath(self, graph):

        #----This first section executes dijkstra's algorithm---

        current=0 #index of first node
        graph[current].distance=0 #sets first node's distance to 0
        graph[current].visit_status=1 #we start at the first node, so it has been visited
        while current!=len(graph)-1: #continue this loop until the last node
                for n in graph[current].neighbors: #checks distances between neighbors of current node
                        if graph[n].visit_status==0: #checks neighbor as long as it has not been visited
                                temp_distance=sqrt( (graph[current].vertex[0]-graph[n].vertex[0])**2 + (graph[current].vertex[1]-graph[n].vertex[1])**2 ) + graph[current].distance
                                if graph[n].distance > temp_distance: #changes node's distance value if one calculated is smaller
                                        graph[n].distance=temp_distance
                                        graph[n].previous=current


                current_smallest=Node((0,0)) #initialize smallest path value 
                for node in graph: #loop finds the next node to start from
                        if node.visit_status==0 and node.distance<current_smallest.distance:
                                current_smallest=node
                current=graph.index(current_smallest)
                graph[current].visit_status=1

        #----This second section saves the shortest path----------
        
        shortest_path=[graph[len(graph)-1].vertex] #last vertex first
        current=len(graph)-1
        while current!=0: #goes through stack of vertices and places them in shortest_path
                current=graph[current].previous
                shortest_path.append(graph[current].vertex)
        shortest_path.reverse()
        return(shortest_path)

    def goTo(self, destination, obstacles):
        self.path = self.findPath(self.generateMap(destination, obstacles))
        self.destination = self.path.pop(0)
        self.stopped = False

    def update(self, dTime, obstacleList):
        # If keys are down, move according to key input. Otherwise, move along path.

        x, y = self.location

        if self.xVelocity or self.yVelocity:
            displacementX = self.xVelocity * self.speed * dTime / 1000.0
            displacementY = self.yVelocity * self.speed * dTime / 1000.0
            if (self.yVelocity and self.xVelocity):
                displacementX /= sqrt(2)
                displacementY /= sqrt(2)

            rect = pygame.Rect(0, 0, 5, 5)

            # Try to move along x

            # (We are bending over backwards a little here because Rects use
            # ints internally. Otherwise we could say "rect.move(...)")
            x += displacementX
            rect.center = (x, y)
            collision = rect.collidelist([obstacle.getInflated() for obstacle in obstacleList])
            if collision != -1:  # We hit an object- move the rect back
                x -= displacementX

            # Try to move along y
            y += displacementY
            rect.center = (x, y)
            collision = rect.collidelist([obstacle.getInflated() for obstacle in obstacleList])
            if collision != -1:  # We hit an object- move the rect back
                y -= displacementY
            
            self.location = (x, y)
            
        elif not(self.stopped):
            # Move towards closest destination. If already there, continue following self.path
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
        # for testing: draw the graph

        for node in self.graph:
            for neighbor in node.neighbors:
                pygame.draw.line(screen, (0, 255, 0), node.vertex, self.graph[neighbor].vertex)


        # x and y are probably floats
        x, y = self.location
        pygame.draw.circle(screen, (255, 0, 0), (int(x), int(y)), 4)
