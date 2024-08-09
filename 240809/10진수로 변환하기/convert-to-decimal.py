n = list(input())
num = 0

for i in range(len(n)):
    num = num * 2 + int(n[i])

print(num)