L = input("two nums : ").split()

if len(L) != 2 :
    print("Number of input data is not 2")
else :
    a = L[0]; b =L[1]
    if a.isnumeric() and b.isnumeric() :
        a = int(a); b = int(b)
        a_s = set()
        for i in range(1,a+1):
            if a % i == 0 :
                a_s.add(i)
        b_s = set()
        for i in range(1,b+1):
            if b % i == 0 :
                b_s.add(i)
        print("first num divisor : ", a_s)
        print("second num divisor : ", b_s)
        ab_s = a_s.intersection(b_s)
        print("{} & {} common divisor : {}".format(a,b,ab_s))
        if a==0 or b==0 :
            print("Not exist greatest common divisor")
        else :
            print("{} & {} greatest common divisor : {}".format(a,b,max(ab_s)))
    else :
        print("Input data is not inerger or not positive interger")
        
        
                
                
            
        
