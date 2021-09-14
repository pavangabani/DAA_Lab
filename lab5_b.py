def knapsack_01_weight(w_v,c):
    i=0
    v=0
    while c-w_v[i][0]>=0:
        c=c-w_v[i][0]
        v=v+w_v[i][1]
        i=i+1 
    return v

def knapsack_01_value(w_v,c):
    i=0
    v=0
    l=len(w_v)
    while i<l:
        if c>=w_v[i][0]:
            c=c-w_v[i][0]
            v=v+w_v[i][1]
        i=i+1
    return v

def knapsack_01_v_w(w_v,c):
    i=0
    v=0
    l=len(w_v)
    while i<l:
        if c >= w_v[i][0]:
            c=c-w_v[i][0]
            v=v+w_v[i][1]
        i=i+1
    return v

w_v=[(2,10),(5,60),(3,3),(7,28)]
c=8
a=sorted(w_v,key=lambda x:x[0])
print(" 01_knapsack_by_weight :")
print(a)
print(knapsack_01_weight(a,c))

b=sorted(w_v,key=lambda x:x[1],reverse=True)
print(" 01_knapsack_by_value :")
print(b)
print(knapsack_01_value(b,c))

c1=sorted(w_v,key=lambda x:x[1]/x[0],reverse=True)
print(" 01_knapsack_by_v/w :")
print(c1)
print(knapsack_01_v_w(c1,c))

