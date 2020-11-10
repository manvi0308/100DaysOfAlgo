

'''Problem statement : Python program to check if two node are in same subtrees of the root node 

Approach : The idea is similar of searching a node in Binary Tree. There are four different cases:
1) If both node1 and node2 are in left subtree of root node.
2) If both node1 and node2 are in right subtree of the root node.
3) If node1 is in the left subtree of the root node and node2 is in the right subtree of root node.
4) If node1 is in the right subtree of the root node and node2 is in the left subtree of root node.
'''

# A Binary Tree Node 
class newNode: 

	# Constructor to create a newNode 
	def __init__(self, data): 
		self.data= data 
		self.left = None
		self.right = None
		self.visited = False

# Function to traverse the tree in 
# preorder and check if the given 
# node exists in a binary tree 
def ifNodeExists(node, key) : 
	if (node == None): 
		return False

	if (node.data == key): 
		return True

	""" then recur on left sutree """
	res1 = ifNodeExists(node.left, key) 

	""" now recur on right subtree """
	res2 = ifNodeExists(node.right, key) 

	return res1 or res2 

# Function to check if the two given nodes are in same subtrees of the root node 
def ifSameSubTree(root, node1, node2): 

	if (root == None) : 
		return False

	# CASE 1: If both nodes are in left subtree 
	if (ifNodeExists(root.left, node1) 
		and ifNodeExists(root.left, node2)): 
		return True

	# CASE 2: If both nodes are in right subtree 
	elif (ifNodeExists(root.right, node1) 
			and ifNodeExists(root.right, node2)): 
		return True
	
	# CASE 3 and 4: Nodes are in different subtrees 
	else: 
		return False
