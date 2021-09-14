def bsort(a,n):
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if(a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
def ssort(a,n):
    for i in range(0,n):
        m=i
        for j in range(i,n):
            if(a[i]>a[j]):
                m=j
        a[m],a[i]=a[i],a[m]   
def isort(a,n):
    for i in range(0,n):
        key=a[i]
        j=i-1
        while j>=0 and key<a[j]:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=key 

import numpy as np
import time

n=10000

a =np.arange(1,n+1)
a =np.arange(n,0,-1)
a =np.random.randint(n,size=(n))  

start = time.time()
a =np.random.randint(n,size=(n)) 
bsort(a,n)
end = time.time()
print(f"Runtime of the bubblesort is {end - start}")

start = time.time() 
a =np.random.randint(n,size=(n)) 
ssort(a,n)
end = time.time()
print(f"Runtime of the selectionsort is {end - start}")

start = time.time()
a =np.random.randint(n,size=(n)) 
isort(a,n)
end = time.time()
print(f"Runtime of the insertiononsort is {end - start}")
