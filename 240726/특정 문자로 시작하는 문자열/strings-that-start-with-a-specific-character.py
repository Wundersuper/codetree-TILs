n = int(input())
arr = [
    input()
    for _ in range(n)
]
alp = input()

cnt = 0
len_sum = 0
for i in range(n):
    if arr[i][0] == alp:
        cnt += 1
        len_sum += len(arr[i])

print(f'{cnt} {len_sum / cnt:.2f}')