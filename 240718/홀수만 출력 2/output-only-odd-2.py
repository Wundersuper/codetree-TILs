n = input()
a = int(n.split()[1])
b = int(n.split()[0])

for i in range(b, a-1, -2):
    print(i, end = " ")