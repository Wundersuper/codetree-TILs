x, y = tuple(map(int, input().split()))

cnt = 0
for k in range(x, y+1):
    list_k = list(map(int, str(k)))
    reverse_k = []
    for num in list_k[::-1]:
        reverse_k.append(num)
    
    if list_k == reverse_k:
        cnt += 1

print(cnt)