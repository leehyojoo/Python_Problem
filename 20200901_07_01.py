L = [12, 29, 30, 0 , 99]
a = input("리스트 L에 추가할 data를 입력 : ")


if a.isnumeric() :
    a = float(a)
    if a>=0 and a==int(a) :
        if L.count(a)!=0 :
            print("이미 존재하는 데이터입니다.")
        else :
            a = int(a)
            L[len(L):len(L)]=[a]
            print(L)
    else :
        print("0이상의 양의 정수 숫자 데이터만 허용합니다.")
else :
    print("0이상의 양의 정수 숫자 데이터만 허용합니다.")
    
