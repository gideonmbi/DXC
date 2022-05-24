# print the first 8 fibonacci numbers
# define a function FibonacciNumList to print the list
def FibonacciNumList(n):
    # initialize n1 and n2
    n1 = 0
    n2 = 1
    if (n < 1): # return 0 if n is 1
        return
    print(n1, end=" ") #
    for i in range(1, n): # use for loop to iterate values till 8
        print(n2, end=" ") # output values on the same line
        next = n1 + n2
        n1 = n2
        n2 = next
FibonacciNumList(8) # call the function to list values
