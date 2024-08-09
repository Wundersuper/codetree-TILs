n = int(input())

line = [0 for _ in range(400)]

for i in range(n):
    a, b = tuple(map(int, input().split()))

    for j in range(a + 100, b + 100):
            line[j] += 1

print(max(line))