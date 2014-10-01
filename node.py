class Node: 

	#The ever so sexy container for each vertex on graph

	vertex = (0,0) #Location of node
	neighbors = [] #Contains index for neighboring nodes in graph
	distance = "inf" #Distance value from beginning.  Default is infinity...Babay...
	previous = "undef" #Saves index of previous node to help keep track of path.
	visit_status = 0 #0 means unvisited. 1 mean visited.  

