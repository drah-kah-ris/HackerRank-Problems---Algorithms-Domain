def fact(n):
    f = 1
    m = n
    for i in range(0,n):
        f = f * m
        m = m - 1
    return f

n = int(raw_input())
print fact(n)
