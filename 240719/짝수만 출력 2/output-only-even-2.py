n = input()
a = int(n.split()[1])
b = int(n.split()[0])

i = b
while i >= a:
    print(i, end = " ")
    i -= 2