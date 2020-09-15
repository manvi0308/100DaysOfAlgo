''' Problem statement : Delete a node in a linked list
    Assumptions       : Only took insertion at beginning function for inserting/creating a node
    Approach          : For deletion there are three cases 
                        1) If the head node is to be deleted
                        2) If any other node, except head is to be deleted
                        3) If the node don't exist'''

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None
    
    # Function to insert a node at beginning
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    # Given a reference to the head of a list and a key,delete the first occurence of key in linked list  
    def deleteNode(self, key):  
        temp = self.head  
  
        # Case 1: If head node itself holds the key to be deleted  
        if (temp is not None):  
            if (temp.data == key):  
                self.head = temp.next
                temp = None
                return
  
        # Case 2: Search for the key to be deleted, keep track of the previous node as we need to change 'prev.next'  
        while(temp is not None):  
            if temp.data == key:  
                break
            prev = temp  
            temp = temp.next
  
        # if key was not present in linked list  
        if(temp == None):  
            return
  
        # Unlink the node from linked list  
        prev.next = temp.next
        temp = None
  
  
    # Utility function to print the linked LinkedList  
    def printList(self):  
        temp = self.head  
        while(temp):  
            print (" %d" %(temp.data)),  
            temp = temp.next

# Driver program  
llist = LinkedList()  
llist.insertAtBeginning(7)  
llist.insertAtBeginning(1)  
llist.insertAtBeginning(3)  
llist.insertAtBeginning(2)  
  
print ("Created Linked List: ") 
llist.printList()  
llist.deleteNode(1)  
print ("\nLinked List after Deletion of 1:") 
llist.printList()  
  