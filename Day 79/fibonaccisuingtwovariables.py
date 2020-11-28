''' Problem statement : Print Fibonacci series using two variables'''

def fibonaccisuingtwovariables(length):
    first_num_of_sequence = 0
    second_num_of_sequence = 1
  
    if(range >= 0):
        print(first_num_of_sequence, end = '')
    
    if(range >= 1):
        print(second_num_of_sequence, end = '')
    
    for range in (2, length+1):
        print(first_num_of_sequence+second_num_of_sequence, end= '')
        second_num_of_sequence = first_num_of_sequence + second_num_of_sequence
        first_num_of_sequence = second_num_of_sequence - first_num_of_sequence

if __name__ == '__main__':
    fibonaccisuingtwovariables(25)
