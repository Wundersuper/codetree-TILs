string = input()
leng = len(string)

cnt = 0
for i in range(leng-1):
    if string[i:i+2] == 'ee':
        cnt += 1
print(cnt, end = " ")

cnt = 0
for i in range(leng-1):
    if string[i:i+2] == 'eb':
        cnt += 1
print(cnt)