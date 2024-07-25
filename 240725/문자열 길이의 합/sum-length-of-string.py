n = int(input())

arr = [
    input()
    for _ in range(n)
]

cnt = 0
lens = 0

for elem in arr:
    if elem[0] == 'a':
        cnt += 1
    lens += len(elem)

print(lens, cnt)