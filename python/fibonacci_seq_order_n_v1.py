# Algorithm that finds the nth number of 
# the fibonacci sequence

def fib(n):
    # Initialize array to None
    array = [None]*(n+1)
    print array
    array[0] = 1
    array[1] = 1
    # Generate all fibonacci numbers until the nth
    for i in range(2,n+1):
        array[i]=array[i-1]+array[i-2]
    print array
    # return nth value
    number = array[n]
    return number
    
n=10
print "The "+str(n)+"th number of the fibonacci sequence is"
print fib(n)

# The order of this algorithm is:
# E O (n )
# is N (linear)
# Since the for loop goes through all the values
# of the array of length n
