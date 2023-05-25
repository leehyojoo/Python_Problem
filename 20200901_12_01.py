list1=input('enter list1 elements : ').split()
list2=input('enter list2 elements : ').split()

i=0
for i in range(len(list1)) :
    list1[i] = int(list1[i])
i=0
for i in range(len(list2)) :
    list2[i] = int(list2[i])

list3=list1+list2

def counting() :
    list4=[]
    i=0
    while i<len(list3) :
        a=list3.count(list3[i])
        if a!=1 :
            list4.append(list3[i])
        i=i+1
    list4=set(list4)
    list4=list(list4)

    if list4==[] :
        return True
    else :
        return False, list4

a = counting()
if a == True :
    print('No overlapping elements')
else :
    print(a[1], 'overlapping elements')

        

    
            
        
