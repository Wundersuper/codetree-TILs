arr = [
    list(map(int, input().split()))
    for _ in range(2)
]

for i in range(2):
    sum_v = 0
    for j in range(4):
        sum_v += arr[i][j]
    print(f'{sum_v / 4:.1f}', end = " ")
print()

for j in range(4):
    sum_v = 0
    for i in range(2):
        sum_v += arr[i][j]
    print(f'{sum_v / 2:.1f}', end = " ")
print()

sum_v = 0
for i in range(4):
    for j in range(2):
        sum_v += arr[j][i]
print(f'{sum_v / 8:.1f}')