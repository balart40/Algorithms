# Insertion sort implementation for lineal structures
# based on pseudo code of https://en.wikipedia.org/wiki/Insertion_sort
# Import random lib
import random
# the array
A = [random.randint(0,11) for r in xrange(9)]
#A = [3, 7, 4, 9, 5, 2, 6, 1]

def insertionSort(array):
    n = len(array)
    for i in range(1,n):
        j=i
        while((j>0) and (array[j-1]>array[j])):
            #print "j= "+str(j)
            # Swapping using xor so we don´t use a temp :)
            array[j-1] = array[j-1] ^ array[j]
            array[j] = array[j] ^ array[j-1]
            array[j-1] = array[j-1] ^ array[j]            
            j -= 1
        #print "j= "+str(j)+"#"+str(array)
    return array

print "The array unsorted\n"
print A
print "\nThe array sorted by insertion sort\n"
print insertionSort(A)
