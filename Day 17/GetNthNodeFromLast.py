''' Problem Statement : Given a Linked List and a number n, write a function that returns the value at the n’th node 
from the end of the Linked List.
Approach used: Iterative'''

# Node class
class Node:
    # Function to initialize the node
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked list class
class LinkedList:
    def __init__(self):
        self.head = None
    
    # Function to insert at the beginning
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Function to print Nth node from last
    def printNthNodefromLast(self, node_number):
        temp = self.head # A temporary variable for pointing to the header node
        length_linkedlist = 0  #Initializing length of linked list

        # Finding length of linked list
        while(temp is not None):
            temp = temp.next
            length_linkedlist += 1
        
        # Case where entered/desired location is greater than the node number
        if node_number > length_linkedlist:
            print('Node number entered is greater than the length of linked list')
            return
        
        # Else go this way
        temp = self.head
        for i in range(0, length_linkedlist-node_number):
            temp = temp.next
        
        print(temp.data)

# Driver code
llist = LinkedList()

# Inserting nodes to form a linked list
llist.insertAtBeginning(10)
llist.insertAtBeginning(10)
llist.insertAtBeginning(34)
llist.insertAtBeginning(45)
llist.insertAtBeginning(56)
llist.insertAtBeginning(67)
llist.insertAtBeginning(78)
llist.insertAtBeginning(89)

# Note the formed linked list would be 89->78->67->56->45->34->10->10, because i have only used insertAtBeginningFunctio

llist.printNthNodefromLast(3) 

    