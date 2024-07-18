n = input()
a = int(n.split()[0])
b = int(n.split()[1])

if a < b:
    print(1, end=" ")
else:
    print(0, end=" ")

if a == b:
    print(1, end=" ")
else:
    print(0, end=" ")