x,y,z = input("세 변의 길이를 입력 : ").split()
x = int(x); y = int(y); z = int(z)


if x <= 0 or y <= 0 or z<= 0 :
    print("0 이하의 값이 입력되었음!!")
else :
    if (x+y<=z and (x<=z,y<=z)) or (x+z<=y and (x<=y,z<=y)) or (y+z<=x and (y<=x,z<=x)) :
        print("삼각형이 아님")
    elif x==y==z :
        print("정삼각형임")
    elif x==y or x==z or y==z :
        print("이등변 삼각형임")
    elif (x*x)+(y*y)==z*z or (x*x)+(z*z)==y*y or (z*z)+(y*y)==x*x :
        print("직각 삼각형임")
    else :
        print("일반 삼각형임")
             

    
    
    
