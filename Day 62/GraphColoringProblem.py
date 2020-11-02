'''Problem Statement :- Graph Coloring Problem
The Graph coloring or vertex coloring is a way of coloring the vertices of graph such that no two vertices share the same color
'''

# class to represent a graph object
class Graph:

	# Constructor
	def __init__(self, edges, N):

		self.adj = [[] for _ in range(N)]

		# add edges to the undirected graph
		for (src, dest) in edges:
			self.adj[src].append(dest)
			self.adj[dest].append(src)


# Function to assign colors to vertices of graph
def colorGraph(graph):

	# stores color assigned to each vertex
	result = {}

	# assign color to vertex one by one
	for u in range(N):

		# set to store color of adjacent vertices of u
		# check colors of adjacent vertices of u and store in set
		assigned = set([result.get(i) for i in graph.adj[u] if i in result])

		# check for first free color
		color = 1
		for c in assigned:
			if color != c:
				break
			color = color + 1

		# assigns vertex u the first available color
		result[u] = color

	for v in range(N):
		print("Color assigned to vertex", v, "is", colors[result[v]])


# Greedy coloring of graph
if __name__ == '__main__':

	# Add more colors for graphs with many more vertices
	colors = ["", "BLUE", "GREEN", "RED", "YELLOW", "ORANGE", "PINK",
			  "BLACK", "BROWN", "WHITE", "PURPLE", "VOILET"]

	#  of graph edges as per above diagram
	edges = [(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)]

	# Set number of vertices in the graph
	N = 6

	# create a graph from edges
	graph = Graph(edges, N)

	# color graph using greedy algorithm
	colorGraph(graph)
