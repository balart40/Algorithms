# Algorithm that finds the nth number of 
# the fibonacci sequence
def fib(n):
    # Jut define the first fibonacci numbers
    a=1
    b=1
    # Generate all fibonacci numbers until the nth
    for i in range(2,n+1):
        c=a+b
        b=a
        a=c
    # return nth value
    number = c
    return number
    
n=8
print "The "+str(n)+"th number of the fibonacci sequence is"
print fib(n)

# The order of this algorithm is:
# E O (n )
# is N (linear)
# Since the for loop goes through all the values
# of the array of length n
