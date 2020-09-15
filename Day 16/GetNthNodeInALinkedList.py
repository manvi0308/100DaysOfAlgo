
''' Problem Statement : To get the Nth node in a linked list
Algorithm: 1. Initialize count = 0
           2. Loop through the link list
                a. if count is equal to the passed index then return current node
                b. Increment count
                c. change current to point to next of the current.
References : https://www.geeksforgeeks.org/write-a-function-to-get-nth-node-in-a-linked-list/'''


# Returns data at given index in linked list 
def getDataAtNthIndex(self, index): 
    current = self.head # Initialise temp 
    count = 0 # Index of current node 
  
    # Loop while end of linked list is not reached 
    while (current): 
        if (count == index): #If the current index holds the data to be found
            return current.data 
        count += 1   #Increment  the value of count
        current = current.next #Shift the pointer to next node
  
        # if we get to this line, the user was asking 
        # for a non-existent element so we assert fail 
    assert(False) 
    return 0; 
