# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        head=A
        
        count_zero = 0
        count_one  = 0
        
        while head:
            if head.val==0:
                count_zero+=1
            else:
                count_one+=1
            head=head.next    
            
        head=A
        c=0
        while head:
            if c<count_zero:
                c += 1
                head.val=0
            else:
                head.val=1
            head=head.next
            
         return A
