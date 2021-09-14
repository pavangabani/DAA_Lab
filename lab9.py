import sys
def chain_matrix(p,l):
    n=l
    m=[[0 for i in range(l)] for j in range(l)]
    for x in range(2,l):
        for y in range(1,l-x+1):
            i=y
            j=x+y-1
            m[i][j]=sys.maxsize
            for k in range(i, j):                 
                q = m[i][k] + m[k + 1][j] + p[i-1]*p[k]*p[j] 
                print("i ",i," j ",j," k ",k,"-->  ", "m",i,k," + m",k+1,j," + p",i-1,"p",k,"p",j," = ",m[i][k] , m[k + 1][j] , p[i-1]*p[k]*p[j]," | total ",q)
                if q < m[i][j]: 
                    m[i][j] = q
            print("loop k end") 
    print(m)
    return m[1][n-1] 

arr = [13, 5, 89, 3,34] 
size = len(arr)  
print("Minimum number of multiplications is " +str(chain_matrix(arr, size))) 

