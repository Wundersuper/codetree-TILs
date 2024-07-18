n = input()
a = int(n.split()[0])
b = int(n.split()[1])
c = int(n.split()[2])

if b > a and b < c:
    print(1)
else:
    print(0)