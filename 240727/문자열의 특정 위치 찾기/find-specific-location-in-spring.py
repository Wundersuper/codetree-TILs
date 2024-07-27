string, a = input().split()

leng = len(string)
start_idx = -1

for i in range(leng-1):
    if string[i] == a:
        start_idx = i
        break

if start_idx == -1:
    print('No')
else:
    print(start_idx)