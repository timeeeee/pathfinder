from math import sqrt
import pygame

# this could potentially be a subclass of Sprite

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
        return [(self.location, [1]),
                (destination, [0])]

    # findPath returns list of destinations on the shortest path from
    # first to last vertex of a map.
    def findPath(self, graph):
        # placeholder, currently just returns list of last vertex
        # so the character will just travel in a straight line

	#----This first section executes dijkstra's algorithm---

	current=0 #index of first node
	while True: 
		if current==0: #if node is the beginning
			graph[current].distance=0
			graph[current].visit_status=1
		for n in graph[current].neighbors: #checks distances between neighbors of current node
			if graph[n].visit_status==0:
				graph[n].previous=current
				temp_distance=sqrt( (graph[current].vertex[0]-graph[n].vertex[0])**2 + (graph[current].vertex[1]-graph[n].vertex[1])**2 ) + graph[current].distance	
				if graph[n].distance > temp_distance:
					graph[n].distance=temp_distance
		distance=[]
		index=[]
		ind=0
		for node in graph: #Saves currently unvisited distances with associated indices
			if node.visit_status==0:
				distance.append((node.distance))
				index.append(ind)
			ind+=1
		current=index[distance.index(min(distance))] #Sets next node to index with lowest distance that is also unvisited
		graph[current].visit_status=1
		if current==len(graph)-1: #if current is the last index, then we're done!
			break

	#----This second section saves the shortest path----------
	
	shortest_path=[graph[len(graph)-1].vertex] #last vertex first
	current=len(graph)-1
	while True: #goes through stack of vertices and places them in shortest_path
		current=graph[current].previous
		if current==0:
			break
		shortest_path.append(graph[current].vertex)
	shortest_path.reverse()
	return(shortest_path)

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
