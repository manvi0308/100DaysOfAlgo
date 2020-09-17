'''Problem statement : Reverse specified portion of linked list
Approach used : Suppose we have to reverse from 3rd node then initalize m as 3 , you have to skip the first m nodes, can
move a pointer to reach to the mth node and then reverse using the logic of complete reversal of linked list
Used iteration'''

# A linked list node
class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next


# Utility function to print a linked list
def printList(msg, head):
	print(msg, end=': ')
	ptr = head
	while ptr:
		print(ptr.data, end=" -> ")
		ptr = ptr.next
	print("None")


# Iteratively reverse a linked list from position m to n
def reverse(head, m, n):

	prev = None
	curr = head

	# 1. Skip the first m nodes
	i = 1
	while curr is not None and i < m:
		prev = curr
		curr = curr.next
		i = i + 1

	# prev now points to position the (m-1)'th node
	# curr now points to position the m'th node

	start = curr
	end = None

	# 2. Traverse and reverse the sub-list from position m to n
	while curr is not None and i <= n:

		# Take note of the next node
		next = curr.next

		# move the 'curr' node onto the 'end'
		curr.next = end
		end = curr

		# move to the next node
		curr = next
		i = i + 1

	# start points to the m'th node
	# end now points to the n'th node
	# curr now points to the (n+1)'th node

	# 3. Fix the pointers and return the head node
	start.next = curr
	if prev is None:		# when m = 1 (prev is None)
		head = end
	else:
		prev.next = end

	return head


if __name__ == '__main__':

	head = None
	for i in reversed(range(7)):
		head = Node(i + 1, head)

	(m, n) = (2, 5)

	printList("Original Linked List", head)
	head = reverse(head, m, n)
	printList("Reversed Linked List", head)
