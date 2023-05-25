majorB = {"computer" : [9,"R"], "math" : [2,"AS"], "elec" : [11,"R"], "psy":[1,"X"]}

a = input("학과명을 입력 : ")
b = majorB.get(a,"NotYet")

if b == "NotYet" :
    print("{}과 정보가 없습니다. GN 건물 1층에 배정합니다.".format(a))
    print("")
    item = list(majorB.items())
    item.sort()
    print("sorting : ", item)
else :
    majorB[a][0] = majorB[a][0]+1
    print("{}과는 {} 건물 {} 층으로 배정합니다.".format(a,majorB[a][1],majorB[a][0]))
    print("")
    item = list(majorB.items())
    item.sort()
    print("sorting : ", item)

