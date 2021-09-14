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
     
a=[10,9,8,7,6,5,4,3,2,1]
merge_sort(a)
print(a)