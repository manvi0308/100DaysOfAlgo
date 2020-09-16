'''Problem statement : Write a function that counts the number of times a given int occurs in a Linked List
   Approach used: Iterative
   Time complexity: O(n)'''

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
    
    # Function to count the occurence of a particular element. The function will return count
    def countOccurenceOfElement(self, searching_element):
        current = self.head  # Making the current point to the head node
        count = 0            # Variable for storing the count
        while(current is not None): #Iterate till the current do not points to None or end of Linked List is reached
            # If the data of current node is the same as data to be searched
            if current.data == searching_element:
                count += 1  
            current = current.next
        
        return count
    
    # A utility function to print linked list
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

# Driver code

# Inserting values
llist = LinkedList()
llist.insertAtBeginning(20)
llist.insertAtBeginning(30)
llist.insertAtBeginning(40)
llist.insertAtBeginning(50)
llist.insertAtBeginning(60)
llist.insertAtBeginning(30)
llist.insertAtBeginning(30)

# Passing the value to be searched to the function
count_answer = llist.countOccurenceOfElement(30)

#Printing the final answer
print(count_answer)

#Code ends here
