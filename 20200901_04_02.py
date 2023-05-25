x = "!abcABCdEF!!aBCDeFAbC!!"

x = x.lower()
a = "abc"; b = "def"
x1 = x.count(a); x10 = x.find(a)
x2 = x.count(b); x20 = x.find(b)

print('"%s 문자열 : %d 인덱스, %d 번 존재"' %(a, x10, x1))
print('"%s 문자열 : %d 인덱스, %d 번 존재"' %(b, x20, x2))

c = "!"
x = x.replace(c,"")
print("%s가 제거된 문자열 : %s" %(c, x))
