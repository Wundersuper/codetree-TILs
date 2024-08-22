n = int(input())
time = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

max_time = 0
for i in range(n):
    working = [0] * 1001
    for j in range(n):
        if i == j:
            continue
        
        a, b = time[j]
        for k in range(a, b):
            working[k] += 1

        total = [x for x in working if x >= 1]
    max_time = max(max_time, len(total))

print(max_time)