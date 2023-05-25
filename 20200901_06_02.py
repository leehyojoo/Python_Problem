x,y,z = input("수식 입력 : ").split()
x = float(x)
z = float(z)

if y == "+" :
    print("%.2f + %.2f = %.2f" %(x,z,(x+z)))
elif y == "-" :
    print("%.2f - %.2f = %.2f" %(x,z,(x-z)))
elif y == "*" :
    print("%.2f * %.2f = %.2f" %(x,z,(x*z)))
elif y == "/" :
    if z != 0 :
        print("%.2f / %.2f = %.2f" %(x,z,(x/z)))
    if z == 0 :
        print("0으로 나누기를 수행할 수 없습니다")
else :
    print("%s 는 지원하지 않는 연산자입니다" %y)
