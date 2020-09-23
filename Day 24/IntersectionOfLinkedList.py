''' 1) Problem Statement : To find the intersection point of two linked list
    2) Time complexity : O(m + n), where m and n is the length of linked list A and B
    
    3) Approach: Find the count of number of nodes in each linked list, whichever is bigger , move the head of that particular
    linked list that many steps equals to the difference in number of nodes, after that compare the values in both the linked liist
    '''
def getIntersectionNode(self, A, B):
        
        # variables to store the number of nodes in linked list A and linked list B
        countA = 0
        countB = 0
        
        # To store the head node
        headA = A
        headB = B
        
        # Getting the count of number of nodes in Linked list 1
        while A is not None:
            A = A.next
            countA += 1

        # Getting the count of number of nodes in linked list 2   
        while B is not None:
            B = B.next
            countB += 1
        
         
        A = headA
        B = headB
        
        # Where the number of nodes in linked list 1 is greater than linked list 2
        if countA > countB:
            for i in range(countA-countB):
                
                # shift the head of list A countA-countB steps ahead
                A = A.next


        else:
            for i in range(countB-countA):

                # shift the head of list B countB-countA steps ahead
                B = B.next

        # Looking for intersection point       
        for i in range(min(countA,countB)):
            if A is B:
                return A
            A = A.next
            B = B.next
            
        return None
            

