''' 1) Problem Statement : Remove redundant nodes in a linked list
    2) Logic : Any three adjacent nodes with same x or y value will be a redundant node, if found same x or y value for a 
    triplet then simply remove the middle node,do so for every three nodes in succession and this way the resultant 
    list will be redundant free linked list
    Time Complexity : O(n)'''


# Node class
class Node:
    # Initializer constructor, each node wil have two values x and y
    def __init__(self, x_data, y_data, next):
        self.x_data = x_data
        self.y_data = y_data
        self.next = next

    # To represent the nodes
    def __repr__(self):
        return str((self.x_data, self.y_data))
 
# A function to remove redundant nodes
def removeNodes(head):

    current = head
    while current.next and current.next.next:
        temp = current.next.next

    # Checking for a vertical triplet - Will have same x value
    if current.x_data == current.next.x_data and current.x_data == temp.x_data:
        # delete the middle most node
        current.next = temp
    
    # Checking for a horizontal triplet - will have same y value
    if current.y_data == current.y_data and current.y_data == temp.y_data:
        # delete the middle most node
        current.next = temp
    
    # If there is neither horizontal nor vertical triplet
    else:
        current = current.next

    return head


# A utlit function to print the list
def printList(head):

    ptr = head
    while ptr:
        print(ptr,end=' -> ')
        ptr = ptr.next

    print('NONE')


# Driver code
if __name__ == '__main__':
    keys = [(0,1),(0,5),(0,8),(1,8),(8,8),(9,8)]
    head = None
    
    for x,y in reversed(keys):
        head = Node(x_data,y_data,head)


    head = removeNodes(head)
    printList(head)
