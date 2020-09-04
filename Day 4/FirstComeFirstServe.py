# Recursive Approach

# Problem statement : Write a function to check if a restaurant serves first come , first serve basis
# Assumptions: 1)There are three lists dine_in_orders , take_out_orders , served_orders
            #  2)The orders number will not be ordered and are randomly assigned
            #  3)They are given as lists
''' Input format :  Three lists 
    Output Format:  True/False
    Edge cases   :  1) When one or both the lists are empty
                    2) If few orders were take away and not marked in the being served list'''

def is_first_come_first_serve(take_out_orders , dine_in_orders , served_orders):
    
    if len(served_orders) == 0:
        return True
    
    if len(take_out_orders) and take_out_orders[0] == served_orders[0]:
        return is_first_come_first_serve(take_out_orders[1:],dine_in_orders,served_orders[1:])

    elif len(dine_in_orders) and dine_in_orders[0] == served_orders[0]:
        return is_first_come_first_serve(take_out_orders ,dine_in_orders[1:],served_orders[1:])

    else:
        return False
    

take_out_sample = [17 ,8 ,24]
dine_in_sample = [12 ,19 ,2]
served_sample = [17 ,8 ,12 ,19 ,24 ,2]

print(is_first_come_first_serve(take_out_sample , dine_in_sample ,served_sample))
     
