n = int(input())

price = list(map(int, input().split()))

# 최대 이익: 최솟값 구하고 최솟값 이후 값에서 최대 찾아서 빼기

prev_min_idx = 0
min_idx = 0

for i in range(prev_min_idx, n-1):
    if price[i] < price[min_idx]:
        min_idx = i

    prev_min_idx = min_idx

max_idx = min_idx
for j in range(prev_min_idx, n):
    if price[max_idx] < price[j]:
        max_idx = j

    prev_min_idx = max_idx

if min_idx == n-1:
    print('0')
else:
    print(price[max_idx] - price[min_idx])