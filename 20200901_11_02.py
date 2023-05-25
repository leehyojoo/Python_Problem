fp_r = open('11_2_in.txt','r')
fp_w = open('20200901_out.txt','w')

k = 1
for s in fp_r :
    t = list(int(x) for x in s.split())
    h = t[0]
    m = t[1]
    a = t[2]

    ah = a//60
    am = a%60

    if a>=0 :
        h = h + ah
        m = m + am

        if h<0 :
            h = h + 24
        if h>24 :
            h = h - 24
        if m>=60 :
            h = h+1
            m = m-60
            if h<0 :
                h = h + 24
            if h>24 :
                h = h - 24
    else :
        h = h + ah
        m = m + am

        if h<0 :
            h = h + 24
        if h>24 :
            h = h - 24
        if m>=60 :
            h = h+1
            m = m-60
            if h<0 :
                h = h + 24
            if h>24 :
                h = h - 24

    print('%d: 최종 시간 = %d:%d\n' %(k,h,m), file=fp_w)
    k = k + 1

fp_r.close(); fp_w.close()
