''' Problem statement : Given a Binary Tree, find the vertical sum of the nodes that are in the same vertical line. Print all sums through different vertical lines.

Approach : We need to check the Horizontal Distances from the root for all nodes. If two nodes have the same Horizontal Distance (HD), 
then they are on the same vertical line. The idea of HD is simple. HD for root is 0, a right edge (edge connecting to right subtree) is
considered as +1 horizontal distance and a left edge is considered as -1 horizontal distance. For example, in the above tree, HD for Node 4
is at -2, HD for Node 2 is -1, HD for 5 and 6 is0 and HD for node 7 is +2.We can do an in-order traversal of the given Binary Tree. While 
traversing the tree, we can recursively calculate HDs. We initially pass the horizontal distance as 0 for root. For left subtree, we pass the 
Horizontal Distance as Horizontal distance of root minus 1. For right subtree, we pass the Horizontal Distance as Horizontal Distance of root plus 1.

Time complexity : O(n)'''


# Python3 program to find Vertical Sum in 
# a given Binary Tree 

# Node defintion 
class newNode: 
	
	def __init__(self, data): 
		
		self.left = None
		self.right = None
		self.data = data 
		
# Traverses the tree in in-order form and populates a hashMap that contains the vertical sum 
def verticalSumUtil(root, hd, Map): 

	# Base case 
	if(root == None): 
		return
	
	# Recur for left subtree 
	verticalSumUtil(root.left, hd - 1, Map) 

	# Add val of current node to 
	# map entry of corresponding hd 
	if(hd in Map.keys()): 
		Map[hd] = Map[hd] + root.data 
	else: 
		Map[hd] = root.data 
		
	# Recur for right subtree 
	verticalSumUtil(root.right, hd + 1, Map) 
	
# Function to find vertical_sum 
def verticalSum(root): 

	# a dictionary to store sum of 
	# nodes for each horizontal distance 
	Map = {} 
	
	# Populate the dictionary 
	verticalSumUtil(root, 0, Map); 

	# Prints the values stored 
	# by VerticalSumUtil() 
	for i,j in Map.items(): 
		print(i, "=", j, end = ", ") 
	
