N = int(input())

arr = list(map(int, input().split()))

min_val = arr[0]

for elem in arr[1:]:
    if min_val > elem:
        min_val = elem

print(min_val, arr.count(min_val))