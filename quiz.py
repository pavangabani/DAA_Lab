#id_no_18CP047_name_pavan_gabani
#LCS function
def LCS(x,y,lx,ly):
    if lx==0 or ly==0:                             
        return 0
    elif x[lx-1] == y[ly-1]:                           
        return 1 + LCS(x, y, lx-1, ly-1)
    else:                                        
        return max(LCS(x , y ,lx ,ly-1) , LCS(x, y, lx-1,ly))

#file a.txt
x=[]
x_h=[]
with open('a.txt') as f:
    x= [list(line.rstrip()) for line in f]
l=len(x[0])
t=0
i=0

f = open("a.txt", "r")
print("file_1 :")
print(f.read())

#calculate_hash_values
while i<l:
    for j in range(5):
        if(i<l):
            t=t+ord(str(x[0][i]))
            i=i+1    
    t=t/5
    x_h.append(t)
print("file_a_hash :")
print(x_h)

#hash_values_store_in_file_a_hash.txt
with open('a_hash.txt', 'w') as f:
    for item in x_h:
        f.write("%s\n" % item)

print(" ")

#file_2
y=[]
y_h=[]
with open('b.txt') as f:
    y= [list(line.rstrip()) for line in f]
l=len(y[0])
t=0
i=0

f = open("b.txt", "r")
print("file_2 :")
print(f.read())

#calculate_hash_values
while i<l:
    for j in range(5):
        if(i<l):
            t=t+ord(str(y[0][i]))
            i=i+1    
    t=t/5
    y_h.append(t)
print("file_b_hash :")
print(y_h)

#y_h_store_in_file_a_hash.txt
with open('y_hash.txt', 'w') as f:
    for item in y_h:
        f.write("%s\n" % item)

print(" ")

#compare_two_file 
r=LCS(x_h,y_h,len(x_h),len(y_h))

if len(x_h)>len(y_h):
    per=r*100/len(x_h)
else:
    per=r*100/len(y_h)

print("Compare :")
print(per,"% files are same")