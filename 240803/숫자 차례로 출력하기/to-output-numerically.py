N = int(input())

def d(n) :
    if n==0 :
        print()
        return
    print(n, end=' ')
    d(n-1)

def u(n) :
    if n==0 :
        return
    u(n-1)

    if n == N:
        print(n)
    else:
        print(n, end=' ')


u(N)
d(N)