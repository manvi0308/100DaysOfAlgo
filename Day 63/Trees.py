''' Insertion in a Binary Tree in level order
Given a binary tree and a key, insert the key into the binary tree at the first position available in level order.'''


The idea is to do iterative level order traversal of the given tree using queue. If we find a node whose left child is empty, we make new key as left child of the node. 
Else if we find a node whose right child is empty, we make the new key as right child. We keep traversing the tree until we find a node whose either left or right is empty. '''
 
 # Python program to insert element in binary tree 
class newNode(): 

	def __init__(self, data): 
		self.key = data
		self.left = None
		self.right = None
		
""" Inorder traversal of a binary tree"""
def inorder(temp):

	if (not temp):
		return

	inorder(temp.left) 
	print(temp.key,end = " ")
	inorder(temp.right) 


"""function to insert element in binary tree """
def insert(temp,key):

	if not temp:
		root = newNode(key)
		return
	q = [] 
	q.append(temp) 

	# Do level order traversal until we find 
	# an empty place. 
	while (len(q)): 
		temp = q[0] 
		q.pop(0) 

		if (not temp.left):
			temp.left = newNode(key) 
			break
		else:
			q.append(temp.left) 

		if (not temp.right):
			temp.right = newNode(key) 
			break
		else:
			q.append(temp.right) 
	
# Driver code 
if __name__ == '__main__':
	root = newNode(10) 
	root.left = newNode(11) 
	root.left.left = newNode(7) 
	root.right = newNode(9) 
	root.right.left = newNode(15) 
	root.right.right = newNode(8) 

	print("Inorder traversal before insertion:", end = " ")
	inorder(root) 

	key = 12
	insert(root, key) 

	print() 
	print("Inorder traversal after insertion:", end = " ")
	inorder(root)


