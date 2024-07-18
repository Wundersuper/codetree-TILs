n = input()
a = int(n.split()[0])
b = int(n.split()[1])
c = int(n.split()[2])

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
elif b > c:
    if b > a:
        print(b)
    else:
        print(a)
else:
    print(c)