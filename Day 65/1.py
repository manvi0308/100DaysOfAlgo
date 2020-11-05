''' Problem Statement : Given a Binary tree and a number N, write a program to find the N-th node in the Postorder traversal of the given Binary tree.

Approach : The idea to solve this problem is to do postorder traversal of the given binary tree and keep track of the count of nodes visited while
traversing the tree and print the current node when the count becomes equal to N.

Complexity : Time complexity : O(n)
Space Complexity : O(1)

'''

"""Python3 program to find n-th node of Postorder Traversal of Binary Tree"""

# A Binary Tree Node 
# Utility function to create a new tree node 
class createNode: 

	# Constructor to create a newNode 
	def __init__(self, data): 
		self.data= data 
		self.left = None
		self.right = None

# function to find the N-th node in the postorder traversal of a given binary tree 
flag = [0] 
def NthPostordernode(root, N): 

	if (root == None): 
		return

	if (flag[0] <= N[0]): 
		
		# left recursion 
		NthPostordernode(root.left, N) 

		# right recursion 
		NthPostordernode(root.right, N) 

		flag[0] += 1

		# prints the n-th node of 
		# preorder traversal 
		if (flag[0] == N[0]): 
			print(root.data) 
						
