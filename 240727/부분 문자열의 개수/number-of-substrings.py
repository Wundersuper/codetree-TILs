str_a = input()
str_b = input()

len_a = len(str_a)
len_b = len(str_b)

cnt = 0
for i in range(len_a-1):
    if str_a[i:i+2] == str_b:
        cnt += 1

print(cnt)