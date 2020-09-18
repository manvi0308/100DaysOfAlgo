''' Problem Statement : Given a singly linked list, whose nodes represent digits of a number, add a single digit number
to it.
Example: 9->9->3->2->1->Null is the input linked list on adding 8 it should become 9->9->3->2->8->Null
References : Techie delight 
Approach : At first reverse the given linked list, then add the number to be added to first node, like in above example,
1->2->3->9->9->Null, suppose we have to add 5 in this (1+5 = 6), then linked list should become, 6->2->3->9->9->Null, Now a
againg use the reverse operation to reverse the linked list.'''

# Node class
class Node:
	def __init__(self, data, left=None, right=None, next=None):
		self.data = data
		self.left = left
		self.right = right
		self.next = next


# Helper function to print given linked list
def printList(msg, head):

	print(msg, end='')
	while head:
		print(head.data, end=" -> ")
		head = head.next
	print("None")


# Function to reverse the given linked list
def reverse(head):

	prev = None
	current = head

	# traverse the list
	while current:
		# tricky: note the next node
		next = current.next

		# fix the current node
		current.next = prev

		# advance the two pointers
		prev = current
		current = next

	# fix the head pointer to point to the front
	head = prev
	return head


# Function to add a single-digit number to a singly linked list
# whose nodes represents digits of a number
def addDigit(head, digit):

	# empty list
	if head is None:
		return head

	# reverse the linked list
	head = reverse(head)

	# initialize carry with given digit
	carry = digit

	# traverse the reversed list
	curr = head
	while carry > 0:

		# get sum of current node and carry
		sum = curr.data + carry

		# update value of the current node with the single-digit sum
		curr.data = sum % 10

		# set carry for the next node
		carry = sum // 10

		# break if current node is the last node
		if curr.next is None:
			break

		# move to the next node
		curr = curr.next

	# add a node at the end of linked list if there is any carry left
	if carry > 0:
		curr.next = Node(carry)

	# reverse the list again to restore the original order
	head = reverse(head)
	return head

# driver code
if __name__ == '__main__':

	head = Node(9)
	head.next = Node(9)
	head.next.next = Node(9)
	head.next.next.next = Node(9)
	head.next.next.next.next = Node(8)

    # Number to be added
	digit = 7

	printList(" Original Linked List: ", head)
	head = addDigit(head, digit)
	printList("Resultant Linked List: ", head)
