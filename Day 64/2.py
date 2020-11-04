# Python program to find binary tree with given 
# inorder traversal 

# Node Structure 
class Node: 

	# Utility to create a new node 
	def __init__(self , item): 
		self.key = item 
		self.left = None
		self.right = None

# A utility function to do preorder traversal of BST 
def preorder(root): 
	if root is not None: 
		print root.key, 
		preorder(root.left) 
		preorder(root.right) 


# Function for constructing all possible trees with given inorder traversal stored in an array from arr[start] to arr[end]. This function returns a  vector of trees. 
def getTrees(arr , start , end): 

	# List to store all possible trees 
	trees = [] 
	
	""" if start > end then subtree will be empty so 
	returning NULL in the list """
	if start > end : 
		trees.append(None) 
		return trees 
	

	""" Iterating through all values from start to end 
		for constructing left and right subtree 
		recursively """
	for i in range(start , end+1): 

		# Constructing left subtree 
		ltrees = getTrees(arr , start , i-1) 
		
		# Constructing right subtree 
		rtrees = getTrees(arr , i+1 , end) 
		
		""" Looping through all left and right subtrees 
		and connecting to ith root below"""
		for j in ltrees : 
			for k in rtrees : 

				# Making arr[i] as root 
				node = Node(arr[i]) 
	
				# Connecting left subtree 
				node.left = j 

				# Connecting right subtree 
				node.right = k 

				# Adding this tree to list 
				trees.append(node) 
	return trees 

# Driver program to test above function 
inp = [4 , 5, 7] 
n = len(inp) 

trees = getTrees(inp , 0 , n-1) 

print "Preorder traversals of different possible\ 
Binary Trees are " 
for i in trees : 
	preorder(i); 
	print "" 

