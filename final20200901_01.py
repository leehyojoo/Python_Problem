s = input('문장 입력 : ')
print('###################################################')
s = s.lower()
number = '0123456789'
alpha = 'qwertyuiopasdfghjklzxcvbnm'

if s=='' :
    print('')
    print('***제거 작업을 실시할 문장 내용이 없음***')
    print('중복 제거한 단어 리스트 : ',s)
else :
    i=0
    while i < len(s) :
        print(s)
        t = input('위 문장에서 제거할 문자는(영어 알파벳과 숫자는 제외)? ')
        if s=='' :
            print('')
            print('***제거 작업을 실시할 문장 내용이 없음***')
            break
        if t=='' :
            break
        if len(t)!=1 :
            print('***제거할 문자 1개만 입력***')
        elif (t in number) or (t in alpha) :
            print('***영어 알파벳과 숫자는 제거할 수 없음***')
        elif t not in s :
            print('*** {} 는 없는 문자임***' .format(t))
        else :
            index=s.find(t)
            s=list(s)
            s.remove(s[index])
            s=''.join(s)
            i=i+1
    L=s.split()
    L=set(L)
    L=list(L)
    print('중복 제거한 단어 리스트 : ',L)
