'''Problem Statement : Write a function to reverse a singly linked linked list
Approach used: Iterating through the linked list by maintaing three pointers '''


# Function to reverse a linked list
def reverse_llist(llist):
    # Three pointers used for navigation of linked list are before, after and current
    
    before = None
    # Initially current points to the header node
    current = llist.head 

    # Case where the linked list is empty , simply return the control back to calling function
    if current is None:
        return
    
    after = current.next # after Points to the next of current node
    while after:
        current.next = before
        before = current
        current = after
        after = after.next
    
    current.next = before
    llist.head = current
 