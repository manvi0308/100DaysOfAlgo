''' Problem statement : Check if given binary tree is height balanced or not
In a height balanced tree, the difference between height of left and right subtree is 0 or 1'

Approach : 
1) Using post order traversal of tree
2) Start from the bottom of tree, return height of subtree rooted at given node to its parent node

Complexity :
Time complexity : O(n)
Space complexity : O(h), where h is height of binary tree'''



# Data structure to store a Binary Tree node
class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


# Recursive function to check if given binary tree is height balanced or not
def isHeightBalanced(root, isBalanced=True):

    # base case: tree is empty or tree is not balanced
    if root is None or not isBalanced:
        return 0, isBalanced

    # get height of left subtree
    left_height, isBalanced = isHeightBalanced(root.left, isBalanced)

    # get height of right subtree
    right_height, isBalanced = isHeightBalanced(root.right, isBalanced)

    # tree is unbalanced if absolute difference between height of
    # its left subtree and right subtree is more than 1
    if abs(left_height - right_height) > 1:
        isBalanced = False

    # return height of subtree rooted at current node
    return max(left_height, right_height) + 1, isBalanced


if __name__ == '__main__':

    """ Construct below tree
              1
            /   \
           /     \
          2       3
         / \     /
        4   5   6
    """

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)

    if isHeightBalanced(root)[1]:
        print("Yes")
    else:
        print("No")
