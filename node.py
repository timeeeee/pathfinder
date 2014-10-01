class Node: 

	#The ever so sexy container for each vertex on graph

	def __init__(self, vertex=(0,0), neighbors=[], distance=float("inf"), previous="undef", visit_status=0):

		self.vertex = vertex #Location of node
		self.neighbors = neighbors #Contains index for neighboring nodes in graph
		self.distance = distance #Distance value from beginning.  Default is infinity...Babay...
		self.previous = previous #Saves index of previous node to help keep track of path.
		self.visit_status = visit_status #0 means unvisited. 1 mean visited.  

