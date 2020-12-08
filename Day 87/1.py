# Data structure to store a BST node
class Node:
    # Constructor
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
# Function to perform the pre-order traversal of a BST
def preorder(root):
 
    if root is None:
        return
 
    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)
 
 
# Recursive function to push nodes of a given binary search tree in a
# List in in-order fashion
def pushTreeNodes(root, nodes):
 
    # base case
    if root is None:
        return
 
    pushTreeNodes(root.left, nodes)
    nodes.append(root)
    pushTreeNodes(root.right, nodes)
 
 
# Recursive function to construct a height-balanced BST from
# given nodes in sorted order
def buildBalancedBST(nodes, start, end):
 
    # base case
    if start > end:
        return None
 
    # find the middle index
    mid = (start + end) // 2
 
    # The root node will be node present at the mid index
    root = nodes[mid]
 
    # recursively construct left and right subtree
    root.left = buildBalancedBST(nodes, start, mid - 1)
    root.right = buildBalancedBST(nodes, mid + 1, end)
 
    # return root node
    return root
 
 
# Function to construct a height-balanced BST from an unbalanced BST
def constructBalancedBST(root):
 
    # Push nodes of a given binary search tree in a List in sorted order
    nodes = []
    pushTreeNodes(root, nodes)
 
    # Construct a height-balanced BST from sorted BST nodes
    return buildBalancedBST(nodes, 0, len(nodes) - 1)
 
 

