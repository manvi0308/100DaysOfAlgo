# Problem statement : https://www.interviewbit.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None
class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        # Creation of two new lists small and large
        small = None
        large = None
        
        # Pointers for traversing small and large respectively
        s = small
        l = large
        
        # Assigning Pointer for traversing list A 
        cur = A
        
        while(cur != None):
            # Creating New Node
            temp = ListNode(cur.val)
            
            # Checking for small or large
            if cur.val < B:
                if small == None:
                    small = temp
                    s = temp
                else:
                    s.next = temp
                    s = s.next
                    else:
                if large == None:
                    large = temp
                    l = temp
                else:
                    l.next = temp
                    l = l.next
            
            # Incrementing the cur pointer
            cur = cur.next
            
        # Appending large list to the small list
        if s != None:
            s.next = large
        else:
            return(large)
        
        # return the Head pointer
        return(small)

