def knapsack(v,w,tw):
    n=len(v)
    k=[[0 for x in range(tw+1)] for x in range(n+1)]
    for x in range(n+1):
        for y in range(tw+1):
            if x==0 or y==0 :
                k[x][y]=0
            elif w[x-1] <= y: 
                k[x][y] = max( k[x-1][y], v[x-1] + k[x-1][y-w[x-1]]) 
            elif w[x-1] > y :
                k[x][y] = k[x-1][y]
    for i in range(n+1):
        for j in range(tw+1):
            print(k[i][j],end=" ")
        print("\n")
    return k[x][y]

v=[1,6,18,22,28]
w=[1,2,5,6,7]
tw=11
print(knapsack(v,w,tw))