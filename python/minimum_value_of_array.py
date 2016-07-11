# Algorithm for finding the minimum number in an array
import math
import random

def min(array):
    min=float("Inf")
    # for loop which will go through n values of array
    for i in range(len(array)):
        if array[i]<=min:
            min= array[i]
    return min

A = [random.randint(-11,11) for r in xrange(10)]

print "The min for the array: \n"
print A
print "\nUsing the min alfgorithm is: "
print min(A)

# The order of this Algorithm:
# E O (n)
# The order of this algorith is n (linear)
# Since the for loop wil go through all the n values
# Of an array of length n
