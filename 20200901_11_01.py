fp_w1 = open('20200901_in_num.txt','w')
fp_w = open('20200901_out_num.txt','w')

k=1
import random

for k in range(1,11) :
    x = random.random()+2.0
    print('%.2f ' %x, file=fp_w1, end='')
    k = k+1

print('',file=fp_w1)

k=1
for k in range(1,11) :
    x = random.random()+2.0
    print('%.2f ' %x, file=fp_w1, end='')
    k = k+1

fp_w1.close()

fp_r = open('20200901_in_num.txt','r')

for s in fp_r :
    num = list(float(x) for x in s.split())

    
    for i in range(len(num)) :
        sq = num[i] * num[i]
        print('  %d' %sq, file=fp_w, end = '')
    fp_w.write('\n')

fp_r.close(); fp_w.close()

