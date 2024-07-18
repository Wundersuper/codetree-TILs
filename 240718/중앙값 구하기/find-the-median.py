n = input()
a, b, c = int(n.split()[0]), int(n.split()[1]), int(n.split()[2])

if a >= b:
    if a <= c:
        print(a)
    else:
        if b >= c:
            print(b)
        else:
            print(c)
else:
    if a >= c:
        print(a) 
    else:
        if b >= c:
            print(c)
        else:
            print(b)