a = input("첫번째 문자열을 입력 : ")
b = input("두번째 문자열을 입력 : ")

A = list(a)
B = list(b)
A1 = sorted(A, reverse=True)
B1 = sorted(B, reverse=True)

if A1==B1 :
    print(a, ",", b, "는 anagram입니다.")
else :
    print(a, ",", b, "는 anagram이 아닙니다.")
