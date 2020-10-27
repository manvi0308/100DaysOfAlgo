'''Depth-first search is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node 
as the root node in the case of a graph) and explores as far as possible along each branch before backtracking. So the basic idea is to start from the root or any arbitrary 
node and mark the node and move to the adjacent unmarked node and continue this loop until there is no unmarked adjacent node. Then backtrack and check for other unmarked 
nodes and traverse them. Finally print the nodes in the path.'''


# Python3 program to print DFS traversal 
# from a given given graph 
from collections import defaultdict 

# This class represents a directed graph using 
# adjacency list representation 
class Graph: 

	# Constructor 
	def __init__(self): 

		# default dictionary to store graph 
		self.graph = defaultdict(list) 

	# function to add an edge to graph 
	def addEdge(self, u, v): 
		self.graph[u].append(v) 

	# A function used by DFS 
	def DFSUtil(self, v, visited): 

		# Mark the current node as visited 
		# and print it 
		visited[v] = True
		print(v, end = ' ') 

		# Recur for all the vertices 
		# adjacent to this vertex 
		for i in self.graph[v]: 
			if visited[i] == False: 
				self.DFSUtil(i, visited) 

	# The function to do DFS traversal. It uses 
	# recursive DFSUtil() 
	def DFS(self, v): 

		# Mark all the vertices as not visited 
		visited = [False] * (max(self.graph)+1) 

		# Call the recursive helper function 
		# to print DFS traversal 
		self.DFSUtil(v, visited) 
