n = int(input())

arr = list(map(int, input().split()))

cnt, ans = 0, 0
for idx, elem in enumerate(arr):
    if elem == 2:
        cnt += 1

    if cnt == 3:
        result = idx
        break

print(result + 1)