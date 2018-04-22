# Algorithm that finds the nth number of 
# the fibonacci sequence, recursive implementation

def fib(k, cache):
    if ((k==0) or (k==1)):
        return 1
    elif(cache[k-1]!=0):
        return cache[k-1]+cache[k-2]
    else:
        cache[k-2]=fib(k-2, cache)
        cache[k-1]=fib(k-1, cache)
        cache[k]=cache[k-2]+cache[k-1]
        #print cache
    return cache[k]
    
n=8
cache = [0]*(n+1)
cache[0]=1
cache[1]=1
print "initial cache"
caches = [k for k in range(n+1)]
print caches        
print cache
print "The "+str(n)+"th number of the fibonacci sequence is"
print fib(n, cache)
# The order of this algorithm is:
# E O (n)
# is n, is Lineal
# Due to the cache we no longer repeat existing operations
