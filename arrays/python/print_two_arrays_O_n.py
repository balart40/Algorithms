# Algorithm to print to arrays

def printer(arrayA, arrayB):
    for item in arrayA:
        print item
    print "\n"
    for item in arrayB:
        print item
        
arrayA = [1,2,3,4,5,6,7,8,9]

arrayB = [1,1,2,3,5,8,12,20,32,52,84]

printer(arrayA, arrayB)
