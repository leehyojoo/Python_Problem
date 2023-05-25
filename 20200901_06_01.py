x,y,z = input("실수 세 개 입력: ").split()
x = float(x); y = float(y); z = float(z)

if x<=y<=z or z<=y<=x :
    mid = y
elif x<=z<=y or y<=x<=x :
    mid = z
elif z<=x<=y or y<=x<=z :
    mid = x
    
print("******************************************")
print("중간 값 :", mid)
