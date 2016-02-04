tc = int(raw_input())
for t in range(0,tc):
    a,b = raw_input().split()
    mat = []
    for i in range(0,int(a)):
        mat.append(raw_input())
    c,d = raw_input().split()
    pat = []
    for i in range(0,int(c)):
        pat.append(raw_input())
    m = []
    n = []
    for i in range(0,int(a)):
        for j in range(0,int(b)):
            if int(pat[0][0]) == int(mat[i][j]):
                if int(d) <= int(b) - j and int(c) <= int(a) - i:
                    m.append(i)
                    n.append(j)
    a = -1
    b = -1
    noteq = 0
    yes = 0
    for i in range(0,len(m)):
        for j in range(m[i],m[i]+int(c)):
            a+=1
            if noteq != 0:
                break
            for k in range(n[i],n[i]+int(d)):
                b+=1
                if mat[j][k]!=pat[a][b]:
                    noteq += 1
                    break
            b=-1
        a=-1
        if noteq!=0:
            noteq=0
        else:
            yes+=1
            
    if yes != 0:
        print 'YES'
    else:
        print 'NO'
