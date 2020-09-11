''' Problem Statement : https://www.codechef.com/problems/CNOTE
    Basic Concepts(pre-requisites) : xrange and range function
                                     Basic AND and OR operation'''
# for the number of test cases
T = input()

for i in range(0,int(T)):
    # taking input for the X pages long poetry  , Y for the number of pages left in chef notebook
    # K for the rubles/money left with the chef , N for the number of notebooks available with the shopkeeper
    
    X, Y, K, N  = map(int,input().strip().split())
    
    # An empty list for storing the values of Price of notebook by P
    # and cost of that particular notebook by C
    
    books = []
    # Taking inputs for price/cost and pages of N notebooks
    for j in range(N):
        P,C = map(int,input().strip().split())
        books.append((P, C))
    
    # Checking for the required conditions
    for P, C in books:
        # Clearly for the chef to be lucky , the notebook to be bought should have greater than/equal to X-Y pages and its cost should be less than
        # Total money remaining with him
        if P >=X-Y and C <=K:
            print('LuckyChef')
            break
        else:
            print('Unlucky Chef')
            break