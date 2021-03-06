class Node: 

	#The ever so sexy container for each vertex on graph

	def __init__(self, vertex, neighbors=[]):

		self.vertex = vertex #Location of node
		self.neighbors = list(neighbors) #Contains index for neighboring nodes in graph
		self.distance = float("inf") #Distance value from beginning.  Default is infinity...Babay...
		self.previous = "undef" #Saves index of previous node to help keep track of path.
		self.visit_status = 0 #0 means unvisited. 1 mean visited.  

	def __str__(self):
		return "Node(" + str(self.vertex) + ", " + str(self.neighbors) + ")"

	def __repr__(self):
		return str(self)
