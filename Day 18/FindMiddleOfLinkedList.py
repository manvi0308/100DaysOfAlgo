'''Problem Statement : Write a program to find the middle element of linked list
   Approach used: Maintain two pointers, initially they both point to head of linked list, make one of them move by 2 
   places in one step and other one by 1 place.When the fast pointer reaches end slow pointer will reach middle of the
   linked list
   Time complexity is O(n)'''
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked list class
class LinkedList:
    def __init__(self):
        self.head = None
    
    # Function to insert a node at beginning
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    # Function to insert a node at last
    def insertAtLast(self, new_data):
        new_node = Node(new_data)
        # Case where the linked list is initially empty
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        # Iterating till the last node
        while(last.next):
            last = last.next
        last.next = new_node
    
    # Function to insert a node in betweeen two nodes
    def insertAtSomewhereBetween(self, prev_node, new_data):
        if prev_node is None:
            print('Previous node cannot be empty')
            return
        
        new_node = Node(new_data)
        new_node.next = prev_node
        prev_node.next = new_node
    
    # Function to find the middle of linked list
    def findMiddleOfLinkedList(self, head):
        
        # Initialize both the pointers pointing to head
        first_ptr = self.head
        second_ptr = self.head
        
        # Case where linked list is empty
        if self.head is None:
            print('Empty linked list')
            return
        
        # Else iterate
        while(first_ptr is not None and second_ptr.next is not None):
            second_ptr = second_ptr.next.next  #Its the fast pointer that moves through two places
            first_ptr  = first_ptr.next        # Move through 1 places
        
        print('Middle most element of linked list is ',first_ptr.data)



    # A  utility function to print list
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp.next

# Driver code
if __name__ == "__main__";
  llist = LinkedList()
  llist.insertAtBeginning(10)
  llist.insertAtLast(50)
  llist.insertAtSomewhereBetween(10, 60)
  llist.printList()
