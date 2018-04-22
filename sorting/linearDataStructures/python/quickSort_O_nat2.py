# Quick sort implementation for lineal structures
# based on pseudo code of page 170 of book
# Introduction to algorithms MIT press
# Import random lib
import random
# the array which is defined in the book as A[p...r]
# where arrays start at index 0 to r-1
#A = [random.randint(0,11) for r in xrange(9)]
A = [9, 10, 6, 8, 11, 6, 4, 6, 2]
#A = [2,8,7,1,3,5,6,4]
def partition(array, p, r ):
    x = array[r]
    i=p-1
    # observe that we will start from the index given
    # by p and go until r
    #print "range "+str(range(p,r))
    for j in range(p,r):
        if(array[j]<=x):
            i+=1
            # swap by xors which saves the use of temp :)
            # xor thows zero if you want to swap the same item j=i
            if(j==i):
                array[i]=array[i]
            else:
                array[i]=array[i]^array[j]
                array[j]=array[j]^array[i]
                array[i]=array[i]^array[j]
            #print array         
    # another swap with xors to avoid use of temp :)
    if(r==(i+1)):
        array[r]=array[r]
    else: 
        array[i+1] = array[i+1]^array[r]
        array[r] = array[r]^array[i+1]
        array[i+1] = array[i+1]^array[r]
    # return pivot
    #print "\narray in partition with i="+str(i+1)+"\n"
    #print array
    return i+1
            
def quickSort(array,p,r):    
    if(p<r):
        q = partition(array, p ,r)
        #print "p="+str(p)+" q="+str(q)+" r="+str(r)+"\n"
        # recursively call the function but now we have
        # q which is the pivot in which we will divide the
        # array with the approach of divide and conquer       
        # Observe we part from begining array to pivot
        #print "array         "+str(array)
        #print "quickSort(array, "+str(p)+", "+str(q)+" - 1)\n"
        array = quickSort(array, p, q - 1)
        #print "array after 1 "+str(array)
        # Observe we part from pivot to end of array
        #print "quickSort(array, "+str(q)+"+1, "+str(r)+")\n"
        array = quickSort(array, q + 1, r)
        #print "array after 2 "+str(array)
    return array

print "The array unsorted\n"
print A
OA = list(A)
print "\nThe array sorted by Quick sort\n"
# In this case the quick sort algorithm you choose p and r
# which will affect the effectivity of the algorithm
# define p=0 which means the beggining of the array
p=0
# define r=last index of the array
r=len(A)-1
print "The p="+str(p)+" and the r="+str(r)+"\n"
print quickSort(A,p,r)
print A
print "original array"
print OA
