L = input("랜덤하게 원하는 횟수만큼 문자 입력 : ")

if L =='' :
    print('입력된 데이터가 없습니다')
else :
    L = list(L)
    i = 0
    sum = 1
    LL = []
    D = []
    
    while i < len(L) :
        if L[i] not in LL :
            for k in range(0,len(L)-1) :
                if L[i] == L[k+1] :
                    sum = sum + 1
                    LL.append(L[i])
            D.append((sum,L[i]))
        i = i + 1
        sum = 0

    k = 0
    while k < len(D) :
        print("문자 %s는 %d번 입력 되었습니다." %(D[k][1],D[k][0]))
        k =  k + 1


    D1 = sorted(D, reverse=True)
    print("입력 횟수 기준 내림차순 정렬 : ",D1)
