def change(c,t):
    n=len(c)
    k=[[0 for x in range(t+1)] for x in range(n+1)]
    for x in range(n+1):
        for y in range(t+1):
            if x==0 and y!=0:
                k[x][y]=t
            elif y==0 :
                k[x][y]=0
            elif c[x-1] <= y: 
                k[x][y] = min( k[x-1][y], k[x][y-c[x-1]]+1) 
            elif c[x-1] > y :
                k[x][y] = k[x-1][y]
    for i in range(1,n+1):
        for j in range(t+1):
            print(k[i][j],end=" ")
        print("\n")
    return k[x][y]

c=[1,4,6]
t=8
print(change(c,t))