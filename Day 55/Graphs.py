''' A Graph is a non-linear data structure consisting of nodes and edges. The nodes are sometimes also referred to as vertices
and the edges are lines or arcs that connect any two nodes in the graph. 
It consists of the following two components:
1. A finite set of vertices also called as nodes.
2. A finite set of ordered pair of the form (u, v) called as edge. The pair is ordered because (u, v) is not the same as (v, u) in case of a directed graph(di-graph). 
The pair of the form (u, v) indicates that there is an edge from vertex u to vertex v. The edges may contain weight/value/cost.'''

""" 
A Python program to demonstrate the adjacency 
list representation of the graph 
"""

# A class to represent the adjacency list of the node 
class AdjNode: 
	def __init__(self, data): 
		self.vertex = data 
		self.next = None


# A class to represent a graph. A graph 
# is the list of the adjacency lists. 
# Size of the array will be the no. of the 
# vertices "V" 
class Graph: 
	def __init__(self, vertices): 
		self.V = vertices 
		self.graph = [None] * self.V 

	# Function to add an edge in an undirected graph 
	def add_edge(self, src, dest): 
		# Adding the node to the source node 
		node = AdjNode(dest) 
		node.next = self.graph[src] 
		self.graph[src] = node 

		# Adding the source node to the destination as 
		# it is the undirected graph 
		node = AdjNode(src) 
		node.next = self.graph[dest] 
		self.graph[dest] = node 

	# Function to print the graph 
	def print_graph(self): 
		for i in range(self.V): 
			print("Adjacency list of vertex {}\n head".format(i), end="") 
			temp = self.graph[i] 
			while temp: 
				print(" -> {}".format(temp.vertex), end="") 
				temp = temp.next
			print(" \n") 



