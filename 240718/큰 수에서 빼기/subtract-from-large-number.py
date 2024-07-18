n = input()
a = int(n.split()[0])
b = int(n.split()[1])
if a < b:
    print(b - a)
else:
    print(a - b)