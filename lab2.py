def linearsearch(a,n,x):
    for i in range(0,n):
        if(x==a[i]):
            return i
        if(i==n-1):
            return -1
def binarysearch_a(a,l,h,x):
    if(h>=l):
        m=(l+h)//2
        if(x<a[m]):
            return binarysearch_a(a,l,m-1,x)
        if(x==a[m]):
            return m
        if(x>a[m]):
            return binarysearch_a(a,m+1,h,x)
    else:
        return -1
def binarysearch_b(a,l,h,x): 
    while l<=h: 
        m = (h + l) // 2
        if a[m] < x: 
            l= m + 1
        if a[m]==x:
            return m
        if a[m] > x: 
            h = m - 1
    return -1
    

    

import numpy as np
import time

n=10000

a =np.arange(1,n+1)
b =np.arange(n,0,-1)
c =np.random.randint(n,size=(n))  


print(linearsearch(c,10000,8775))
print(binarysearch_a(a,0,10000,3535))
print(binarysearch_b(a,0,10000,4353))




