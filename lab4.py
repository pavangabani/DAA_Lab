def countingSort(a,b):
    size = len(a)
    output = [0] * size
    count = [0] * (b+1)
    for i in range(0, size):
        count[a[i]] += 1
    for i in range(1, b+1):
        count[i] += count[i - 1]
    i=size-1
    while i >= 0:
        output[count[a[i]] - 1] = a[i]
        count[a[i]] -= 1
        i -= 1
    for i in range(0, size):
        a[i] = output[i]
def merge_sort(a):
    l=len(a)
    if(l>1):
        mid=l//2
        la=a[:mid]
        ra=a[mid:]
        merge_sort(la)
        merge_sort(ra)
        i = j = k = 0
        while i < len(la) and j < len(ra): 
            if la[i] < ra[j]: 
                a[k] = la[i] 
                i+= 1
            else: 
                a[k] = ra[j] 
                j+= 1
            k+= 1 
        while i < len(la): 
            a[k] = la[i] 
            i+= 1
            k+= 1 
        while j < len(ra): 
            a[k] = ra[j] 
            j+= 1
            k+= 1
print("merge sort :")
a=[10,9,8,7,6,5,4,3,2,1]
merge_sort(a)
print(a)

print("counting sort :")
b=[5,7,77,55,24,21,78,65,44,3]
max_of_b=78
countingSort(b,max_of_b)
print(b)

