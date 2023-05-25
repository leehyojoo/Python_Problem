print('*Menu********************************')
print('1. 성적 관리(입력 형태는 name score1 score2')
print('2. 학생 정보 출력')
print('3. 학생 정보 삭제')
print('4. 프로그램 종료')
print('*************************************')


SS=[['name','mid','final','grade']]
Lname = []

def menu1() :
    L = input('이름 중간 기말 성적 입력 : ').split()
    if len(L)!=3 :
        print('입력 데이터 갯수 오류입니다.')
    else :
        name=L[0]
        mscore=int(L[1])
        fscore=int(L[2])
        if L[0] not in Lname :
            Lname.append(name)
            score = (0.4*mscore)+(0.6*fscore)
            if score>=90 :
                grade='A'
            elif score>=80 :
                grade='B'
            elif score>=70 :
                grade='C'
            else :
                grade ='D'
            SS.append([name,mscore,fscore,grade])
        else :
            print('이미 존재하는 학생 정보입니다.')

def menu2() :
    if SS==[['name','mid','final','grade']] :
        print('입력된 학생 정보가 없습니다')
    else :
        print(SS[0][0], SS[0][1], SS[0][2], SS[0][3])
        print('-------------------------------')
        i=1
        while i<len(SS) :
            print(SS[i][0], SS[i][1], SS[i][2], SS[i][3])
            i=i+1
        
def menu3() :
    if SS==[['name','mid','final','grade']] :
        print('입력된 학생 정보가 없습니다')
    else :
        name=input('삭제할 학생의 이름을 입력 : ')
        for i in range(len(SS)) :
            if name in SS[i][0] :
                print(name,'학생의 정보를 삭제했습니다.')
                SS.remove(SS[i])
                a=0
            else :
                a=1
        if a==1 :
            print('정보가 없는 학생입니다.')
        
def menu4() :
    print('프로그램을 종료합니다')

while(True) :
    k = input('메뉴 1,2,3,4번 중 하나 선택 : ')
    if k=='1' :
        a=menu1()
    elif k=='2' :
        a=menu2()
    elif k=='3' :
        a=menu3()
    elif k=='4' :
        a=menu4()
        break
    else :
        print('없는 번호의 명령어입니다. 다시 선택하세요.')
