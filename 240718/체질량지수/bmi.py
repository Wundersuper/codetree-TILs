n = input()
h = int(n.split()[0])
w = int(n.split()[1])
b = (10000*w)//(h**2)

#출력
print(b)
if b >= 25:
    print('Obesity')