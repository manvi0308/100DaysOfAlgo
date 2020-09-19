'''Problem Statement : Write a program to check if a given linked list is palindrome or not.
   Example : 1->2->1->None is palindrome
             1->3->5->5->None is not palindrome
   Constraints: 0->0->0 will be palindrome
    '''
# Data Structure to store a linked list node
class Node:
	# Constructor
	def __init__(self, data, next=None):
		self.data = data
		self.next = next


# Function to determine if a given linked list is palindrome or not
def isPalindrome(curr, head):

	# base case: end of the list reached
	if curr is None:
		return True, head

	# advance all the way till end of the list and
	# return false in case of any conflict
	isPalin, head = isPalindrome(curr.next, head)
	if not isPalin:
		return False, head

	# check vs. "mirror" when "coming back" from recursion
	if curr.data != head.data:
		return False, head

	# advance "mirror" by one step for every one step "taken back" in the recursion
	head = head.next
	return True, head


# Determine if a given linked list is palindrome or not .
# The function takes a pointer to the head node of the list.
def checkPalindrome(head):
	return isPalindrome(head, head)[0]


if __name__ == '__main__':

	head = Node(1)
	head.next = Node(2)
	head.next.next = Node(3)
	head.next.next.next = Node(2)
	head.next.next.next.next = Node(1)

	if checkPalindrome(head):
		print("Linked List is a palindrome")
	else:
		print("Linked List is not a palindrome")
