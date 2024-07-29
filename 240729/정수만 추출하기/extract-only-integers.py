s1, s2 = input().split()

leng1 = len(s1)
leng2 = len(s2)

num1 = ''
num2 = ''

for i in range(leng1):
    if s1[i] >= '0' and s1[i] <= '9':
        num1 += s1[i]
    else:
        break

for i in range(leng2):
    if s2[i] >= '0' and s2[i] <= '9':
        num2 += s2[i]
    else:
        break

print(int(num1) + int(num2))