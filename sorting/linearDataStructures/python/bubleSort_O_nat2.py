# Bubble sort implementation for lineal structures
# based on pseudo code of https://en.wikipedia.org/wiki/Bubble_sort
# Import random lib
import random
# the array
A = [random.randint(0,11) for r in xrange(9)]

def bubbleSort(array):
    n = len(array)
    swapped = None
    while(swapped != False):
        swapped = False
        # arrays in python start from 0 to n-1
        # we start the indexes from 1 to n-1 with the
        # definition below
        for i in range(1,n):
            if(array[i-1]>array[i]):
                # Swapping using xor so we don´t use a temp :)
                array[i-1]=array[i-1]^array[i]
                array[i]=array[i]^array[i-1]
                array[i-1]=array[i-1]^array[i]
                swapped =  True
    return array

print "The array unsorted\n"
print A
print "\nThe array sorted by bubble sort\n"
print bubbleSort(A)
