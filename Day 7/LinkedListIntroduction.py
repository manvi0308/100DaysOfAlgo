'''Linked list - Creation of Linked List
               - Insertion of Linked List
               - Printing of Linked List'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__ == '__main__':
    llist = LinkedList() # To initialize a linked list object having head as Null
    llist.head = Node(1) #Inserting 1 as the first node
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next     = third
    llist.printList()

