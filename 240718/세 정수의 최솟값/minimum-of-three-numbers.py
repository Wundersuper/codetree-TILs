n = input()
a = int(n.split()[0])
b = int(n.split()[1])
c = int(n.split()[2])

if a <= b and a <= c:
    print(a)
elif b <= a and b <= c:
    print(b)
else:
    print(c)