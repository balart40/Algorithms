
# Algorithm to print sum of two to arrays

def printer(arrayA, arrayB):
    for itemA in arrayA:
        for itemB in arrayB:
            print (itemA+itemB)
        
arrayA = [1,2,3,4,5,6,7,8,9]

arrayB = [1,1,2,3,5,8,12,20,32,52,84]

printer(arrayA, arrayB)
