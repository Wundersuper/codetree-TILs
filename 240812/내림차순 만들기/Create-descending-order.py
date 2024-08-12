n = int(input()) #원소의 수
arr = list(map(int, input().split())) #수열

cnt = 0
for i in range(1, n):
    if arr[i] >= arr[i-1]:
        cnt += 1

print(cnt)