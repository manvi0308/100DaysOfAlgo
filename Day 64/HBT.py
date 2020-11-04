'''Given Inorder traversal and Level Order traversal of a Binary Tree. The task is to calculate the height of the tree without constructing it.

Example:

Input : Input: Two arrays that represent Inorder
       and level order traversals of a 
       Binary Tree
       in[]    = {4, 8, 10, 12, 14, 20, 22};
       level[] = {20, 8, 22, 4, 12, 10, 14};
Output : 4
 '''
# Python3 program to calculate height of Binary Tree from InOrder and LevelOrder Traversals 

# Function to find the index of value in the InOrder Traversal list 


def search(arr, start, end, value): 
	for i in range(start, end + 1): 
		if arr[i] == value: 
			return i 
	return -1

# Function to calculate the height of the Binary Tree 
def getHeight(inOrder, levelOrder, 
			start, end, height, n): 
					
	# Base Case 
	if start > end: 
		return 0
	
	# Get Index of current root in InOrder Traversal 
	getIndex = search(inOrder, start, end, levelOrder[0]) 

	if getIndex == -1: 
		return 0

	# Count elements in Left Subtree 
	leftCount = getIndex - start 

	# Count elements in Right Subtree 
	rightCount = end - getIndex 
	
	# Declare two lists for left and right subtrees 
	newLeftLevel = [None for _ in range(leftCount)] 
	newRightLevel = [None for _ in range(rightCount)] 

	lheight, rheight, k = 0, 0, 0

	# Extract values from level order traversal list 
	# for current left subtree 
	for i in range(n): 
		for j in range(start, getIndex): 
			if levelOrder[i] == inOrder[j]: 
				newLeftLevel[k] = levelOrder[i] 
				k += 1
				break
	
	k = 0

	# Extract values from level order traversal list 
	# for current right subtree 
	for i in range(n): 
		for j in range(getIndex + 1, end + 1): 
			if levelOrder[i] == inOrder[j]: 
				newRightLevel[k] = levelOrder[i] 
				k += 1
				break

	# Recursively call to calculate height 
	# of left subtree 
	if leftCount > 0: 
		lheight = getHeight(inOrder, newLeftLevel, start, 
							getIndex - 1, height, leftCount) 

	# Recursively call to calculate height 
	# of right subtree 
	if rightCount > 0: 
		rheight = getHeight(inOrder, newRightLevel, 
							getIndex + 1, end, height, rightCount) 

	# current height 
	height = max(lheight + 1, rheight + 1) 

	# return height 
	return height 
