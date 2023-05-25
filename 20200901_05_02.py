h,r = input("원기둥의 높이 h와 밑면의 반지름 r을 입력 : ").split()
h = float(h); r = float(r)
import math
s = (2*(math.pi)*r*h) + (2*(math.pi)*r*r)
print("높이가 {:.2f}이고 반지름이 {:.2f}인 원기둥의 겉넓이는 {:.4e}입니다." .format(h,r,s))
print("원기둥의 겉넓이가 10 이상입니까?", s>=10)
