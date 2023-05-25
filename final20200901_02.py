i = 1
L=[]
import random
while i < 11 :
    k=random.randint(10,30)
    L.append(k)
    i=i+1

print('랜덤 수 : ', L)

def counting(L) :
    i=0
    Dict={}
    while i < len(L) :
        Dict[L[i]]=L.count(L[i])
        i=i+1
    return Dict

a=counting(L)
print('(1)번 함수 반환 결과 : ', a)

def counting2(a) :
    k=0
    LL=[]
    T=[]
    while k < len(a) :
        T.append(a[k][1])
        T.append(a[k][0])
        T=tuple(T)
        LL.append(T)
    LL= sorted(LL, reverse=true)
    return LL

b=counting2(a)
print('(2)번 함수 반환 결과 : ', b)
