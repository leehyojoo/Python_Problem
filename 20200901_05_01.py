x = input("문장입력 : ")
y = input("문장에서 찾는 단어 입력 : ")

print("%s 문장에서는 %s 단어가 %d번 사용되었습니다." %(x,y,x.count(y)))
print("")
print("%s 문장에서 %s 단어를 제거한 문장 : " %(x,y))
print("    %s" %x.replace(y,""))

