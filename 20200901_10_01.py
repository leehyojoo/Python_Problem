import random

number = random.randint(10,20) #number만큼 랜덤 정수 a 발생
number = int(number)
L = []

for i in range(number) :
    a = random.randint(-10,10)
    L.append(a)

print("랜덤 정수 리스트 :", L)

i = 1
sum = 0

while i < 11 :
    for k in range(len(L)-1) :
        if L[k] == i :
            sum = sum + 1
    print("숫자 %d는 %d번 입력 되었습니다."%(i,sum))
    i = i + 1
    sum = 0  
