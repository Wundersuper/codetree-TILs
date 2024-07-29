arr = input().split()

n = int(arr[0])
A = arr[1]

cnt = 0
for i in range(n):
    s = input()

    if s == A:
        cnt += 1


print(cnt)