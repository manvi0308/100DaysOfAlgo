''' Problem Statemenr : Python program to segregate even and odd nodes in a Linked List
Complexity : O(n)'''

head = None # head of list 

# Node class 
class Node: 
	
	# Function to initialise the node object 
	def __init__(self, data): 
		self.data = data # Assign data 
		self.next =None

def segregateEvenOdd(): 

	global head 
	end = head 
	prev = None
	curr = head 

	# Get pointer to last Node 
	while (end.next != None): 
		end = end.next

	new_end = end 

	# Consider all odd nodes before getting first even node 
	while (curr.data % 2 !=0 and curr != end): 
		
		new_end.next = curr 
		curr = curr.next
		new_end.next.next = None
		new_end = new_end.next
		
	# do following steps only if there is an even node 
	if (curr.data % 2 == 0): 
		
		head = curr 

		# now curr points to first even node 
		while (curr != end): 
			
			if (curr.data % 2 == 0): 
				
				prev = curr 
				curr = curr.next
				
			else: 
				
				# Break the link between prev and curr 
				prev.next = curr.next

				# Make next of curr as None 
				curr.next = None

				# Move curr to end 
				new_end.next = curr 

				# Make curr as new end of list 
				new_end = curr 

				# Update curr pointer 
				curr = prev.next
			
	# We have to set prev before executing rest of this code 
	else: 
		prev = curr 

	if (new_end != end and end.data % 2 != 0): 
		
		prev.next = end.next
		end.next = None
		new_end.next = end 
		
# Given a reference (pointer to pointer) to the head 
# of a list and an int, push a new node on the front 
# of the list. 
def push(new_data): 
	global head 

	# 1 & 2: Allocate the Node & 
	#		 Put in the data 
	new_node = Node(new_data) 

	# 3. Make next of new Node as head 
	new_node.next = head 

	# 4. Move the head to point to new Node 
	head = new_node 

# Utility function to print a linked list 
def printList(): 
	global head 
	temp = head 
	while(temp != None): 
		
		print(temp.data, end = " ") 
		temp = temp.next
		
	print(" ") 

# Driver program to test above functions 

push(11) 
push(10) 
push(8) 
push(6) 
push(4) 
push(2) 
push(0) 
print("Origional Linked List") 
printList() 

segregateEvenOdd() 

print("Modified Linked List") 
printList() 


