# MERGE SORT ALGORITHM IMPLEMENTATION
import math
#   [0 ,1,2,3,4,5,6,7]
A = [10,9,8,7,6,5,4,3]
#A = [10,9,8,7,6,5,4,3,2]

def merge(array, p, q, r):
    left = q - p+1#n1
    right = r - q#n2
    if((left<=0) or (right<=0)):
        return
    #print "\nCALL TO MERGE"
    #print "r="+str(r)+" p="+str(p)+" q="+str(q)+" left="+str(left)+" right="+str(right)
    #print "array "+str(array)
    L = [None]*(left)
    R = [None]*(right)
    for i in range(left):
        #print "ii="+str(i)
        L[i] = array[p+i]
    #print "L "+str(L)
    for j in range(right):
        #print "jj="+str(j)
        R[j] = array[q+j+1] 
    #print "R "+str(R)
    i = 0
    j = 0
    for k in range(p,r+1):
        #print "i="+str(i)
        #print "j="+str(j)
        #print "k="+str(k)
        #print array
        if(j==len(R)):
            array[k:k+len(L[i:])]=L[i:]
            break
        elif(i==len(L)):
            array[k:k+len(R[j:])]=R[j:]                        
            break
        elif(L[i] <= R[j]):
            array[k] = L[i]
            i = i + 1
        else:
            array[k] = R[j]
            j = j + 1

def mergesort(array, p, r):
    if(p < r):
        #print "\np < r = "+str(p<r)
        #print "CALL TO MERGESORT"
        q = int(math.floor((p + r) / 2))
        #print "current q="+str(q)+" current p="+str(p)+" current r="+str(r)
        mergesort(array, p, q)
        mergesort(array, q+1, r)
        merge(array, p, q, r)
    return array

p = 0
#r = (range(len(A)))[-1]
r = len(A)-1
# print r
print "Array unsorted\n" 
print A
print "\nArray sorted with merge sorth arlgorithm"
print mergesort(A,p,r)
