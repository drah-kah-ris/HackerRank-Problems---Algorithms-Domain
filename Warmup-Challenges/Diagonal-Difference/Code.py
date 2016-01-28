def dg_diff(mat,n):
    d1 = 0
    for i in range(0,n):
        d1 = d1 + int(mat[i][i])
    d2 = 0
    a = n - 1
    for i in range(0,n):
        d2 = d2 + int(mat[i][a])
        a = a - 1
    return d1 - d2    
        
n = int(raw_input())
mat = []
for i in range(0,n):
    mat.append(raw_input().split())

print abs(dg_diff(mat,n))
