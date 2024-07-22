arr = list(map(int, input().split()))

ans = []

for elem in arr:
    if elem == 0:
        break
    ans.append(elem)

for elem in ans[::-1]:
    print(elem, end = " ")