D = {}
for i in range(0,8) :
    T = input("Enter plyer info : ")
    T = T.split()
    T[1] = int(T[1]); T[2] = int(T[2])
    D[I[0]] = [T[1],T[2],T[3]]
Ls = []; sd = []; so = []; Ln = []; nd = []; no = []
L = list(D.items())
for k in range(len(L)):
    if L[k][1][2] == "South":
        Ls.append(L[k]); sd.append(L[k][1][0]); so.append(L[k][1][1])
    elif L[k][1][2] == "North":
        Ln.append(L[k]); nd.append(L[k][1][0]); no.append(L[k][1][1])
print()
print("South Team Info : DF =",sum(sd), "OF  =",sum(so))
for k in range(len(Ls)):
    print(Ls[k][0],': DF =',Ls[k][1][0],', OF =',Ls[k][1][1])
    print()
print("North Team Info : DF =",sum(nd), "OF  =",sum(no))
for k in range(len(Ln)):
    print(Ln[k][0],": DF =",Ln[k][1][0],", OF =",Ln[k][1][1]); print()
for a in range(5):
    N = input("*********** Enter names to swap :")
    if len(N) == 0:
        break
    else:
        n1, n2 = N.split()
        if D.get(n1) == None or D.get(n2) == None:
            print('Not exist player!')
            print()
        elif D.get(n1)[2] == D.get(n2)[2]:
            print(n1,'and',n2,'are same team!')
            print()
        else:
            del Ls[:]; del sd[:]; del so[:]
            del Ln[:]; del nd[:]; del no[:]
            b = D.get(n1)[2]
            D.get(n1)[2] = D.get(n2)[2]
            D.get(n2)[2] = b
            L = list(D.items())
            for i in range(len(L)):
                if L[i][1][2] == 'South':
                    Ls.append(L[i])
                    sd.append(L[i][1][0])
                    so.append(L[i][1][1])
                elif L[i][1][2] == 'North':
                    Ln.append(L[i])
                    nd.append(L[i][1][0])
                    no.append(L[i][1][1])
    print()
    print("South Team Info : DF =",sum(sd), "OF  =",sum(so))
    for m in range(len(Ls)):
        print(Ls[m][0],': DF =',Ls[m][1][0],', OF =',Ls[m][1][1])
    print()
    print("North Team Info : DF =",sum(nd), "OF  =",sum(no))
    for m in range(len(Ln)):
        print(Ln[m][0],': DF =',Ln[m][1][0],', OF =',Ln[m][1][1])
