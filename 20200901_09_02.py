a = input("Enter list A numbers : ")
A = a.split(' ')
for i in range(len(A)) :
    A[i]=int(A[i])
b = input("Enter list B numbers : ")
B = b.split(' ')
for i in range(len(B)) :
    B[i]=int(B[i])

AA = []    
for k in A :
    if k not in AA :
        AA.append(k)
        
BB = []
for k in B :
    if k not in BB :
        BB.append(k)

T = []
L = AA + BB
for k in L :
    if k in AA and k in BB :
        continue
    else :
        if k not in T :
            T.append(k)
T.sort()
print(T)
