''Problem statement : Construct a binary tree from given inorder and preorder traversals '''


# Data structure to store a Binary Tree node
class Node:
	# Constructor
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


# Recursive function to perform inorder traversal of a binary tree
def inorderTraversal(root):

	if root is None:
		return

	inorderTraversal(root.left)
	print(root.data, end=' ')
	inorderTraversal(root.right)


# Recursive function to perform postorder traversal of a binary tree
def preorderTraversal(root):

	if root is None:
		return

	print(root.data, end=' ')
	preorderTraversal(root.left)
	preorderTraversal(root.right)


# Recursive function to construct a binary tree from given
# inorder and preorder sequence
def construct(start, end, preorder, pIndex, dict):

	# base case
	if start > end:
		return None, pIndex

	# The next element in preorder will be the root node of subtree
	# formed by inorder[start, end]
	root = Node(preorder[pIndex])
	pIndex = pIndex + 1

	# get the index of root node in inorder to determine the
	# boundary of left and right subtree
	index = dict[root.data]

	# recursively construct the left subtree
	root.left, pIndex = construct(start, index - 1, preorder, pIndex, dict)

	# recursively construct the right subtree
	root.right, pIndex = construct(index + 1, end, preorder, pIndex, dict)

	# return current node
	return root, pIndex


# Construct a binary tree from inorder and preorder traversals
# This function assumes that the input is valid
# i.e. given inorder and preorder sequence forms a binary tree
def constructTree(inorder, preorder):

	# create a dictionary to efficiently find the index of any element in
	# given inorder sequence
	dict = {}
	for i, e in enumerate(inorder):
		dict[e] = i

	# pIndex stores index of next unprocessed node in preorder sequence
	# start with root node (present at 0'th index)
	pIndex = 0

	return construct(0, len(inorder) - 1, preorder, pIndex, dict)[0]
