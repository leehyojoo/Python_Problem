string = input("Enter a sentence :\n")
string = string.lower()
L = string.split()

if len(L) == 0 :
    print("")
    print("No sentence")
else :
    L = set(L)
    L = list(L)
    L.sort()
    print("Non duplicate words (list) : ", L)

    x = input("Enter one character for string : ")
    L = x.join(L)
    print("Non duplicate words (string) : ", L)
    
