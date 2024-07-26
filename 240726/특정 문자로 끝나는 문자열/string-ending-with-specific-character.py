arr = [
    input()
    for _ in range(10)
]

alp = input()

cnt = 0
for i in range(10):
    if arr[i][-1] == alp:
        cnt += 1
        print(arr[i])

if cnt == 0:
    print('None')