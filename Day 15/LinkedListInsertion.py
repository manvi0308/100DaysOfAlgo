''' Linked List : Insertion and deletion'''

# Node class
class Node:
    
    
    # initialing the node object
    def __init__(self,data):
        self.data = data  # Assigning data
        self.next = None  # Assigning next as NULL
# Linked list class
class LinkedList:
    
    # Function to initialize the linked list object
    def __init__(self):
        self.head = None

''' Insertion can be done as :-
    1) At front
    2) At  end
    3) Somewhere in between two nodes''' +

# Function for inserting a node at beginning , its time complexity is O(1)
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data) # Creating a new node
        new_node.next = self.head # Assigning the next of new node as head
        self.head = new_node      # Move the head to point to the new node

# Function for inserting a node after a given node
    def insertAfterANode(self, prev_node,  new_data):
        if prev_node is None:
            print('There is no previous node')
            return
    
    # Creation of new node
        new_node = Node(new_data)
    # Linking new node next to previous node next
        new_node.next = prev_node.next
    # Linking previous node next to new node
        prev_node.next = new_node
    
# Function for inserting a node at the last position its time complexity will be O(n) since we have to traverse n element
    def insertAtLast(self, new_data):
        new_node = Node(new_data)
    # There will be two cases here : 1)If the linked list is initially happy
                                     # 2)If there are some nodes already
        
        if self.head is None:  # Case 1
            self.head = new_node
            return
        # Case 2 in this case we have to iter till the last node
        last = self.head 
        while(last.next):
            last = last.next
    
        last.next = new_node  #Finally assigning it to the last node

