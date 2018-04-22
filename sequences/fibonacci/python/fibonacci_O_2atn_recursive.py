# Algorithm that finds the nth number of 
# the fibonacci sequence, recursive implementation

def fib(n):
    if ((n==0) or (n==1)):
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
n=8
print "The "+str(n)+"th number of the fibonacci sequence is"
print fib(n)

# The order of this algorithm is:
# E O (2^n)
# is 2^n, is exponentil
# Due to the Master´s theroem
# We have 2 branches (2 recursive calls)
# and n is the n th fibonacci number we seek
