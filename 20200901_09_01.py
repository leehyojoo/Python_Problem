n = input("Enter maximun number of data : ")
n = int(float(n))
L = []
T = []

for x in range(n):
    x = input("Enter a number : ")
    if x == '0':
        break
    else:
        x = int(float(x))
        X = abs(x)
        t = True
    for k in range(2,X):
        if X % k == 0:
            t = False
    if t == False:
        L.append(x)
        
if len(L) == 0:
    print("입력 데이터가 없습니다")
else:
    print("입력 데이터 :",L)
    i = 0
    for i in range(len(L)-1):
            if L[i] >= L[i+1]:
                T.append(i)
                for k in range(len(T)-1):
                    for m in range(k+1,len(T)):
                        if L[T[k]] >= L[T[m]]:
                            i = T[k]
                        else:
                            i = T[m]
            else:
                i = i+1
    print("가장 큰 값을 가지는 원소의 인덱스 :",i)
    
    
