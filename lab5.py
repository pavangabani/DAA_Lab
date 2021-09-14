def find(n,d):
    r =[]
    for i in range(len(d)):
        while n>=d[i]:
            n=n-d[i]
            r.append(d[i])
    return r , 'left ->', n
    
d=[1,2,7]
d.sort(reverse=True)
print(find(10,d))
