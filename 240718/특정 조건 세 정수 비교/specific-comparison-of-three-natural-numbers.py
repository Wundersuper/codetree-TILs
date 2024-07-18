n = input()
a = int(n.split()[0])
b = int(n.split()[1])
c = int(n.split()[2])

if a == min([a,b,c]):
    print(1, end = " ")
else:
    print(0, end = " ")

if a == b and b == c:
    print(1)
else:
    print(0)