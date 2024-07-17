n = input()
a = int(n.split()[0])
b = int(n.split()[1])
a += b
b += a
print(a, b)