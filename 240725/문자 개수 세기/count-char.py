str1 = input()

a = input()

cnt = 0

for i in range(len(str1)):
    if str1[i] == a:
        cnt += 1

print(cnt)