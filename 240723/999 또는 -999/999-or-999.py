arr = list(map(int, input().split()))

for elem in arr:
    if elem == 999 or elem == -999:
        idx = arr.index(elem)
        break

min_val, max_val = arr[0], arr[0]

for elem in arr[1:idx]:
    if elem > max_val:
        max_val = elem
    if min_val > elem:
        min_val = elem

print(max_val, min_val)