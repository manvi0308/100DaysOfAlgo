'''AVL tree is a self-balancing Binary Search Tree (BST) where the difference between heights of left and right subtrees cannot be more than one for all nodes.

Most of the BST operations (e.g., search, max, min, insert, delete.. etc) take O(h) time where h is the height of the BST. The cost of these operations may become O(n) 
for a skewed Binary tree. If we make sure that height of the tree remains O(Logn) after every insertion and deletion, 
then we can guarantee an upper bound of O(Logn) for all these operations. The height of an AVL tree is always O(Logn) where n is the number of nodes in the tree '''

# Python code to insert a node in AVL tree 

# Generic tree node class 
class TreeNode(object): 
	def __init__(self, val): 
		self.val = val 
		self.left = None
		self.right = None
		self.height = 1

# AVL tree class which supports the 
# Insert operation 
class AVL_Tree(object): 

	# Recursive function to insert key in 
	# subtree rooted with node and returns 
	# new root of subtree. 
	def insert(self, root, key): 
	
		# Step 1 - Perform normal BST 
		if not root: 
			return TreeNode(key) 
		elif key < root.val: 
			root.left = self.insert(root.left, key) 
		else: 
			root.right = self.insert(root.right, key) 

		# Step 2 - Update the height of the 
		# ancestor node 
		root.height = 1 + max(self.getHeight(root.left), 
						self.getHeight(root.right)) 

		# Step 3 - Get the balance factor 
		balance = self.getBalance(root) 

		# Step 4 - If the node is unbalanced, 
		# then try out the 4 cases 
		# Case 1 - Left Left 
		if balance > 1 and key < root.left.val: 
			return self.rightRotate(root) 

		# Case 2 - Right Right 
		if balance < -1 and key > root.right.val: 
			return self.leftRotate(root) 

		# Case 3 - Left Right 
		if balance > 1 and key > root.left.val: 
			root.left = self.leftRotate(root.left) 
			return self.rightRotate(root) 

		# Case 4 - Right Left 
		if balance < -1 and key < root.right.val: 
			root.right = self.rightRotate(root.right) 
			return self.leftRotate(root) 

		return root 

	def leftRotate(self, z): 

		y = z.right 
		T2 = y.left 

		# Perform rotation 
		y.left = z 
		z.right = T2 

		# Update heights 
		z.height = 1 + max(self.getHeight(z.left), 
						self.getHeight(z.right)) 
		y.height = 1 + max(self.getHeight(y.left), 
						self.getHeight(y.right)) 

		# Return the new root 
		return y 

	def rightRotate(self, z): 

		y = z.left 
		T3 = y.right 

		# Perform rotation 
		y.right = z 
		z.left = T3 

		# Update heights 
		z.height = 1 + max(self.getHeight(z.left), 
						self.getHeight(z.right)) 
		y.height = 1 + max(self.getHeight(y.left), 
						self.getHeight(y.right)) 

		# Return the new root 
		return y 

	def getHeight(self, root): 
		if not root: 
			return 0

		return root.height 

	def getBalance(self, root): 
		if not root: 
			return 0

		return self.getHeight(root.left) - self.getHeight(root.right) 

	def preOrder(self, root): 

		if not root: 
			return

		print("{0} ".format(root.val), end="") 
		self.preOrder(root.left) 
		self.preOrder(root.right) 
